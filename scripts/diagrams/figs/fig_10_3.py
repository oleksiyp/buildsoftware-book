"""Figure 10.3: four forecasts of the partner-API milestone, in weeks from the start of June."""
from html import escape

from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_10_3():
    d = Diagram("fig-10-3", 864, 356, "Four forecasts of one milestone",
                "Weeks from the start of June, when the forecasts were made at month 4, on a scale from 8 to 22, "
                "with the commitment, the start of October, at about week 17.4. Points converted to a date "
                "(410 points at 37 points a week): 11 weeks, with no percentile. Monte Carlo with a fixed backlog "
                "(80 items, the last 12 weeks' throughput): 10 weeks at the 50th percentile, 11 at the 85th. "
                "Monte Carlo with backlog growth (80 items grown by 30 to 65 percent): 15 weeks at the 50th, 17 at "
                "the 85th, the last week of September. The week-8 re-run, before the cut, on the remaining items "
                "after discovered work: the 85th percentile three weeks past the commitment. After the cut the "
                "85th percentile came back to late September, and the sandbox opened to Rowmate on 29 September.")
    p = Plot(d, x=248, y=48, w=568, h=208, xr=(8, 22), yr=(0, 4))
    p.axes(xticks=list(range(8, 23, 2)), yticks=[], xlabel="WEEKS FROM THE START OF JUNE (MONTH 4)", grid=False)
    for t in range(8, 23, 2):
        xx = p.px(t)
        d.zones.append(f'<line class="dg-grid" x1="{xx:.1f}" y1="48" x2="{xx:.1f}" y2="256"/>')
    commit = 122 / 7  # start of October: 122 days after 1 June
    p.vline(commit, kind="accent", dashed=True)
    d.label_at("COMMITMENT: START OF OCTOBER", p.px(commit), 40, horizontal=True, side="above", kind="accent")
    rows = [  # y value, name, sub
        (3.5, "Points converted to a date", "410 points ÷ 37 a week"),
        (2.5, "Monte Carlo, fixed backlog", "80 items, last 12 weeks"),
        (1.5, "Monte Carlo, with growth", "80 items, grown 30–65%"),
        (0.5, "Week-8 re-run, before cut", "after discovered work"),
    ]
    for y, name, sub in rows:
        yy = p.py(y)
        d.extra.append(f'<text class="dg-name" x="24" y="{yy - 1:.0f}" style="text-anchor:start">{escape(name)}</text>')
        d.extra.append(f'<text class="dg-sub" x="24" y="{yy + 12:.0f}" style="text-anchor:start">{escape(sub)}</text>')

    def p50(x, y):
        xx, yy = p.pt(x, y)
        d.nodes.append(f'<circle class="dg-dot-hollow" cx="{xx:.1f}" cy="{yy:.1f}" r="4" '
                       f'style="fill:var(--dg-paper);stroke:var(--dg-ink);stroke-width:1.4"/>')

    # row 1: single point
    p.dot(11, 3.5, kind="ink")
    p.annotate(11, 3.5, "11 WEEKS · NO PERCENTILE", dx=10, dy=3)
    # row 2
    p.line([(10, 2.5), (11, 2.5)], kind="soft")
    p50(10, 2.5); p.dot(11, 2.5, kind="ink")
    p.annotate(11, 2.5, "10 · 11 WEEKS", dx=10, dy=3)
    # row 3
    p.line([(15, 1.5), (17, 1.5)], kind="soft")
    p50(15, 1.5); p.dot(17, 1.5, kind="ink")
    p.annotate(15, 1.5, "15 · 17 WEEKS", dx=-10, dy=3, anchor="end")
    p.annotate(17, 1.5, "LAST WEEK OF SEPTEMBER", dx=-2, dy=-10, anchor="end")
    # row 4: re-run, then the cut
    late = commit + 3
    ax, ay = p.pt(late, 0.5)
    sx = p.px(122 / 7 - 2 / 7)  # 29 September
    d.path([(int(ax) // 4 * 4 - 8, int(ay) // 4 * 4), (int(sx) // 4 * 4 + 8, int(ay) // 4 * 4)], kind="muted")
    p.dot(late, 0.5, kind="accent")
    p.annotate(late, 0.5, "85% ≈ 3 WEEKS PAST", dx=-4, dy=-10, kind="accent", anchor="end")
    p.dot(122 / 7 - 2 / 7, 0.5, kind="ink")
    p.annotate(122 / 7 - 2 / 7, 0.5, "AFTER THE CUT: SANDBOX OPEN 29 SEP", dx=-10, dy=3, anchor="end")
    # legend (custom marks)
    y = d.h - 28
    lg = [f'<line class="dg-rule" x1="24" y1="{y - 12}" x2="{d.w - 24}" y2="{y - 12}"/>',
          f'<circle cx="30" cy="{y + 4}" r="4" style="fill:var(--dg-paper);stroke:var(--dg-ink);stroke-width:1.4"/>',
          f'<text class="dg-legend" x="40" y="{y + 7}">50th percentile</text>',
          f'<circle class="dg-dot dg-dot-ink" cx="150" cy="{y + 4}" r="4"/>',
          f'<text class="dg-legend" x="160" y="{y + 7}">85th percentile (or a single date)</text>',
          f'<line class="dg-series dg-s-accent" x1="372" y1="{y + 4}" x2="396" y2="{y + 4}" stroke-dasharray="5 4"/>',
          f'<text class="dg-legend" x="404" y="{y + 7}">The commitment</text>']
    d.extra.append("\n".join(lg))
    return d
