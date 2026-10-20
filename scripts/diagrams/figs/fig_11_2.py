"""Figure 11.2: Verified Resale's 23 dependencies at month 4 and the 14 left at month 9, by team, with how each cut went."""
from html import escape

from dg import Diagram
from registry import figure

ROWS = [  # team, month 4, cut kinds (R = taken over by Resale, P = moved to the platform, F = folded), how
    ("Inventory", 3, "R", ["Proof of a Gate purchase built by Resale from existing",
                           "TicketIssued events instead of a new call"]),
    ("Venue Entry", 3, "F", ["The revocation feed folded into Inventory's reissue change",
                             "as TicketRevoked, which Venue Entry's list builder consumes"]),
    ("Orders & Payments", 2, "", ["—"]),
    ("Bot Screening", 2, "R", ["Per-buyer limits written by Resale in the rules engine,",
                               "reviewed by Bot Screening"]),
    ("Billing & Payouts", 3, "", ["—"]),
    ("Partner APIs", 3, "PR", ["Webhook delivery moved to the platform;",
                               "listing endpoints written by Resale"]),
    ("Organizer Console", 1, "", ["—"]),
    ("Mobile App", 2, "R", ["The Resale module in the fan app taken over by Resale;",
                            "the release train and version floor remain"]),
    ("Fan Messaging", 2, "R", ["The two messages written by Resale on Fan Messaging's templates;",
                               "pass replacement remains, as a contract"]),
    ("Design System", 1, "R", ["Badge and capped-price field contributed by Resale",
                               "through the contribution path"]),
    ("Security Engineering", 1, "P", ["Partner credentials became self-service",
                                      "on the platform's partner-facing path"]),
]


@figure
def fig_11_2():
    desc = ("Verified Resale's cross-team dependencies by the team that must deliver, at the first quarterly plan "
            "(month 4) and at month 9, drawn as one square per dependency: solid squares remained, dashed squares "
            "were cut, lettered by how the work moved (R taken over by Resale, P moved to the platform, F folded "
            "into a change already planned). "
            + " ".join(f"{t}: {n} to {n - len(c)}; {' '.join(h)}." for t, n, c, h in ROWS)
            + " Of Inventory's two that remained, one is VR-01, the void and reissue in one step inside the barcode "
              "core, the dependency that blocked. Total: 23 at month 4, 14 at month 9; the nine cuts were six taken "
              "over by Resale, two moved to the platform and one folded into a change already planned.")
    RS, Y0 = 36, 64
    H = Y0 + len(ROWS) * RS + 48 + 44
    d = Diagram("fig-11-2", 864, H, "Where nine dependencies went", desc)
    SX, SQ, STEP = 192, 16, 24
    CX, HX = 280, 336
    eb = lambda x, y, t, a="start": d.extra.append(  # noqa: E731
        f'<text class="dg-eyebrow" x="{x}" y="{y}" style="text-anchor:{a}">{escape(t)}</text>')
    eb(24, 44, "TEAM THAT MUST DELIVER")
    eb(SX, 44, "MONTH 4")
    eb(CX, 44, "4 → 9")
    eb(HX, 44, "HOW THE DIFFERENCE WENT")
    for r, (team, n, cuts, how) in enumerate(ROWS):
        y = Y0 + r * RS
        if r:
            d.zones.append(f'<line class="dg-rule" x1="24" y1="{y - 6}" x2="840" y2="{y - 6}"/>')
        d.extra.append(f'<text class="dg-name" x="24" y="{y + 16}" style="text-anchor:start">{escape(team)}</text>')
        kept = n - len(cuts)
        for i in range(n):
            x = SX + i * STEP
            if i < kept:
                accent = team == "Inventory" and i == 0
                cls = "dg-ill-fill-accent" if accent else "dg-n dg-n-backend"
                d.nodes.append(f'<rect class="{cls}" x="{x}" y="{y + 4}" width="{SQ}" height="{SQ}" rx="2"/>')
            else:
                d.nodes.append(f'<rect class="dg-n dg-n-optional" x="{x}" y="{y + 4}" width="{SQ}" height="{SQ}" '
                               f'rx="2" stroke-dasharray="3,2"/>')
                d.extra.append(f'<text class="dg-label" x="{x + SQ // 2}" y="{y + 15}">{cuts[i - kept]}</text>')
        d.extra.append(f'<text class="dg-tick" x="{CX}" y="{y + 15}">{n} → {kept}</text>')
        if len(how) == 1:
            d.note(HX, y + 15, how[0])
        else:
            d.note(HX, y + 9, how[0])
            d.note(HX, y + 21, how[1])
    ty = Y0 + len(ROWS) * RS
    d.zones.append(f'<line class="dg-axis" x1="24" y1="{ty - 6}" x2="840" y2="{ty - 6}"/>')
    d.extra.append(f'<text class="dg-name" x="24" y="{ty + 16}" style="text-anchor:start">Total</text>')
    d.extra.append(f'<text class="dg-tick" x="{CX}" y="{ty + 15}">23 → 14</text>')
    d.note(HX, ty + 15, "Taken over by Resale 6 · moved to the platform 2 · folded into a change already planned 1")
    d.legend([("backend", "Remained at month 9"), ("optional", "Cut: R by Resale · P platform · F folded"),
              ("focal", "VR-01, reissue in the barcode core: the one that blocked")])
    return d
