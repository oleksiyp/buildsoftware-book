"""Figure 9.7: Encore's onboarding cohorts in year nine, days to first and to tenth merged change."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_9_7():
    rows = [("MONTHS 0–2", 9, 11, 71, ["baseline"]),
            ("MONTHS 3–5", 12, 6, 48, ["owner; buddy before", "day one; first task", "chosen in advance"]),
            ("MONTHS 6–8", 10, 4, 33, ["golden-path environment", "on day one; curriculum"]),
            ("MONTHS 9–11", 9, 3, 27, ["day-30 feedback survey", "fed into the curriculum"])]
    d = Diagram("fig-9-7", 864, 420, "Onboarding cohorts in year nine",
                "A line chart of Encore's four onboarding cohorts in year nine, with median days to a new "
                "engineer's first and tenth merged change. Months 0 to 2, 9 new engineers, the baseline: 11 days "
                "to first change, 71 to tenth. Months 3 to 5, 12 engineers, after onboarding got an owner, the "
                "buddy was assigned before day one and the first task was chosen in advance: 6 and 48. Months 6 "
                "to 8, 10 engineers, with the golden-path environment ready on day one and a curriculum: 4 and 33. "
                "Months 9 to 11, 9 engineers, after a day-30 feedback survey fed back into the curriculum: 3 and "
                "27. A shaded band marks the first week. The first change moved inside week one; the tenth fell more slowly.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="24" style="text-anchor:start">'
                   'MEDIAN DAYS, PER COHORT · YEAR NINE</text>')
    p = Plot(d, x=72, y=56, w=744, h=232, xr=(-0.5, 3.5), yr=(0, 80))
    p.axes(xticks=[], yticks=[0, 20, 40, 60, 80], ylabel="DAYS TO MERGED CHANGE")
    p.area([(-0.5, 7), (3.5, 7)], kind="soft")
    p.annotate(-0.5, 3.5, "WITHIN WEEK ONE", dx=8, dy=3)
    tenth = [(i, r[3]) for i, r in enumerate(rows)]
    first = [(i, r[2]) for i, r in enumerate(rows)]
    p.line(tenth, kind="ink")
    p.line(first, kind="accent")
    for i, (_, _, f, t, _) in enumerate(rows):
        p.dot(i, t, kind="ink", r=3.5)
        p.annotate(i, t, f"{t}", dx=8, dy=-6)
        p.dot(i, f, kind="accent", r=3.5)
    for i in range(4):
        p.annotate(i, rows[i][2], f"{rows[i][2]}", dx=8, dy=-10, kind="accent")
    for i, (lab, n, _, _, what) in enumerate(rows):
        cx = round(p.px(i))
        d.extra.append(f'<line class="dg-axis" x1="{cx}" y1="288" x2="{cx}" y2="292"/>')
        d.note(cx, 306, lab, anchor="middle")
        d.note(cx, 320, f"{n} new engineers", anchor="middle")
        for k, line in enumerate(what):
            d.note(cx, 342 + 13 * k, line, anchor="middle")
    d.legend([("arrow:muted", "Tenth merged change"), ("arrow:accent", "First merged change")])
    return d
