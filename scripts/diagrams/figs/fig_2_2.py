"""Figure 2.2: the debt metaphor, from the WyCash report (1992) to the Dagstuhl definition (2016)."""
from dg import Diagram
from registry import figure


@figure
def fig_2_2():
    d = Diagram("fig-2-2", 864, 352, "The debt metaphor, 1980 to 2016",
                "A timeline from 1978 to 2018 on a proportional scale. Above the line: Lakoff and Johnson's "
                "Metaphors We Live By (1980), the book Cunningham later said shaped his interest in metaphor; "
                "Ward Cunningham's WyCash experience report, dated 26 March 1992 and presented at OOPSLA in "
                "Vancouver in October 1992, which coins the debt metaphor and says the debt is paid back with "
                "a rewrite; Martin Fowler's Refactoring (1999), which made refactoring a working vocabulary; and "
                "Cunningham's 2009 video, which retells the repayment as refactoring and says the metaphor was "
                "never a license to write code poorly. Below the line: William Opdyke's Illinois doctoral thesis "
                "(1992), which first defined refactoring in depth, in the same year as the report; Fowler's "
                "technical debt quadrant (2009), crossing reckless with prudent and deliberate with inadvertent; "
                "and the Dagstuhl seminar of April 2016, which agreed a definition centred on constructs "
                "expedient in the short term that make future change more costly or impossible. A bracket marks "
                "the 17 years between the coinage and Cunningham's gloss. The two Cunningham entries are "
                "highlighted.")
    X0, Y0, PER = 48, 1978, 19.2  # 1978 at x=48, 2018 at x=816
    AX = 168

    def yx(year):
        return round(X0 + (year - Y0) * PER)

    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'HOW ONE METAPHOR WAS COINED, RETOLD AND REDEFINED · PROPORTIONAL TIME</text>')
    # the axis, ticks every decade
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AX}" x2="{yx(2018)}" y2="{AX}"/>')
    for yr in (1980, 1990, 2000, 2010):
        x = yx(yr)
        d.zones.append(f'<line class="dg-axis" x1="{x}" y1="{AX}" x2="{x}" y2="{AX + 4}"/>')
    # events: (year, x, y, w, tag, name, sub, kind, up)
    up_y, down_y, H = 64, 216, 64
    events = [
        (1980, 40, up_y, 160, "1980 · LAKOFF & JOHNSON", "Metaphors We Live By", "metaphors shape thought",
         "backend"),
        (1992, 236, up_y, 168, "MARCH 1992 · CUNNINGHAM", "The WyCash report", "debt paid with a rewrite",
         "focal"),
        (1999, 432, up_y, 160, "1999 · FOWLER", "Refactoring", "a working vocabulary", "backend"),
        (2009, 620, up_y, 168, "2009 · CUNNINGHAM", "The debt video", "repaid by refactoring", "focal"),
        (1992, 236, down_y, 168, "1992 · OPDYKE, ILLINOIS", "Doctoral thesis", "refactoring defined", "backend"),
        (2009, 524, down_y, 168, "2009 · FOWLER", "The debt quadrant", "reckless vs prudent", "backend"),
        (2016, 712, down_y, 128, "APRIL 2016", "Dagstuhl 16162", "agreed definition", "backend"),
    ]
    for yr, x, y, w, tag, name, sub, kind in events:
        cx = yx(yr) // 4 * 4
        assert x + 8 <= cx <= x + w - 8, (name, cx)
        if y < AX:
            d.zones.append(f'<line class="dg-ill-soft" x1="{cx}" y1="{y + H}" x2="{cx}" y2="{AX}"/>')
        else:
            d.zones.append(f'<line class="dg-ill-soft" x1="{cx}" y1="{AX}" x2="{cx}" y2="{y}"/>')
        d.node(x, y, w, H, name, sub, kind, tag=tag)
        d.extra.append(f'<circle class="dg-dot dg-dot-ink" cx="{cx}" cy="{AX}" r="3.5"/>')
    d.note(608, 298, "× DELIBERATE VS INADVERTENT", anchor="middle")
    # tick labels
    for yr in (1980, 1990, 2000, 2010):
        x = yx(yr)
        if yr in (1990, 2010):
            d.extra.append(f'<text class="dg-tick" x="{x}" y="{AX - 6}" text-anchor="middle">{yr}</text>')
        else:
            d.extra.append(f'<text class="dg-tick" x="{x}" y="{AX + 16}" text-anchor="middle">{yr}</text>')
    # the 17 years between coinage and gloss
    a, b = yx(1992) // 4 * 4, yx(2009) // 4 * 4
    by = AX + 28
    d.zones.append(f'<path class="dg-ill-soft" d="M {a + 8},{by - 4} v 4 H {b - 8} v -4"/>')
    d.label_at("17 YEARS: KEEP THE DATES APART", (a + b) / 2, by - 6, horizontal=True, side="below")
    d.legend([("focal", "Cunningham's own words"), ("backend", "Work on the idea by others")])
    return d
