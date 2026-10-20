"""Figure 7.2: Encore's self-service onboarding funnel over four quarters, drawn as bars."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_7_2():
    d = Diagram("fig-7-2", 864, 420, "Encore's self-service onboarding funnel",
                "Horizontal bars for Encore's self-service venues over the four quarters before Verified "
                "Resale, with the share of sign-ups and the median time from sign-up for each step. Signed up: "
                "180 venues, 100%. Storefront provisioned (onboarding_storefront_provisioned): 178, 99%, 4 "
                "minutes. Payout account verified (onboarding_payout_account_verified): 161, 89%, 1 day. Seat map "
                "completed (onboarding_seat_map_completed): 97, 54%, 6 days. First event published "
                "(onboarding_first_event_published): 92, 51%, 7 days. First sale to a fan "
                "(onboarding_first_sale_recorded): 85, 47%, 13 days. The highlighted gap at the seat map, 64 "
                "venues, is the largest single loss. The provisioning workflow takes minutes; the venue's own "
                "work takes days.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'SELF-SERVICE VENUES · FOUR QUARTERS BEFORE VERIFIED RESALE</text>')
    X0, SCALE = 232, 2.6667  # 180 venues -> 480 px
    steps = [("Signed up", None, 180, "180 · 100% · —"),
             ("Storefront provisioned", "onboarding_storefront_provisioned", 178, "178 · 99% · 4 MIN"),
             ("Payout account verified", "onboarding_payout_account_verified", 161, "161 · 89% · 1 DAY"),
             ("Seat map completed", "onboarding_seat_map_completed", 97, "97 · 54% · 6 DAYS"),
             ("First event published", "onboarding_first_event_published", 92, "92 · 51% · 7 DAYS"),
             ("First sale to a fan", "onboarding_first_sale_recorded", 85, "85 · 47% · 13 DAYS")]
    Y0, RS = 64, 40
    d.extra.append(f'<text class="dg-label" x="{X0 + 480 + 8}" y="{Y0 - 8}" style="text-anchor:start">'
                   'VENUES · SHARE · MEDIAN</text>')
    prev = None
    for i, (name, ev, n, note) in enumerate(steps):
        y = Y0 + i * RS
        w = round(n * SCALE)
        d.extra.append(f'<text class="dg-name" x="{X0 - 12}" y="{y + 15 if ev else y + 20}" '
                       f'style="text-anchor:end">{escape(name)}</text>')
        if ev:
            d.extra.append(f'<text class="dg-sub" x="{X0 - 12}" y="{y + 28}" style="text-anchor:end">{ev}</text>')
        d.nodes.append(f'<rect class="dg-n dg-n-backend" x="{X0}" y="{y + 6}" width="{w}" height="20" rx="3"/>')
        if prev is not None and prev > n:
            pw = round(prev * SCALE)
            if name == "Seat map completed":
                d.nodes.append(f'<rect class="dg-ill-fill-accent" x="{X0 + w}" y="{y + 6}" width="{pw - w}" '
                               f'height="20" rx="3"/>')
                d.label_at("−64 VENUES · THE LARGEST LOSS", X0 + w + (pw - w) / 2, y + 16 - 8 + 12 + 8,
                           horizontal=True, side="below", kind="accent")
            else:
                d.nodes.append(f'<rect class="dg-n dg-n-optional" x="{X0 + w}" y="{y + 6}" width="{pw - w}" '
                               f'height="20" rx="3" stroke-dasharray="4,3"/>')
        d.note(X0 + 480 + 8, y + 20, note)
        prev = n
    # axis
    AY = Y0 + 6 * RS + 4
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{X0 + 480}" y2="{AY}"/>')
    for t in (0, 45, 90, 135, 180):
        xx = X0 + t * SCALE
        d.zones.append(f'<line class="dg-axis" x1="{xx:.1f}" y1="{AY}" x2="{xx:.1f}" y2="{AY + 4}"/>'
                       f'<text class="dg-tick" x="{xx:.1f}" y="{AY + 16}" text-anchor="middle">{t}</text>')
    d.zones.append(f'<text class="dg-axis-label" x="{X0 + 480}" y="{AY + 32}" text-anchor="end">VENUES</text>')
    d.note(24, AY + 52, "The workflow's own step takes minutes (99% provisioned in 4 min); "
           "the venue's own work takes days, and the seat map is where most give up.")
    d.legend([("backend", "Venues reaching the step"), ("optional", "Lost since the step before"),
              ("focal", "The largest loss")])
    return d
