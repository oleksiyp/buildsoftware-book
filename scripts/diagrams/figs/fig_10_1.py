"""Figure 10.1: Polaris, 1955-1960, as a schematic timeline, with what PERT was and what delivered the programme."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_10_1():
    d = Diagram("fig-10-1", 864, 480, "Polaris, 1955 to 1960",
                "Schematic timeline from 1955 to 1964. A dashed bar shows the original plan: from the Special "
                "Projects Office's creation late in 1955, with Rear Admiral William F. Raborn as director, to an "
                "interim capability around 1963. A solid bar shows the programme as delivered, ending with the "
                "first deterrent patrol in November 1960; the missile that went to sea, the A-1, had less range "
                "and a smaller warhead than first wanted. Events marked on the axis: late 1955, the office is "
                "created; October 1957, Sputnik, after which the target moves to 1960; 1959, the PERT paper in "
                "Operations Research; 20 July 1960, USS George Washington makes the first launch from a submerged "
                "submarine; November 1960, the first deterrent patrol, roughly three years ahead of the original "
                "plan by the Navy's own account. Two panels below. The technique: PERT drew the programme as a "
                "network of events joined by activities, took three-point estimates weighted four to one toward "
                "the most likely time, and let the critical path set the date; contractors resented it and the "
                "office never evaluated it. What delivered the programme: a national priority, an office protected "
                "from rival bureaus, people who believed in the work, and scope that gave way to the date.")
    X0, PY = 72, 80  # 1955 at x=72, 80 px per year
    xs = lambda yr: int(round((X0 + (yr - 1955) * PY) / 4)) * 4  # noqa: E731
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'POLARIS · SPECIAL PROJECTS OFFICE · SCHEMATIC TIMELINE</text>')
    start, patrol, target = xs(1955.9), xs(1960.87), xs(1963.0)
    d.node(start, 56, target - start, 32, "Original plan: interim capability around 1963", kind="optional")
    d.node(start, 100, patrol - start, 32, "As delivered: first patrol, Nov 1960", kind="focal")
    d.note(patrol + 12, 120, "A-1: less range, smaller warhead")
    # axis
    AY = 156
    ax = [f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{xs(1964)}" y2="{AY}"/>']
    for yr in range(1955, 1965):
        x = xs(yr)
        ax.append(f'<line class="dg-axis" x1="{x}" y1="{AY}" x2="{x}" y2="{AY + 4}"/>')
        if yr < 1964:
            ax.append(f'<text class="dg-tick" x="{x + 40}" y="{AY - 8}" text-anchor="middle">{yr}</text>')
    d.zones.append("\n".join(ax))
    rows = {"A": 196, "B": 232, "C": 268}
    events = [  # year, row, anchor, line 1, line 2
        (1955.9, "A", "start", "LATE 1955", "office created, Raborn"),
        (1957.8, "A", "start", "OCT 1957", "Sputnik: target 1960"),
        (1959.5, "B", "end", "1959", "PERT paper published"),
        (1960.55, "C", "end", "20 JUL 1960", "first submerged launch"),
        (1960.87, "C", "start", "NOV 1960", "first deterrent patrol"),
        (1963.0, "A", "end", "AROUND 1963", "original interim target"),
    ]
    for yr, row, anchor, l1, l2 in events:
        x, y = xs(yr), rows[row]
        d.zones.append(f'<line class="dg-ill-soft" x1="{x}" y1="{AY}" x2="{x}" y2="{y + 16}"/>')
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{x}" cy="{AY}" r="3.5"/>')
        tx = x + 6 if anchor == "start" else x - 6
        d.extra.append(f'<text class="dg-label" x="{tx}" y="{y}" style="text-anchor:{anchor}">{escape(l1)}</text>')
        d.note(tx, y + 13, l2, anchor=anchor)
    # panels
    PY0 = 316
    panels = [(24, "THE TECHNIQUE · PERT, 1959",
               ["a network of events joined by activities",
                "three-point estimates, weighted 4:1",
                "toward the most likely time",
                "the critical path sets the date",
                "contractors resented it; never evaluated"]),
              (440, "WHAT DELIVERED THE PROGRAMME",
               ["a national priority",
                "an office protected from rival bureaus",
                "people who believed in the work",
                "scope that gave way to the date",
                "PERT's real service: a reputation, and freedom"])]
    for x, label, lines in panels:
        d.zone(x, PY0, 400, 104, label)
        for i, t in enumerate(lines):
            d.note(x + 16, PY0 + 24 + i * 16, t)
    d.legend([("optional", "Original plan"), ("focal", "The programme as delivered"),
              ("start", "Event")])
    return d
