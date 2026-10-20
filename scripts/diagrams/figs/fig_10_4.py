"""Figure 10.4: Encore's capacity allocation for year nine, as one bar of engineering capacity."""
from dg import Diagram
from registry import figure


@figure
def fig_10_4():
    d = Diagram("fig-10-4", 864, 316, "Encore's capacity allocation",
                "One bar of Encore's engineering capacity in year nine, about 400 engineers, divided in four. "
                "New product and features, 56%: bets, roadmap features and new markets; set as the residual after "
                "the other lines, and the only line negotiated each quarter. Keeping the lights on, 20%: unplanned "
                "work, on-call, upgrades and support escalations; measured as each team's trailing two-quarter "
                "share. Debt and risk, 14%: chosen by teams against their own scorecards and incidents; a floor of "
                "one-tenth per team, protected. Platform group, 10%: nine teams, 40 people; funded centrally before "
                "allocation and shown to each value stream as a platform tax.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'ENCORE · YEAR NINE · ABOUT 400 ENGINEERS · SHARE OF CAPACITY</text>')
    BY, BH = 56, 48
    segs = [(24, 456, "New product and features", "56%", "focal"),
            (480, 164, "Keeping the lights on", "20%", "backend"),
            (644, 112, "Debt and risk", "14%", "backend"),
            (756, 84, "Platform", "10%", "store")]
    cols = [24, 236, 448, 660]
    notes = [("NEGOTIATED EACH QUARTER",
              ["bets, roadmap features,", "new markets", "the residual after the", "other three lines"]),
             ("MEASURED",
              ["unplanned work, on-call,", "upgrades, escalations", "each team's trailing", "two-quarter share"]),
             ("PROTECTED",
              ["chosen by teams against", "scorecards and incidents", "floor of one-tenth per", "team; not raided"]),
             ("TOP-SLICED",
              ["platform group: nine", "teams, 40 people", "funded centrally; shown", "as a platform tax"])]
    TY = 152
    for (x, w, name, pct, kind), cx, (tag, lines) in zip(segs, cols, notes):
        mid = x + w // 2
        d.path([(mid, BY + BH), (mid, BY + BH + 16), (cx + 8, BY + BH + 16), (cx + 8, TY - 8)],
               kind="muted", arrow=False) if mid != cx + 8 else None
        d.node(x, BY, w, BH, name, pct, kind)
        d.extra.append(f'<text class="dg-label" x="{cx + 16}" y="{TY + 4}" style="text-anchor:start">{tag}</text>')
        d.extra.append(f'<text class="dg-name" x="{cx + 16}" y="{TY + 24}" style="text-anchor:start">{"Platform group" if name == "Platform" else name} · {pct}</text>')
        for i, t in enumerate(lines):
            d.note(cx + 16, TY + 44 + i * 15, t)
    d.legend([("focal", "Negotiated each quarter"), ("backend", "Measured or protected"),
              ("store", "Top-sliced before allocation")])
    return d
