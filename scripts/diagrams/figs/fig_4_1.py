"""Figure 4.1: Git in 2005, from the BitKeeper break to version 1.0 (April enlarged)."""
from html import escape

from dg import Diagram
from registry import figure

AXIS = 264
APR_X0, APR_PX = 72, 12          # 1 April at x=72, 12 px a day
REST_X0, REST_X1 = 452, 816      # 1 May .. 31 December
MONTH_START = {5: 0, 6: 31, 7: 61, 8: 92, 9: 123, 10: 153, 11: 184, 12: 214}  # days after 1 May


def X(month, day):
    if month == 4:
        return APR_X0 + (day - 1) * APR_PX
    off = MONTH_START[month] + day - 1
    return int(round((REST_X0 + off * (REST_X1 - REST_X0) / 244) / 4) * 4)


def text(d, x, y, s, cls="dg-note", anchor="start"):
    d.extra.append(f'<text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anchor}">{escape(s)}</text>')


@figure
def fig_4_1():
    d = Diagram("fig-4-1", 864, 420, "Git in 2005",
                "A timeline. Before Git, from 1991 to 2002, Linux kernel changes travelled as patches and tarballs "
                "applied by hand by Linus Torvalds; from 2002 to 2005 the kernel used BitKeeper, BitMover's "
                "proprietary system, offered free to open-source developers. In the spring of 2005, after Andrew "
                "Tridgell wrote a client that read BitKeeper's metadata, BitMover withdrew the free license. "
                "The 2005 axis below draws April at about eight times the scale of May to December. By the commonly "
                "cited chronology, work on Git began on 3 April. On 6 April Torvalds posted 'Kernel SCM saga..' "
                "to the linux-kernel list, saying he would stop using BitKeeper. On 7 April Git committed its own "
                "source, 'Initial revision of git, the information manager from hell'. On 18 April came the first "
                "merge of several branches; on 19 April Olivia Mackall announced Mercurial, for the same reason. "
                "On 16 June Git managed the 2.6.12 kernel release, about ten weeks after it first hosted itself. "
                "On 26 July Torvalds handed maintenance to Junio Hamano, and Git 1.0 appeared on 21 December 2005.")
    # ---- before Git ---------------------------------------------------------------------------
    d.zone(24, 32, 816, 80, "BEFORE GIT")
    d.node(72, 52, 228, 44, "Patches and tarballs", "1991–2002 · applied by hand", "input")
    d.node(332, 52, 228, 44, "BitKeeper", "2002–2005 · free to open source", "input")
    d.node(592, 52, 224, 44, "Free license withdrawn", "spring 2005 · BitMover", "external")
    d.path([(300, 74), (332, 74)])
    d.path([(560, 74), (592, 74)])

    # ---- 2005 axis ----------------------------------------------------------------------------
    d.zone(24, 136, 816, 260, "2005 · APRIL DRAWN ENLARGED")
    ax = [f'<line class="dg-axis" x1="{APR_X0}" y1="{AXIS}" x2="{X(4, 30) + 8}" y2="{AXIS}"/>',
          f'<line class="dg-axis" x1="{REST_X0 - 8}" y1="{AXIS}" x2="{REST_X1}" y2="{AXIS}"/>',
          f'<line class="dg-axis" x1="{X(4, 30) + 4}" y1="{AXIS + 5}" x2="{X(4, 30) + 12}" y2="{AXIS - 5}"/>',
          f'<line class="dg-axis" x1="{REST_X0 - 12}" y1="{AXIS + 5}" x2="{REST_X0 - 4}" y2="{AXIS - 5}"/>']
    # month boundaries and names
    for m in range(5, 13):
        xx = X(m, 1)
        ax.append(f'<line class="dg-axis" x1="{xx}" y1="{AXIS}" x2="{xx}" y2="{AXIS + 4}"/>')
    for day in (1, 10, 20, 30):
        xx = X(4, day)
        ax.append(f'<line class="dg-axis" x1="{xx}" y1="{AXIS}" x2="{xx}" y2="{AXIS + 4}"/>')
    d.zones.append("\n".join(ax))
    for day, lab in ((1, "1 APR"), (10, "10"), (30, "30 APR")):
        d.extra.append(f'<text class="dg-tick" x="{X(4, day)}" y="{AXIS + 16}" text-anchor="middle">{lab}</text>')
    names = {5: "MAY", 6: "JUN", 7: "JUL", 8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC"}
    for m, n in names.items():
        nxt = X(m + 1, 1) if m < 12 else REST_X1
        d.extra.append(f'<text class="dg-tick" x="{(X(m, 1) + nxt) / 2:g}" y="{AXIS + 16}" '
                       f'text-anchor="middle">{n}</text>')

    # ---- events: (month, day, lane y, head, detail, accent) -----------------------------------
    events = [
        (4, 3, 164, "3 APR · WORK BEGINS", "by the commonly cited chronology", False),
        (4, 6, 196, "6 APR · “KERNEL SCM SAGA..”", "Torvalds stops using BitKeeper", False),
        (4, 7, 228, "7 APR · GIT HOSTS ITSELF", "“the information manager from hell”", True),
        (4, 19, 296, "19 APR · MERCURIAL ANNOUNCED", "by Olivia Mackall, same reason", False),
        (4, 18, 332, "18 APR · FIRST MERGE", "of several branches", False),
        (6, 16, 196, "16 JUN · KERNEL 2.6.12", "the first release Git managed", True),
        (7, 26, 296, "26 JUL · JUNIO HAMANO", "takes over maintenance", False),
        (12, 21, 196, "21 DEC · GIT 1.0", "", False),
    ]
    for m, day, ly, head, detail, accent in events:
        xx = X(m, day)
        above = ly < AXIS
        anchor = "end" if (m, day) == (12, 21) else "start"
        tx = xx - 6 if anchor == "end" else xx + 6
        if above:
            d.zones.append(f'<line class="dg-ill-soft" x1="{xx}" y1="{ly - 10}" x2="{xx}" y2="{AXIS}"/>')
        else:
            d.zones.append(f'<line class="dg-ill-soft" x1="{xx}" y1="{AXIS}" x2="{xx}" y2="{ly + 4}"/>')
        cls = "dg-label dg-l-accent" if accent else "dg-label"
        d.extra.append(f'<text class="{cls}" x="{tx}" y="{ly}" style="text-anchor:{anchor};font-size:8.5px">'
                       f'{escape(head)}</text>')
        if detail:
            text(d, tx, ly + 13, detail, anchor=anchor)
        d.nodes.append(f'<circle class="dg-dot dg-dot-{"accent" if accent else "ink"}" cx="{xx}" cy="{AXIS}" '
                       f'r="{4.5 if accent else 3.5}"/>')

    # ---- the ten weeks ----------------------------------------------------------------------------
    a, b, by = X(4, 7), X(6, 16), 364
    d.zones.append(f'<path class="dg-ill-ink" d="M {a},{by - 8} V {by} H {b} V {by - 8}"/>')
    d.label_at("ABOUT 10 WEEKS FROM SELF-HOSTING TO A KERNEL RELEASE", (a + b) / 2, by,
               horizontal=True, side="below")
    return d
