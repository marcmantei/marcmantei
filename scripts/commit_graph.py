#!/usr/bin/env python3
"""Render the profile's commit-activity card as two self-contained SVGs.

One card, two readings of the same daily commit counts:
  - a weekly curve on a square-root scale, so quiet weeks stay visible
    next to the busy ones (the layout of Julien's commit graph), and
  - a day-by-day heatmap on the same columns (Shipyard Mission Control's
    commit calendar: same tokens, same Geist type).
Peak weeks carry marcmantei.com's accent, so the card belongs to the site.

Data comes from GitHub's GraphQL contributionsCollection: commits to
default branches across every repository the token can see, private
ones included. Repository names never leave this script; the card shows
totals only.

Standard library only, so the scheduled workflow needs no install step.

  GH_TOKEN=... python3 scripts/commit_graph.py --login marcmantei
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import math
import os
import pathlib
import sys
import urllib.request
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent
API = "https://api.github.com/graphql"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 100) {
        repository { nameWithOwner isPrivate }
        contributions(first: 100) { nodes { occurredAt commitCount } }
      }
    }
  }
}
"""


# ── Data ──────────────────────────────────────────────────────────────────

def graphql(token: str, variables: dict) -> dict:
    body = json.dumps({"query": QUERY, "variables": variables}).encode()
    request = urllib.request.Request(API, body, {
        "Authorization": f"bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "marcmantei-commit-graph",
    })
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    return payload["data"]


def fetch(token: str, login: str, start: dt.date, end: dt.date) -> dict:
    """Daily commit counts from start to end inclusive, plus repo totals.

    Queried in chunks of 61 days, so no repository can have more than 100
    contribution days in one response and nothing needs paging.
    """
    per_repo_day: dict[tuple[str, str], int] = {}
    private: dict[str, bool] = {}
    chunk_start = start
    while chunk_start <= end:
        chunk_end = min(end, chunk_start + dt.timedelta(days=60))
        data = graphql(token, {
            "login": login,
            "from": f"{chunk_start.isoformat()}T00:00:00Z",
            "to": f"{chunk_end.isoformat()}T23:59:59Z",
        })
        for entry in data["user"]["contributionsCollection"]["commitContributionsByRepository"]:
            repo = entry["repository"]["nameWithOwner"]
            private[repo] = entry["repository"]["isPrivate"]
            for node in entry["contributions"]["nodes"]:
                day = node["occurredAt"][:10]
                # Chunks can meet on the same day at their edges; a day is one value.
                per_repo_day[(repo, day)] = max(per_repo_day.get((repo, day), 0), node["commitCount"])
        chunk_start = chunk_end + dt.timedelta(days=1)

    days: dict[str, int] = {}
    repo_totals: dict[str, int] = {}
    for (repo, day), count in per_repo_day.items():
        if start.isoformat() <= day <= end.isoformat():
            days[day] = days.get(day, 0) + count
            repo_totals[repo] = repo_totals.get(repo, 0) + count
    active = [r for r, n in repo_totals.items() if n]
    return {
        "days": days,
        "repositories": len(active),
        "private_repositories": sum(1 for r in active if private[r]),
    }


# ── Model ─────────────────────────────────────────────────────────────────

def build(raw: dict, start: dt.date, today: dt.date, generated: dt.datetime) -> dict:
    series = []
    day = start
    while day <= today:
        series.append(raw["days"].get(day.isoformat(), 0))
        day += dt.timedelta(days=1)
    weeks = [sum(series[i:i + 7]) for i in range(0, len(series), 7)]

    streak = longest = 0
    for count in series:
        streak = streak + 1 if count else 0
        longest = max(longest, streak)

    return {
        "start": start, "today": today, "generated": generated,
        "series": series, "weeks": weeks,
        "total": sum(series),
        "this_week": weeks[-1],
        "avg_week": sum(series) / len(weeks),
        "peak_week": max(range(len(weeks)), key=lambda i: (weeks[i], i)),
        "active_days": sum(1 for c in series if c),
        "longest_streak": longest,
        "repositories": raw["repositories"],
        "private_repositories": raw["private_repositories"],
    }


# ── Render ────────────────────────────────────────────────────────────────

