"""Figure 6.4: the adoption funnel for shared webhook delivery, month 9 against month 11."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_6_4():
    d = Diagram("fig-6-4", 864, 324, "Adoption funnel for webhook delivery",
                "Two funnels side by side for the 14 services whose manifests declared exposure: partner by month "
                "11, one at month 9 and one at month 11. Aware means the owning team has seen the path's brief or "
                "newsletter entry: 14 at month 9, 14 at month 11. Tried means the service has sent a webhook "
                "through it in the sandbox: 7, then 10. Adopted means the service sends its production webhooks "
                "through it: 2, then 6. Still using after six months means adopted and has not reintroduced its "
                "own sender: no count yet at either month. The stall between tried and adopted lasted until "
                "retries became configurable per partner.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'SHARED WEBHOOK DELIVERY · 14 SERVICES WITH EXPOSURE: PARTNER</text>')
    stages = [("Aware", "has seen the path's brief or newsletter", 14, 14),
              ("Tried", "sent a webhook through it in the sandbox", 7, 10),
              ("Adopted", "sends its production webhooks through it", 2, 6),
              ("Still using at six months", "adopted, and no sender of its own again", None, None)]
    C9, C11, UNIT, Y0, RS, BH = 456, 704, 14, 72, 52, 32
    d.note(C9, 60, "MONTH 9", anchor="middle")
    d.note(C11, 60, "MONTH 11", anchor="middle")
    for i, (name, defin, m9, m11) in enumerate(stages):
        y = Y0 + i * RS
        d.extra.append(f'<text class="dg-name" x="24" y="{y + 14}" style="text-anchor:start">{escape(name)}</text>')
        d.note(24, y + 28, defin)
        for cx, v, kind in ((C9, m9, "input"), (C11, m11, "backend")):
            if v is None:
                w = 96
                d.nodes.append(f'<rect class="dg-n dg-n-optional" x="{cx - w // 2}" y="{y}" width="{w}" '
                               f'height="{BH}" rx="3" stroke-dasharray="4,3"/>')
                d.extra.append(f'<text class="dg-sub" x="{cx}" y="{y + 19}">no count yet</text>')
                continue
            w = v * UNIT
            d.nodes.append(f'<rect class="dg-n dg-n-{kind}" x="{cx - w // 2}" y="{y}" width="{w}" '
                           f'height="{BH}" rx="3"/>')
            d.extra.append(f'<text class="dg-name" x="{cx}" y="{y + 20}">{v}</text>')
    # the stall at month 9 (one accent element)
    ys, ya = Y0 + RS + BH // 2, Y0 + 2 * RS + BH // 2
    bx = C9 + 7 * UNIT // 2 + 16
    d.zones.append(f'<path class="dg-ill-accent" d="M {bx - 8},{ys} h 8 v {ya - ys} h -8"/>')
    d.label_at("STALL: 7 TRIED, 2 ADOPTED", bx, (ys + ya) // 2, horizontal=False, side="right", kind="accent")
    d.legend([("input", "Month 9"), ("backend", "Month 11"),
              ("optional", "No count yet")])
    return d
