"""Figure 9.1: the Eagle at Data General, 1977-1981, as a schematic timeline and the team that built it."""
from dg import Diagram
from registry import figure


@figure
def fig_9_1():
    d = Diagram("fig-9-1", 864, 572, "The Eagle at Data General",
                "Schematic; only the dates named are documented. Top: a timeline from 1977 to 1981 in three lanes. "
                "In 1977 the rival Digital Equipment Corporation released the 32-bit VAX. Data General moved its lead "
                "development group to North Carolina to build an ambitious new 32-bit design, the Fountainhead "
                "Project, which fell behind and was cancelled. In 1978 Tom West, in Westborough, Massachusetts, "
                "proposed Eagle, a 32-bit extension of the Eclipse, as insurance, and promised it in a year; it was "
                "built in a basement and announced in April 1980 as the Eclipse MV/8000, later than promised. Then "
                "the team was broken up and West was sent to Japan before a single MV/8000 was sold, and by July "
                "1981, when Tracy Kidder's book appeared, many of the engineers had left or were leaving. Bottom: "
                "the team. Tom West led it with his deputy Carl Alsing; the Microkids, led by Alsing, wrote the "
                "microcode; the Hardy Boys, led by Ed Rasala, built the hardware; Steve Wallach was the architect. "
                "About two dozen engineers, most straight out of college, 'signed up' to do whatever the machine "
                "required, with overtime and no extra pay; the reward, 'pinball', was the chance to build the next.")
    px = lambda yr: round((160 + (yr - 1977) * 136) / 4) * 4  # noqa: E731
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'THE EAGLE AT DATA GENERAL, 1977–1981 · SCHEMATIC TIMELINE</text>')
    # year axis
    ax = [f'<line class="dg-ill-soft" x1="{px(1977)}" y1="64" x2="{px(1982)}" y2="64"/>']
    for yr in range(1977, 1983):
        ax.append(f'<line class="dg-ill-soft" x1="{px(yr)}" y1="60" x2="{px(yr)}" y2="68"/>')
    d.zones.append("\n".join(ax))
    for yr in range(1977, 1982):
        d.note(px(yr) + 68, 56, str(yr), anchor="middle")
    lanes = [(100, "RIVAL · DEC"), (168, "WESTBOROUGH, MA"), (240, "NORTH CAROLINA")]
    for y, name in lanes:
        d.note(24, y + 4, name)
    # DEC lane
    d.nodes.append(f'<circle class="dg-dot dg-dot-link" cx="{px(1977)}" cy="100" r="6"/>')
    d.note(px(1977) + 16, 104, "1977 · DEC releases the 32-bit VAX; the 16-bit Eclipse loses sales")
    # Westborough lane: Eagle
    a, b = px(1978), px(1980.25)
    d.nodes.append(f'<rect class="dg-ill-fill" x="{a}" y="156" width="{b - a}" height="24" rx="4"/>')
    d.extra.append(f'<text class="dg-sub" x="{(a + b) // 2}" y="171">EAGLE · BUILT IN A BASEMENT</text>')
    d.note(a, 144, "1978 · West proposes Eagle, promised in a year")
    c = px(1981.5)
    d.nodes.append(f'<line class="dg-ill-accent" x1="{b + 8}" y1="168" x2="{c - 8}" y2="168" stroke-dasharray="5 4"/>')
    d.nodes.append(f'<circle class="dg-dot dg-dot-accent" cx="{b}" cy="168" r="6"/>')
    d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{c}" cy="168" r="5"/>')
    d.note(b + 12, 144, "team broken up · West sent to Japan")
    d.note(b, 200, "April 1980 · announced as the Eclipse MV/8000", anchor="end")
    d.note(840, 200, "July 1981 · Kidder's book", anchor="end")
    d.note(840, 214, "many have left or are leaving", anchor="end")
    # North Carolina lane: Fountainhead
    f0, f1 = px(1977.5), px(1980)
    d.nodes.append(f'<rect class="dg-n dg-n-optional" x="{f0}" y="228" width="{f1 - f0}" height="24" rx="4" stroke-dasharray="4,3"/>')
    d.extra.append(f'<text class="dg-sub" x="{(f0 + f1) // 2}" y="243">FOUNTAINHEAD · NEW 32-BIT DESIGN</text>')
    d.extra.append(f'<path class="dg-ill-ink" d="M {f1 + 6},234 l 12,12 M {f1 + 18},234 l -12,12"/>')
    d.note(f1 + 28, 244, "fell behind; cancelled")
    # the team
    d.zone(24, 300, 816, 180, "THE EAGLE TEAM · ABOUT TWO DOZEN ENGINEERS, MOST STRAIGHT OUT OF COLLEGE")
    d.path([(344, 372), (344, 392), (156, 392), (156, 412)], arrow=False)
    d.path([(344, 372), (344, 392), (380, 392), (380, 412)], arrow=False)
    d.path([(344, 372), (344, 392), (604, 392), (604, 412)], arrow=False)
    d.path([(432, 348), (456, 348)], arrow=False)
    d.node(256, 324, 176, 48, "Tom West", "ran the Eclipse group")
    d.node(456, 324, 176, 48, "Carl Alsing", "deputy")
    d.node(56, 412, 200, 48, "The Microkids", "microcode · led by Alsing")
    d.node(280, 412, 200, 48, "The Hardy Boys", "hardware · led by Ed Rasala")
    d.node(516, 412, 176, 48, "Steve Wallach", "architect")
    d.note(24, 504, "“Signing up”: doing whatever the machine required, overtime included, for no extra pay.")
    d.note(24, 520, "“Pinball”: win one game and you get to play another; the prize was building the next machine.")
    d.legend([("backend", "Eagle and the people who built it"), ("optional", "Fountainhead, cancelled"),
              ("arrow:accent:dashed", "After the launch: the team broken up")])
    return d