# Base and blues: Shipyard Mission Control (stack/portal/mission.html).
# Peak: marcmantei.com's accent (src/index.css). RGB triplets.
THEMES = {
    "dark": {
        "bg": (11, 11, 10), "fg": (243, 243, 238),
        "accent": (84, 150, 255), "line_old": (46, 98, 255), "line_new": (138, 198, 255),
        "peak": (255, 150, 105), "ok": (140, 214, 108),
        "empty": .055, "heat": (.18, .38, .65, .95), "area": .20,
    },
    "light": {
        "bg": (247, 247, 243), "fg": (16, 16, 15),
        "accent": (46, 98, 255), "line_old": (30, 62, 176), "line_new": (84, 150, 255),
        "peak": (232, 78, 38), "ok": (46, 140, 60),
        "empty": .06, "heat": (.20, .42, .68, .95), "area": .14,
    },
}

W, H = 1200, 776
PAD = 48
PLOT_L, PLOT_R = 100, W - PAD
CURVE_TOP, CURVE_BASE = 328, 494
MONTHS_Y = 530
HEAT_TOP = 548


def rgb(c, a=None) -> str:
    return f"rgb({c[0]} {c[1]} {c[2]})" if a is None else f"rgb({c[0]} {c[1]} {c[2]} / {a:g})"


def font_face(family: str, weight: int, file: str) -> str:
    data = base64.b64encode((ROOT / "fonts" / file).read_bytes()).decode()
    return (f'@font-face{{font-family:"{family}";font-weight:{weight};'
            f'src:url(data:font/woff2;base64,{data}) format("woff2")}}')


def nice_ticks(peak: int) -> list[int]:
    """Round values (1, 2.5, 5 times a power of ten) nearest to four evenly
    spaced positions in square-root space."""
    candidates = [m * 10 ** e for e in range(6) for m in (1, 2.5, 5)]
    top = math.sqrt(max(4, peak))
    ticks = {0}
    for k in (1, 2, 3, 4):
        target = top * k / 4
        ticks.add(int(min(candidates, key=lambda c: abs(math.sqrt(c) - target))))
    return sorted(ticks)


def monotone_path(points: list[tuple[float, float]]) -> str:
    """Fritsch-Carlson monotone cubic: smooth, and never dips below zero."""
    n = len(points)
    if n < 2:
        return ""
    xs, ys = zip(*points)
    d = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [d[0]] + [0.0 if d[i - 1] * d[i] <= 0 else (d[i - 1] + d[i]) / 2 for i in range(1, n - 1)] + [d[-1]]
    for i in range(n - 1):
        if d[i] == 0:
            m[i] = m[i + 1] = 0.0
            continue
        a, b = m[i] / d[i], m[i + 1] / d[i]
        if a * a + b * b > 9:
            t = 3 / math.sqrt(a * a + b * b)
            m[i], m[i + 1] = t * a * d[i], t * b * d[i]
    out = [f"M{xs[0]:.1f} {ys[0]:.1f}"]
    for i in range(n - 1):
        h = (xs[i + 1] - xs[i]) / 3
        out.append(f"C{xs[i] + h:.1f} {ys[i] + m[i] * h:.1f} {xs[i + 1] - h:.1f} "
                   f"{ys[i + 1] - m[i + 1] * h:.1f} {xs[i + 1]:.1f} {ys[i + 1]:.1f}")
    return "".join(out)


def peaks(weeks: list[int], limit: int = 5, gap: int = 4) -> list[int]:
    """The highest local maxima, at least `gap` weeks apart."""
    last = len(weeks) - 1
    candidates = [i for i in range(len(weeks)) if weeks[i]
                  and (i == 0 or weeks[i] >= weeks[i - 1]) and (i == last or weeks[i] >= weeks[i + 1])]
    chosen: list[int] = []
    for i in sorted(candidates, key=lambda i: -weeks[i]):
        if all(abs(i - j) >= gap for j in chosen):
            chosen.append(i)
        if len(chosen) == limit:
            break
    return sorted(chosen)


def heat_bands(peak_day: int) -> list[int]:
    """Upper bounds of the four heat levels on the curve's square-root scale,
    so one 200-commit day does not flatten every other day to level 1."""
    if not peak_day:
        return []
    return sorted({max(1, round(peak_day * (k / 4) ** 2)) for k in (1, 2, 3, 4)})


