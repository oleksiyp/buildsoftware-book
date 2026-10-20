"""Figure 6.3: the Resale team's journey to its first production deploy, as 23 working days laid end to end."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_6_3():
    d = Diagram("fig-6-3", 864, 464, "The Resale team's first deploy",
                "Seven steps laid end to end across 23 working days, with waiting shaded. Create the repository "
                "and service from the template: 1 day, no waiting. Walking-skeleton build with the pipeline green: "
                "2 days, no waiting. Sandbox partner credential: 5 days, all waiting, on a ticket to Security "
                "Engineering and a certificate issued by hand. Production partner credential: 4 days, all waiting, "
                "on a second ticket with a separate approval. Write a webhook sender, copied from Partner APIs': "
                "3 days, no waiting. Security review of the new sender: 6 days, all waiting, in the review queue "
                "with questions about the signing scheme. First production deploy and first webhook to Rowmate's "
                "sandbox: 2 days, no waiting. In total 23 working days, of which 15 were waiting: 9 for "
                "credentials and 6 for the review of a sender the platform did not offer.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'VERIFIED RESALE · REPOSITORY CREATED TO FIRST PRODUCTION DEPLOY · WORKING DAYS</text>')
    steps = [  # (step, second line: what the wait was for, or detail; days; waiting)
        ("Create repository and service from the template", None, 1, False),
        ("Walking-skeleton build; pipeline green", None, 2, False),
        ("Sandbox partner credential", "ticket to Security Eng.; cert by hand", 5, True),
        ("Production partner credential", "second ticket, separate approval", 4, True),
        ("Write a webhook sender", "copied from Partner APIs' sender", 3, False),
        ("Security review of the new sender", "review queue; signing-scheme questions", 6, True),
        ("First production deploy", "and first webhook to Rowmate's sandbox", 2, False),
    ]
    X0, DAY, Y0, RS, BH = 320, 20, 64, 40, 24
    wait = []
    t = 0
    for i, (name, why, days, waiting) in enumerate(steps):
        y = Y0 + i * RS
        d.extra.append(f'<text class="dg-note" x="24" y="{y + (10 if why else 16)}" '
                       f'style="fill:var(--dg-ink)">{escape(name)}</text>')
        if why:
            d.note(24, y + 23, why)
        x = X0 + t * DAY
        w = days * DAY
        if waiting:
            wait.append(f"M {x + 3},{y} h {w - 6} a 3 3 0 0 1 3 3 v {BH - 6} a 3 3 0 0 1 -3 3 "
                        f"h -{w - 6} a 3 3 0 0 1 -3 -3 v -{BH - 6} a 3 3 0 0 1 3 -3 z")
        else:
            d.nodes.append(f'<rect class="dg-n dg-n-backend" x="{x}" y="{y}" width="{w}" height="{BH}" rx="3"/>')
        d.extra.append(f'<text class="dg-sub" x="{x + w / 2:g}" y="{y + 15}">{days}</text>')
        t += days
    d.nodes.append(f'<path class="dg-ill-fill-accent" d="{" ".join(wait)}"/>')
    # day axis
    AY = Y0 + len(steps) * RS + 4
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{X0 + 23 * DAY}" y2="{AY}"/>')
    for k in (0, 5, 10, 15, 20, 23):
        xx = X0 + k * DAY
        d.zones.append(f'<line class="dg-axis" x1="{xx}" y1="{AY}" x2="{xx}" y2="{AY + 4}"/>')
        d.zones.append(f'<line class="dg-grid" x1="{xx}" y1="{Y0 - 8}" x2="{xx}" y2="{AY}"/>')
        d.extra.append(f'<text class="dg-tick" x="{xx}" y="{AY + 16}" text-anchor="middle">{k}</text>')
    d.extra.append(f'<text class="dg-axis-label" x="{X0 + 23 * DAY}" y="{AY + 32}" text-anchor="end">'
                   f'WORKING DAYS</text>')
    # brackets for the two missing capabilities
    BY = AY + 48
    for a, b, text in ((3, 12, "CREDENTIALS · 9 DAYS WAITING"), (15, 21, "SENDER REVIEW · 6 DAYS WAITING")):
        xa, xb = X0 + a * DAY, X0 + b * DAY
        d.zones.append(f'<path class="dg-ill-soft" d="M {xa},{BY - 6} v 6 h {xb - xa} v -6"/>')
        d.note((xa + xb) // 2, BY + 16, text, anchor="middle")
    d.label_at("23 DAYS · 15 OF THEM WAITING", X0 + 23 * DAY - 84, Y0 - 12, horizontal=True, side="above",
               kind="accent")
    d.legend([("backend", "The team's own work"), ("focal", "Waiting on another team"),
              ])
    return d
