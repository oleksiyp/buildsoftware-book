"""Figure 9.5: Larson's four states of a team, each with its own fix, and Encore's teams at month four."""
from dg import Diagram
from registry import figure


@figure
def fig_9_5():
    d = Diagram("fig-9-5", 864, 460, "The four states of a team",
                "Four states drawn as a rising staircase, after Will Larson. A team falling behind has more work "
                "arriving than it can finish; the fix is to hire more people until it is treading water. A team "
                "treading water keeps up but cannot reduce its backlog; the fix is to add process to consolidate "
                "its efforts and reduce concurrent work, that is, limit work in progress. A team repaying debt can "
                "at last pay down its accumulated problems; the fix is to add time. A team innovating can take on "
                "new work; the fix is to keep enough slack in the schedule to build quality in. At Encore's month "
                "four, Partner APIs was falling behind and shed webhook delivery; Inventory was repaying debt on "
                "the barcode core and needed protected time for characterization tests; the new Resale team was "
                "innovating by design. No team is named as treading water.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'DIAGNOSE THE STATE, THEN APPLY ITS FIX · AFTER LARSON (2018)</text>')
    W, H = 160, 56
    xs = [24, 236, 448, 660]
    ys = [232, 176, 120, 64]
    names = [("Falling behind", "more arrives than ends"), ("Treading water", "keeps up, backlog stays"),
             ("Repaying debt", "can pay down problems"), ("Innovating", "can take on new work")]
    for i in range(3):
        x0, y0, y1 = xs[i] + W, ys[i] + H // 2, ys[i + 1] + H // 2
        d.path([(x0, y0), (x0 + 24, y0), (x0 + 24, y1), (xs[i + 1], y1)])
    for i, ((n, sub), x, y) in enumerate(zip(names, xs, ys)):
        d.state(x, y, W, H, n, sub, kind="focal" if i == 3 else "backend")
    d.extra.append('<line class="dg-rule" x1="24" y1="312" x2="840" y2="312"/>')
    cols = [("FIX · HIRE", ["“Hire more people until the", "team moves into treading", "water.”"],
             "Encore, month 4: Partner APIs"),
            ("FIX · LIMIT WORK IN PROGRESS", ["“Add process to consolidate", "the team's efforts… and", "reduce concurrent work.”"],
             "Encore, month 4: none named"),
            ("FIX · ADD TIME", ["“Add time.”"], "Encore, month 4: Inventory"),
            ("FIX · KEEP SLACK", ["“Maintain enough slack in your", "team's schedule… to build", "quality into their work.”"],
             "Encore, month 4: Resale")]
    for x, (fix, q, team) in zip(xs, cols):
        d.extra.append(f'<text class="dg-eyebrow" x="{x}" y="332" style="text-anchor:start">{fix}</text>')
        for k, line in enumerate(q):
            d.note(x, 352 + 14 * k, line.replace("'", "’"))
        d.note(x, 408, team)
    d.legend([("backend", "State a team can be in"), ("focal", "Where a team can take on new work"),
              ("arrow:muted", "Its fix moves the team up a step")])
    return d