def fmt(n: float) -> str:
    return f"{n:,.0f}"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(model: dict, theme: str, login: str, tz: str) -> str:
    t = THEMES[theme]
    fg, accent, peak = t["fg"], t["accent"], t["peak"]
    ink3, ink4 = rgb(fg, .44), rgb(fg, .30)
    hair, hair2 = rgb(fg, .09), rgb(fg, .15)
    dot = t["line_new"] if theme == "dark" else accent

    weeks, series, start = model["weeks"], model["series"], model["start"]
    cols = len(weeks)
    col_w = (PLOT_R - PLOT_L) / cols
    cell = col_w - 3
    cx = lambda i: PLOT_L + col_w * (i + .5)

    ticks = nice_ticks(max(weeks))
    scale_top = max(ticks[-1], max(weeks), 1)
    cy = lambda v: CURVE_BASE - (CURVE_BASE - CURVE_TOP) * math.sqrt(v / scale_top)

    pk = model["peak_week"]
    peak_start = start + dt.timedelta(weeks=pk)

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-labelledby="t d">',
         f'<title id="t">{esc(login)} · commit activity</title>',
         f'<desc id="d">{fmt(model["total"])} commits across {model["repositories"]} repositories '
         f'({model["private_repositories"]} private) from {start.isoformat()} to {model["today"].isoformat()}. '
         f'{fmt(model["this_week"])} this week, {model["avg_week"]:.0f} per week on average. '
         f'Most active week starts {peak_start.isoformat()} with {fmt(weeks[pk])} commits. '
         f'Weekly curve on a square-root scale above a daily heatmap.</desc>']

    s.append("<defs>"
             f'<linearGradient id="ln" x1="{PLOT_L}" x2="{PLOT_R}" y1="0" y2="0" gradientUnits="userSpaceOnUse">'
             f'<stop offset="0" stop-color="{rgb(t["line_old"])}"/><stop offset="1" stop-color="{rgb(t["line_new"])}"/></linearGradient>'
             f'<linearGradient id="ar" x1="0" x2="0" y1="{CURVE_TOP}" y2="{CURVE_BASE}" gradientUnits="userSpaceOnUse">'
             f'<stop offset="0" stop-color="{rgb(accent)}" stop-opacity="{t["area"]}"/>'
             f'<stop offset="1" stop-color="{rgb(accent)}" stop-opacity="0"/></linearGradient>'
             '<linearGradient id="nm" x1="0" x2="1" y1="0" y2="0">'
             f'<stop offset="0" stop-color="{rgb(t["line_new"] if theme == "dark" else t["line_old"])}"/>'
             f'<stop offset="1" stop-color="{rgb(accent)}"/></linearGradient>'
             "</defs>")

    s.append("<style>"
             + font_face("Geist", 500, "Geist-Medium.subset.woff2")
             + font_face("Geist Mono", 400, "GeistMono-Regular.subset.woff2")
             + font_face("Geist Mono", 500, "GeistMono-Medium.subset.woff2")
             + "text{font-family:'Geist Mono',ui-monospace,'SF Mono',Menlo,Consolas,monospace;font-size:16px;"
             f"fill:{ink3};letter-spacing:-.02em}}"
             f".sans{{font-family:Geist,ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;font-weight:500;fill:{rgb(fg)}}}"
             ".h{font-size:40px;letter-spacing:-.05em}"
             ".v{font-size:50px;letter-spacing:-.06em;font-variant-numeric:tabular-nums}"
             ".k{font-size:14px;letter-spacing:.1em}"
             f".sub{{font-size:15px;fill:{ink4}}}"
             f".pk{{font-size:16px;font-weight:500;fill:{rgb(peak)};stroke:{rgb(t['bg'])};stroke-width:5px;"
             "paint-order:stroke;stroke-linejoin:round}"
             ".line{stroke-dasharray:1;stroke-dashoffset:1;animation:draw 1.8s cubic-bezier(.22,1,.36,1) .15s forwards}"
             ".fade{opacity:0;animation:fade .9s cubic-bezier(.22,1,.36,1) forwards}"
             "@keyframes draw{to{stroke-dashoffset:0}}@keyframes fade{to{opacity:1}}"
             "@media (prefers-reduced-motion:reduce){.line{animation:none;stroke-dashoffset:0}.fade{animation:none;opacity:1}}"
             "</style>")

    # Card and header
    s.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{rgb(t["bg"])}" stroke="{hair2}"/>')
    s.append(f'<text x="{PAD}" y="66" class="sans h">Commit activity</text>')
    s.append(f'<text x="{PAD}" y="98">@{esc(login)} · last {cols} weeks · every repository, private included</text>')
    s.append(f'<circle cx="{W - PAD - 222}" cy="56" r="4" fill="{rgb(t["ok"])}"/>')
    s.append(f'<text x="{W - PAD}" y="61" text-anchor="end">live · refreshed daily</text>')
    s.append(f'<line x1="{PAD}" x2="{W - PAD}" y1="126" y2="126" stroke="{hair}"/>')

    # Stats: five tiles across the card
    tiles = [
        ("TOTAL COMMITS", fmt(model["total"]),
         f'{model["repositories"]} repos · {model["private_repositories"]} private', True),
        ("THIS WEEK", fmt(model["this_week"]), "Monday to today", False),
        ("AVG / WEEK", f'{model["avg_week"]:.0f}', f"over {cols} calendar weeks", False),
        ("MOST ACTIVE WEEK", fmt(weeks[pk]), f'week of {peak_start.day} {peak_start.strftime("%b %Y")}', False),
        ("ACTIVE DAYS", fmt(model["active_days"]), f'longest streak {model["longest_streak"]} days', False),
    ]
    tile_w = (W - 2 * PAD) / len(tiles)
    for i, (label, value, sub, lead) in enumerate(tiles):
        x = PAD + tile_w * i
        fill = ' fill="url(#nm)"' if lead else ""
        s.append(f'<text x="{x:.1f}" y="164" class="k">{label}</text>')
        s.append(f'<text x="{x - 2:.1f}" y="216" class="sans v"{fill}>{value}</text>')
        s.append(f'<text x="{x:.1f}" y="246" class="sub">{esc(sub)}</text>')

    # Curve: section label and square-root ticks
    s.append(f'<text x="{PAD}" y="296" class="k">COMMITS / WEEK · √ SCALE</text>')
    s.append(f'<circle cx="{PAD + 290}" cy="291" r="4" fill="{rgb(peak)}"/>')
    s.append(f'<text x="{PAD + 302}" y="296" class="k">PEAK WEEKS</text>')
    for v in ticks:
        y = cy(v)
        dash = ' stroke-dasharray="2 5"' if v else ""
        s.append(f'<line x1="{PLOT_L}" x2="{PLOT_R}" y1="{y:.1f}" y2="{y:.1f}" stroke="{hair if v else hair2}"{dash}/>')
        s.append(f'<text x="{PLOT_L - 14}" y="{y + 5:.1f}" text-anchor="end">{fmt(v)}</text>')

    # The most active week, joined from its point on the curve to its heatmap column
    px = cx(pk)
    s.append(f'<line class="fade" style="animation-delay:1.4s" x1="{px:.1f}" x2="{px:.1f}" y1="{cy(weeks[pk]) + 6:.1f}" '
             f'y2="{HEAT_TOP - 4}" stroke="{rgb(peak, .5)}" stroke-dasharray="2 4"/>')

    points = [(cx(i), cy(v)) for i, v in enumerate(weeks)]
    settled = points[:-1] if len(points) > 2 else points
    path = monotone_path(settled)
    if path:
        s.append(f'<path class="fade" d="{path}L{settled[-1][0]:.1f} {CURVE_BASE}L{settled[0][0]:.1f} {CURVE_BASE}Z" fill="url(#ar)"/>')
        s.append(f'<path class="line" pathLength="1" d="{path}" fill="none" stroke="url(#ln)" stroke-width="2.5" '
                 'stroke-linecap="round" stroke-linejoin="round"/>')
    # The running week is a lower bound, not a value: dashed and hollow.
    if len(points) > 2:
        (x0, y0), (x1, y1) = points[-2], points[-1]
        s.append(f'<path class="fade" style="animation-delay:1.6s" d="M{x0:.1f} {y0:.1f}L{x1:.1f} {y1:.1f}" '
                 f'stroke="{rgb(t["line_new"])}" stroke-width="2" stroke-dasharray="3 4" fill="none"/>')
        s.append(f'<circle class="fade" style="animation-delay:1.6s" cx="{x1:.1f}" cy="{y1:.1f}" r="4" '
                 f'fill="{rgb(t["bg"])}" stroke="{rgb(t["line_new"])}" stroke-width="2"/>')
    for i, (x, y) in enumerate(settled):
        s.append(f'<circle class="fade" style="animation-delay:{.15 + 1.5 * i / cols:.2f}s" cx="{x:.1f}" cy="{y:.1f}" '
                 f'r="2.2" fill="{rgb(dot)}"/>')
    for i in peaks(weeks[:-1]):
        x, y = points[i]
        s.append(f'<circle class="fade" style="animation-delay:1.5s" cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{rgb(peak)}"/>')
        s.append(f'<text class="pk fade" style="animation-delay:1.5s" x="{x:.1f}" y="{y - 14:.1f}" '
                 f'text-anchor="middle">{fmt(weeks[i])}</text>')

    # Month labels, shared by curve and heatmap: at the column holding the 1st
    for col in range(cols - 1):
        monday = start + dt.timedelta(weeks=col)
        first = next((monday + dt.timedelta(days=d) for d in range(7)
                      if (monday + dt.timedelta(days=d)).day == 1), None)
        if first and col > 0:
            s.append(f'<text x="{PLOT_L + col_w * col + 1.5:.1f}" y="{MONTHS_Y}">{first.strftime("%b")}</text>')

    # Heatmap: Monday-first rows, one column per curve point
    bands = heat_bands(max(series))
    for row, name in ((0, "Mon"), (2, "Wed"), (4, "Fri")):
        s.append(f'<text x="{PLOT_L - 14}" y="{HEAT_TOP + col_w * row + cell / 2 + 5:.1f}" text-anchor="end" class="sub">{name}</text>')
    for col in range(cols):
        cells = []
        for row in range(7):
            i = col * 7 + row
            if i >= len(series):
                break
            v = series[i]
            level = next(k for k, upper in enumerate(bands, 1) if v <= upper) if v else 0
            fill = rgb(accent, t["heat"][level - 1]) if level else rgb(fg, t["empty"])
            day = start + dt.timedelta(days=i)
            cells.append(f'<rect x="{PLOT_L + col_w * col + 1.5:.1f}" y="{HEAT_TOP + col_w * row:.1f}" '
                         f'width="{cell:.1f}" height="{cell:.1f}" rx="2" fill="{fill}">'
                         f'<title>{day.strftime("%a")} {day.day} {day.strftime("%b %Y")} · {fmt(v)} commits</title></rect>')
        s.append(f'<g class="fade" style="animation-delay:{.1 + 1.2 * col / cols:.2f}s">{"".join(cells)}</g>')
    heat_h = col_w * 6 + cell
    s.append(f'<rect class="fade" style="animation-delay:1.4s" x="{PLOT_L + col_w * pk:.1f}" y="{HEAT_TOP - 3:.1f}" '
             f'width="{col_w:.1f}" height="{heat_h + 6:.1f}" rx="4" fill="none" stroke="{rgb(peak, .85)}" stroke-width="1.2"/>')

    # Footer: legend left, provenance right
    fy = HEAT_TOP + heat_h + 38
    s.append(f'<line x1="{PAD}" x2="{W - PAD}" y1="{fy - 22:.1f}" y2="{fy - 22:.1f}" stroke="{hair}"/>')
    legend = [("0", rgb(fg, t["empty"]))]
    low = 1
    for k, upper in enumerate(bands, 1):
        legend.append((str(upper) if low == upper else f"{low}-{upper}", rgb(accent, t["heat"][k - 1])))
        low = upper + 1
    x = PAD
    for label, color in legend:
        s.append(f'<rect x="{x}" y="{fy - 12:.1f}" width="13" height="13" rx="2" fill="{color}"/>')
        s.append(f'<text x="{x + 20}" y="{fy:.1f}" class="sub">{label}</text>')
        x += 20 + 9 * len(label) + 18
    s.append(f'<text x="{x + 2:.1f}" y="{fy:.1f}" class="sub">per day</text>')
    stamp = model["generated"].strftime("%Y-%m-%d %H:%M UTC")
    s.append(f'<text x="{W - PAD}" y="{fy:.1f}" text-anchor="end" class="sub">'
             f'{esc(tz)} · default branches · {stamp}</text>')

    s.append("</svg>")
    return "\n".join(s) + "\n"


