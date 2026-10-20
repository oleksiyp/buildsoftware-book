"""Figure 5.5: Encore's staggered randomized rollout of background agents, year 9."""
from html import escape

from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_5_5():
    d = Diagram("fig-5-5", 864, 400, "A staggered randomized rollout",
                "A timeline in months from month 0 of year 9 to month 18, with one row for each of four cohorts "
                "of ten stream-aligned teams, drawn in random order. Cohort 1, which includes Inventory, receives "
                "background agents at month 3; cohort 2, which the Resale team joined when it formed at month 4, "
                "at month 6; cohort 3 at month 9; cohort 4 at month 12. Before its start each cohort is waiting "
                "and serves as comparison for the cohorts already using agents; the quarter just before its start "
                "is its baseline. Quality lag indicators are tracked for two quarters past each start, and the "
                "decision to expand, hold or withdraw is taken at each cohort start. A vertical line at month 9 "
                "marks the first answer, when cohort 1 had two quarters of use: merged changes per engineer up "
                "about 10% with an interval that includes no change, review time per change up about a fifth, "
                "rework rate flat, no detectable difference in change failure rate, and static warnings in "
                "changed code up in six of the ten teams.")
    p = Plot(d, x=192, y=56, w=648, h=192, xr=(0, 18), yr=(0, 4))
    p.axes(xticks=[0, 3, 6, 9, 12, 15, 18], yticks=[], grid=False,
           xlabel="MONTH, FROM MONTH 0 OF YEAR 9", xfmt=lambda v: f"M{v}")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   '40 TEAMS · 4 COHORTS OF 10 · ORDER DRAWN BY CHANCE · ONE QUARTER APART</text>')
    rows = [("Cohort 1", "incl. Inventory", 3), ("Cohort 2", "incl. Resale (from M4)", 6),
            ("Cohort 3", "10 teams", 9), ("Cohort 4", "10 teams", 12)]
    BH = 28
    for i, (name, sub, start) in enumerate(rows):
        cy = 56 + 24 + i * 44
        top = cy - BH // 2
        x0, xb, xs, xl, xe = p.px(0), p.px(start - 3), p.px(start), p.px(start + 6), p.px(18)
        if start > 3:
            d.zones.append(f'<rect class="dg-n dg-n-optional" x="{x0:.0f}" y="{top}" width="{xb - x0:.0f}" '
                           f'height="{BH}" rx="4" stroke-dasharray="4,3"/>')
            d.extra.append(f'<text class="dg-sub" x="{(x0 + xb) / 2:.0f}" y="{cy + 3}">waiting</text>')
        d.zones.append(f'<rect class="dg-n dg-n-input" x="{xb:.0f}" y="{top}" width="{xs - xb:.0f}" height="{BH}" rx="4"/>')
        d.extra.append(f'<text class="dg-sub" x="{(xb + xs) / 2:.0f}" y="{cy + 3}">baseline</text>')
        d.zones.append(f'<rect class="dg-n dg-n-backend" x="{xs:.0f}" y="{top}" width="{xe - xs:.0f}" height="{BH}" rx="4"/>')
        d.zones.append(f'<rect class="dg-area dg-ar-soft" x="{xs:.0f}" y="{top}" width="{min(xl, xe) - xs:.0f}" height="{BH}"/>')
        d.extra.append(f'<text class="dg-sub" x="{(xs + min(xl, xe)) / 2:.0f}" y="{cy + 3}">agents · lag watched</text>')
        if xl < xe:
            d.extra.append(f'<text class="dg-sub" x="{(xl + xe) / 2:.0f}" y="{cy + 3}">agents</text>')
        d.extra.append(f'<text class="dg-name" x="24" y="{cy - 1}" style="text-anchor:start">{escape(name)}</text>')
        d.note(24, cy + 12, sub)
    p.vline(9, kind="accent", dashed=False)
    d.zones.insert(1, d.nodes.pop())  # behind the bars: visible between the rows
    d.label_at("M9 · FIRST ANSWER", p.px(9), 56 - 4, horizontal=True, side="above", kind="accent")
    lines = ["First answer at month 9, cohort 1 after two quarters, later cohorts as comparison:",
             "merged changes per engineer ≈ +10% (interval includes no change) · review time per change ≈ +1/5",
             "rework rate flat · change failure rate: no detectable difference · warnings up in 6 of 10 teams"]
    for i, t in enumerate(lines):
        d.note(24, 296 + i * 16, t)
    d.legend([("optional", "Waiting: the comparison group"), ("input", "Baseline quarter"),
              ("backend", "Using background agents")])
    return d
