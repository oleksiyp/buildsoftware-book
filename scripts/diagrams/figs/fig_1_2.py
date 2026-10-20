"""Figure 1.2: Encore's engineering system at three sizes, and the default each size left behind."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_1_2():
    d = Diagram("fig-1-2", 864, 476, "Encore at three sizes",
                "Three stages from left to right, each with its people, code, path to production and the decision "
                "made by default. Year 1: 9 engineers in one team; one modular monolith in one repository; a "
                "pipeline one founder wrote and a few deploys a week; default: everyone reads everything, so "
                "nothing needs an owner. Year 4: 70 engineers in nine teams; seven services split from the "
                "monolith, whose repository was kept as the shared repository; a pipeline per service and about "
                "20 deploys a day; default: code that did not move with a service stays where it is, owned by "
                "whoever last touched it. Year 7: 400 engineers in 40 teams and a platform group; services in the "
                "shared repository and in their own, web and mobile frontends on one design system; golden path, "
                "trunk-based development and canaries, about 180 deploys a working day; default: code that works "
                "is left alone. A bar under each stage shows headcount on one scale. The defaults, outlined in "
                "vermilion, were never written down at the time.")
    W, xs = 248, (24, 308, 592)
    stages = [
        ("YEAR 1", "9 engineers", "one team", 9,
         ["One modular monolith", "in one repository"],
         ["A pipeline one founder wrote;", "a few deploys a week"],
         ["Everyone reads everything,", "so nothing needs an owner"]),
        ("YEAR 4", "70 engineers", "nine teams", 70,
         ["Seven services split from the", "monolith; its repository kept", "as the shared repository"],
         ["A pipeline per service;", "about 20 deploys a day"],
         ["Code that did not move with a", "service stays where it is, owned", "by whoever last touched it"]),
        ("YEAR 7", "400 engineers", "40 teams and a platform group", 400,
         ["Services in the shared repository", "and in their own; web and mobile", "frontends on one design system"],
         ["Golden path, trunk-based", "development, canaries; about", "180 deploys a working day"],
         ["Code that works", "is left alone"]),
    ]
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, 76), (b, 76)])
    accent = []
    for x, (tag, name, sub, n, code, path, default) in zip(xs, stages):
        d.node(x, 48, W, 56, name, sub, "backend", tag=tag)
        # headcount on one scale: 400 engineers = the column width after the number
        bw = max(4, round(n / 400 * (W - 32) / 4) * 4)
        d.note(x + 24, 128, f"{n}", anchor="end")
        d.zones.append(f'<rect class="dg-ill-fill" x="{x + 32}" y="{120}" width="{bw}" height="8" rx="1"/>')
        for label, lines, y0 in (("CODE", code, 160), ("PATH TO PRODUCTION", path, 240)):
            d.extra.append(f'<text class="dg-eyebrow" x="{x}" y="{y0}" style="text-anchor:start">{label}</text>')
            for k, line in enumerate(lines):
                d.note(x, y0 + 16 + 14 * k, line)
        # the default, one accent outline for all three
        y, h = 324, 84
        accent.append(f"M {x + 6},{y} h {W - 12} a 6 6 0 0 1 6 6 v {h - 12} a 6 6 0 0 1 -6 6 "
                      f"h -{W - 12} a 6 6 0 0 1 -6 -6 v -{h - 12} a 6 6 0 0 1 6 -6 z")
        d.extra.append(f'<text class="dg-eyebrow" x="{x + 12}" y="{y + 18}" style="text-anchor:start">'
                       f'DECISION MADE BY DEFAULT</text>')
        top = y + 40 if len(default) == 3 else y + 46
        for k, line in enumerate(default):
            d.extra.append(f'<text class="dg-name" x="{x + 12}" y="{top + 16 * k}" style="text-anchor:start">'
                           f'{escape(line)}</text>')
    d.zones.append(f'<path class="dg-ill-fill-accent" d="{" ".join(accent)}"/>')
    d.legend([("backend", "Stage of growth"), ("focal", "Default nobody wrote down at the time"),
              ("arrow:muted", "Growth; each default constrains the next size")])
    return d