# ── Main ──────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--login", default="marcmantei")
    parser.add_argument("--tz", default="Europe/Berlin")
    parser.add_argument("--weeks", type=int, default=53)
    parser.add_argument("--out", default=str(ROOT.parent / "assets"))
    parser.add_argument("--cache", help="read daily counts from this JSON if it exists, else write them there")
    args = parser.parse_args()

    generated = dt.datetime.now(dt.timezone.utc).replace(second=0, microsecond=0)
    today = generated.astimezone(ZoneInfo(args.tz)).date()
    start = today - dt.timedelta(days=today.weekday(), weeks=args.weeks - 1)

    cache = pathlib.Path(args.cache) if args.cache else None
    if cache and cache.exists():
        raw = json.loads(cache.read_text())
    else:
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            sys.exit("Set GH_TOKEN to a token that can read your contributions.")
        raw = fetch(token, args.login, start, today)
        if cache:
            cache.write_text(json.dumps(raw))

    model = build(raw, start, today, generated)
    out = pathlib.Path(args.out)
    for theme in THEMES:
        (out / f"commit-graph-{theme}.svg").write_text(render(model, theme, args.login, args.tz))
    print(f"{fmt(model['total'])} commits · {model['repositories']} repos · "
          f"peak week {fmt(model['weeks'][model['peak_week']])} · written to {out}")


if __name__ == "__main__":
    main()
