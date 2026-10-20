"""Figure 1.1: Garmisch, 1968 — the working conference (schematic) and the years around it, to scale."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_1_1():
    d = Diagram("fig-1-1", 864, 500, "Garmisch, 1968",
                "Schematic, top: people from three constituencies, the users of computers, their manufacturers "
                "and the universities, more than 50 from 11 countries, came to the NATO conference at Garmisch, "
                "7 to 11 October 1968, chaired by Friedrich L. Bauer. It worked in three groups, on the design, "
                "the production and the service of software. Rapporteurs' notes and tape recordings became the "
                "report, written in Munich by Peter Naur and Brian Randell and published in January 1969. "
                "Bottom, a timeline to scale: late 1967, the NATO Science Committee's study group recommends the "
                "conference; April 1968, Conway's 'How Do Committees Invent?' appears in Datamation; 7 to 11 "
                "October 1968, Garmisch; January 1969, the report; 27 to 31 October 1969, the second conference "
                "near Rome, after which the series was not continued; 1972, Dijkstra's Turing lecture 'The Humble "
                "Programmer' calls Garmisch the turning point and makes 'software crisis' canonical.")
    # ---- the conference, schematic ---------------------------------------------------------
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'THE WORKING CONFERENCE · SCHEMATIC</text>')
    for i, name in enumerate(("Computer users", "Manufacturers", "Universities")):
        y = 64 + i * 52
        d.node(24, y, 144, 40, name, None, "input")
        d.path([(168, y + 20), (200, y + 20)])
    d.zone(200, 56, 360, 148, "GARMISCH · 7–11 OCT 1968 · CHAIR F. L. BAUER")
    for i, name in enumerate(("Design", "Production", "Service")):
        d.node(216 + i * 112, 84, 104, 56, name, "working group", "backend")
    d.note(380, 168, "more than 50 people · 11 countries", anchor="middle")
    d.note(380, 184, "Dijkstra, Perlis, Naur, McIlroy, Randell", anchor="middle")
    d.path([(560, 112), (704, 112)], label="NOTES AND TAPES")
    d.node(704, 84, 136, 56, "The report", "Naur & Randell", "backend")
    d.note(772, 160, "written in Munich", anchor="middle")
    d.note(772, 174, "published Jan 1969", anchor="middle")

    # ---- the timeline, to scale ------------------------------------------------------------
    d.extra.append('<text class="dg-eyebrow" x="24" y="244" style="text-anchor:start">'
                   'BEFORE AND AFTER · TIMELINE TO SCALE</text>')
    AY, X0, X1, Y0, Y1 = 380, 64, 816, 1967.5, 1973.0

    def px(t):
        return round((X0 + (t - Y0) / (Y1 - Y0) * (X1 - X0)) / 4) * 4

    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{X1}" y2="{AY}"/>')
    for yr in range(1968, 1973):
        x = px(yr)
        d.zones.append(f'<line class="dg-axis" x1="{x}" y1="{AY - 4}" x2="{x}" y2="{AY + 4}"/>')
        # 1969's label sits left of its tick, clear of the January 1969 stem
        anchor, tx = ("end", x - 3) if yr == 1969 else ("middle", x)
        d.extra.append(f'<text class="dg-tick" x="{tx}" y="{AY + 16}" text-anchor="{anchor}">{yr}</text>')

    def event(t, tier, date, lines, anchor="start", accent=False):
        """tier < 0: above the axis; > 0: below. Text sits beside the stem's end."""
        x = px(t)
        ty = AY + tier * 28
        d.zones.append(f'<line class="dg-ill-soft" x1="{x}" y1="{AY}" x2="{x}" y2="{ty + (8 if tier < 0 else -8)}"/>')
        dot = "dg-dot dg-dot-accent" if accent else "dg-dot dg-dot-ink"
        d.nodes.append(f'<circle class="{dot}" cx="{x}" cy="{AY}" r="{5 if accent else 4}"/>')
        tx = x + 6 if anchor == "start" else x - 6
        top = ty - 4 - 12 * (len(lines)) if tier < 0 else ty
        cls = "dg-label dg-l-accent" if accent else "dg-label"
        d.extra.append(f'<text class="{cls}" x="{tx}" y="{top + 8}" style="text-anchor:{anchor}">'
                       f'{escape(date)}</text>')
        for k, line in enumerate(lines):
            d.extra.append(f'<text class="dg-note" x="{tx}" y="{top + 22 + 12 * k}" text-anchor="{anchor}">'
                           f'{escape(line)}</text>')

    event(1967.9, -3, "LATE 1967", ["NATO study group", "recommends a conference"])
    event(1968.29, 1, "APR 1968", ["Conway, 'How Do", "Committees Invent?'"], anchor="end")
    event(1968.77, -1, "7–11 OCT 1968", ["Garmisch: 'software", "engineering' named"], accent=True)
    event(1969.04, 1, "JAN 1969", ["the report", "is published"])
    event(1969.82, -3, "27–31 OCT 1969", ["near Rome: 'a lack of", "communication'; series ends"])
    event(1972.6, 1, "1972", ["Dijkstra, 'The Humble Programmer':", "'software crisis' made canonical"],
          anchor="end")
    d.legend([("input", "Who came"), ("backend", "Working group or output"),
              ("arrow:muted", "Flow of material"), ("start", "Event; vermilion: Garmisch")])
    return d
