"""Figure 9.2: an engineering organization's people as stocks and flows."""
from dg import Diagram
from registry import figure


@figure
def fig_9_2():
    d = Diagram("fig-9-2", 864, 404, "People as stocks and flows",
                "A stock-and-flow diagram. Hires flow into a stock of engineers who are ramping up. Ramping "
                "engineers flow into the stock of productive engineers through a valve whose rate is set by "
                "onboarding capacity, the time of experienced people; a buddy can usefully take one newcomer at a "
                "time. Productive engineers leave through two outflows, attrition and moves into management, and "
                "they also feed back into the valve, because they are the buddies for the next cohort; a cohort "
                "that ramped slowly becomes poorly prepared buddies. Each flow has a limit, and a growth target "
                "must be checked against all of them. Encore's year six, shown as an example: 150 hired, 20 left, "
                "and 145 of 250 engineers had joined within the previous 12 months.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'ENGINEERS AS STOCKS AND FLOWS · EVERY FLOW HAS A LIMIT</text>')
    Y = 132  # flow centre line

    def valve(cx, cy):
        d.extra.append(f'<path class="dg-mask" d="M {cx - 10},{cy - 12} L {cx + 10},{cy - 12} L {cx - 10},{cy + 12} '
                       f'L {cx + 10},{cy + 12} Z"/>'
                       f'<path class="dg-ill-ink" d="M {cx - 10},{cy - 12} L {cx + 10},{cy - 12} L {cx - 10},{cy + 12} '
                       f'L {cx + 10},{cy + 12} Z"/>')

    # flows (drawn first)
    d.path([(152, Y), (272, Y)])
    d.label_at("HIRES", 240, Y, horizontal=True, side="above")
    d.path([(456, Y), (576, Y)])
    d.path([(668, Y + 40), (668, 252)])
    d.path([(760, Y + 40), (760, 252)])
    # feedback: productive engineers teach the next cohort
    d.path([(620, Y - 40), (620, 64), (516, 64), (516, Y - 16)], kind="accent")
    d.label_at("EXPERIENCED TIME · ONE NEWCOMER PER BUDDY", 568, 64, horizontal=True, side="above", kind="accent")
    valve(196, Y)
    valve(516, Y)
    d.label_at("ONBOARDING CAPACITY", 516, Y + 12, horizontal=True, side="below")
    # stocks and sinks
    d.node(24, Y - 28, 128, 56, "Candidates", "outside Encore", kind="external")
    d.node(272, Y - 40, 184, 80, "Ramping", "stock: still learning", kind="focal")
    d.node(576, Y - 40, 264, 80, "Productive", "stock: can ship and teach", kind="store")
    d.node(612, 252, 112, 48, "Attrition", "regretted or not", kind="external")
    d.node(732, 252, 108, 48, "Management", "leaves the stock", kind="external")
    # year six numbers
    d.note(24, Y + 64, "Year six at Encore: 150 hired, 20 left; 145 of 250 had joined within 12 months.")
    d.note(24, Y + 80, "Fewer engineers with a year's tenure than newcomers, so buddies were")
    d.note(24, Y + 96, "doubled up, borrowed from other teams or skipped.")
    d.note(24, 340, "Slow ramping one year leaves poorly trained buddies the next; the limit is a stock, not effort.")
    d.legend([("focal", "Stock that grows when the valve is narrow"), ("store", "Stock"),
              ("external", "Source or sink"), ("arrow:accent", "Feedback: who teaches")])
    return d
