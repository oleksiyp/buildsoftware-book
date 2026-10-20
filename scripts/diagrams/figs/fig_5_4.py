"""Figure 5.4: the validation ladder for Encore's barcode call-site migration."""
from dg import Diagram
from registry import figure


@figure
def fig_5_4():
    d = Diagram("fig-5-4", 864, 424, "The validation ladder",
                "Five rungs, run in order from left to right on each of the 60 agent-generated changes, one per "
                "call site, in 11 repositories owned by seven teams. Each rung costs more than the one before. "
                "Rung 1, build and static checks, run by CI (continuous integration): the change compiles and "
                "passes lint and fitness functions; at Encore it caught 4 changes that imported the lookup client "
                "in a forbidden direction. Rung 2, characterization and unit tests, run by CI with tests the agent "
                "cannot edit: old behavior preserved where it should be; it caught 7 changes that altered behavior "
                "at an edge. Rung 3, the sponsor's inspection by Ines: the change does what the spec says and "
                "nothing else; it caught 9 changes with unrelated improvements, reverted hunk by hunk. Rung 4, "
                "owner review, one shard per team, by the owning team: the change is right for this code and its "
                "context; one shard, Venue Entry's, was rejected outright (Section 5.3). Rung 5, progressive "
                "delivery by canary, as for any change: behavior in production; it caught nothing.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   '60 AGENT CHANGES · ONE PER CALL SITE · 11 REPOSITORIES · 7 OWNING TEAMS</text>')
    W, H, G, Y = 152, 64, 16, 120
    xs = [24 + i * (W + G) for i in range(5)]
    d.zone(20, 96, 2 * W + G + 8, 268, "MACHINE CHECKS")
    d.zone(xs[2] - 4, 96, 2 * W + G + 8, 268, "PEOPLE")
    d.zone(xs[4] - 4, 96, W + 8, 268, "PRODUCTION")
    d.path([(xs[0], 60), (xs[4] + W, 60)], label="EACH RUNG COSTS MORE THAN THE ONE BEFORE", side="below",
           arrow=True)
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, Y + 36), (b, Y + 36)])
    rungs = [
        ("Build, static", "lint, fitness functions", "1 · CI", "backend",
         ["compiles; passes lint", "and fitness functions"],
         ["4 changes importing the", "lookup client in a", "forbidden direction"]),
        ("Tests", "characterization + unit", "2 · CI, LOCKED TESTS", "backend",
         ["old behavior preserved", "where it should be;", "agent cannot edit tests"],
         ["7 changes that altered", "behavior at an edge"]),
        ("Sponsor's look", "Ines inspects", "3 · SPONSOR", "backend",
         ["does what the spec says,", "and nothing else"],
         ["9 changes with unrelated", "\"improvements\", reverted", "hunk by hunk"]),
        ("Owner review", "one shard per team", "4 · OWNING TEAM", "focal",
         ["right for this code", "and its context"],
         ["one shard rejected", "outright: Venue Entry's", "offline scanner (5.3)"]),
        ("Canary", "progressive delivery", "5 · AS FOR ANY CHANGE", "backend",
         ["behavior in production"],
         ["nothing"]),
    ]
    for x, (name, sub, tag, kind, checks, caught) in zip(xs, rungs):
        d.node(x, Y, W, H + 8, name, sub, kind, tag=tag)
        d.extra.append(f'<text class="dg-eyebrow" x="{x + 4}" y="{Y + 104}" style="text-anchor:start">CHECKS</text>')
        for i, t in enumerate(checks):
            d.note(x + 4, Y + 120 + i * 14, t)
        d.extra.append(f'<text class="dg-eyebrow" x="{x + 4}" y="{Y + 184}" style="text-anchor:start">'
                       'CAUGHT AT ENCORE</text>')
        for i, t in enumerate(caught):
            d.note(x + 4, Y + 200 + i * 14, t)
    d.legend([("backend", "Rung of checks"), ("focal", "The rung that caught what every test passed"),
              ("arrow:muted", "Changes move on to the next rung")])
    return d
