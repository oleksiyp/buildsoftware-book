"""Figure 6.1: the Programmer's Workbench at Bell Labs, a schematic of the installation and its timeline."""
from html import escape

from dg import Diagram, label_width
from registry import figure


@figure
def fig_6_1():
    d = Diagram("fig-6-1", 864, 560, "The Programmer's Workbench, 1973–78",
                "Schematic, not a floor plan. Left: programmers, about 1,100 of them by the end of 1977, who "
                "before the workbench carried decks of punched cards and sent their jobs straight to each target "
                "machine. Centre: the Programmer's Workbench, PWB/UNIX, a set of PDP-11s dedicated to development "
                "(seven PDP-11/45s and /70s by the end of 1977), with its small tools: the PWB shell by John Mashey, "
                "the Source Code Control System by Marc Rochkind, find, cpio and expr by Dick Haight, and the "
                "Remote Job Entry subsystem, which sent jobs to the targets and brought their output back. Right: "
                "the target machines, two IBM 370/168s, two UNIVAC 1100-series systems and an XDS Sigma 5. "
                "Bottom: a timeline. In 1972 Rochkind began SCCS on an IBM System/370; in mid-1973 Evan Ivie "
                "proposed doing development on a dedicated machine; late in 1973 the first PDP-11/45 was installed; "
                "PWB/UNIX 1.0 was released on 1 July 1977; by the end of 1977 the main installation ran seven "
                "PDP-11s for about 1,100 people; in 1978 Dolotta, Haight and Mashey described it in the Bell "
                "System Technical Journal.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'SCHEMATIC · THE MAIN BELL LABS INSTALLATION AT THE END OF 1977</text>')
    # ---- connectors first --------------------------------------------------------------------
    d.path([(176, 116), (224, 116)])
    d.path([(100, 144), (100, 216)], dashed=True)
    d.path([(100, 272), (100, 352), (756, 352), (756, 296)], dashed=True,
           label="BEFORE: CARDS AND JOBS STRAIGHT TO EACH TARGET", at=1, side="below")
    for ty in (116, 188, 260):
        d.path([(568, 260), (616, 260), (616, ty), (672, ty)] if ty != 260 else [(568, 260), (672, 260)],
               kind="link")
    d.label_at("JOBS · OUTPUT", 620, 260, horizontal=True, side="below", kind="link")
    # ---- the workbench (one accent element) ---------------------------------------------------
    FX, FY, FW, FH = 224, 64, 360, 256
    d.zones.append(f'<rect class="dg-n dg-n-focal" x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="8"/>')
    lab = "PROGRAMMER'S WORKBENCH · PWB/UNIX"
    lw = label_width(lab)
    d.zones.append(f'<rect class="dg-mask" x="{FX + 12}" y="{FY - 6}" width="{lw}" height="12" rx="2"/>'
                   f'<text class="dg-eyebrow" x="{FX + 12 + lw / 2:g}" y="{FY + 3}">{escape(lab)}</text>')
    for k in range(7):
        x = 240 + k * 40
        d.nodes.append(f'<rect class="dg-ill-fill" x="{x}" y="84" width="28" height="20" rx="2"/>')
        d.nodes.append(f'<line class="dg-ill-soft" x1="{x + 6}" y1="98" x2="{x + 22}" y2="98"/>')
    d.note(240, 124, "seven PDP-11/45s and /70s, for development only")
    tools = [(240, 148, "PWB shell", "John Mashey"), (424, 148, "SCCS", "Marc Rochkind"),
             (240, 232, "find, cpio, expr", "Dick Haight"), (424, 232, "Remote Job Entry", "jobs out, output back")]
    for x, y, name, sub in tools:
        d.node(x, y, 144, 56, name, sub, "backend")
    # ---- people and the targets ---------------------------------------------------------------
    d.node(24, 88, 152, 56, "Programmers", "about 1,100 by 1977", "input")
    d.node(24, 216, 152, 56, "Card decks", "thrown away by most", "optional")
    d.note(672, 76, "TARGET MACHINES")
    d.node(672, 88, 168, 56, "2 × IBM 370/168", "batch, own job language", "external")
    d.node(672, 160, 168, 56, "2 × UNIVAC 1100", "1100-series systems", "external")
    d.node(672, 232, 168, 56, "XDS Sigma 5", "one machine", "external")
    # ---- timeline -----------------------------------------------------------------------------
    AX, AY, X0, X1 = 48, 456, 48, 816
    span = (1972.0, 1979.0)
    px = lambda yr: X0 + (yr - span[0]) / (span[1] - span[0]) * (X1 - X0)  # noqa: E731
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{X1}" y2="{AY}"/>')
    for yr in range(1972, 1980):
        xx = px(yr)
        d.zones.append(f'<line class="dg-axis" x1="{xx:.1f}" y1="{AY - 3}" x2="{xx:.1f}" y2="{AY + 3}"/>')
    d.note(X1 + 8, AY + 3, "1979")
    d.note(X0 - 8, AY + 3, "1972", anchor="end")
    events = [  # (year, text, tier: negative above, positive below, anchor)
        (1972.8, "1972 · ROCHKIND BEGINS SCCS ON AN IBM 370", -2, "start"),
        (1973.5, "MID-1973 · IVIE: DEVELOP ON A DEDICATED MACHINE", 1, "start"),
        (1973.9, "LATE 1973 · FIRST PDP-11/45 INSTALLED", -1, "start"),
        (1977.5, "1 JULY 1977 · PWB/UNIX 1.0", 1, "end"),
        (1977.95, "END OF 1977 · 7 PDP-11 MACHINES, ABOUT 1,100 USERS", -2, "end"),
        (1978.5, "1978 · THE BELL SYSTEM TECHNICAL JOURNAL PAPER", 2, "end"),
    ]
    for yr, text, tier, anchor in events:
        xx = round(px(yr))
        ty = AY + (tier * 22 - 6 if tier < 0 else tier * 22 + 2)
        y1, y2 = (ty + 4, AY) if tier < 0 else (AY, ty - 9)
        d.zones.append(f'<line class="dg-ill-soft" x1="{xx}" y1="{y1}" x2="{xx}" y2="{y2}"/>')
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{xx}" cy="{AY}" r="3.5"/>')
        d.extra.append(f'<text class="dg-note" x="{xx + (4 if anchor == "start" else -4)}" y="{ty}" '
                       f'text-anchor="{anchor}">{escape(text)}</text>')
    d.legend([("input", "Users"), ("focal", "Dedicated to development"),
              ("backend", "Small tool"), ("external", "Target machine"),
              ("arrow:link", "Remote Job Entry"), ("arrow:muted:dashed", "Before PWB")])
    return d
