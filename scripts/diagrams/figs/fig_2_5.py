"""Figure 2.5: Reissue sprouted beside the old barcode issuer, entering it through the tested pinch point."""
from dg import Diagram
from registry import figure


@figure
def fig_2_5():
    d = Diagram("fig-2-5", 864, 432, "Reissue, sprouted beside the issuer",
                "Inside Seat Inventory & Ticketing, owned by the Inventory team, two pieces of code sit side by "
                "side. On the right is the old barcode issuer: existing callers choose one of its issue variants, "
                "and every variant finally calls one pinch point that builds and persists a ticket. A "
                "characterization suite of 1,400 cases, running in continuous integration, pins what that pinch "
                "point does today. On the left is Reissue, a new class tested from birth. The Resale service calls "
                "it with a reissue request; Reissue makes exactly one call into the old issuer, through the pinch "
                "point the tests already cover, and does everything new in its own code: it revokes the old "
                "identity, issues a new opaque ticket_id, and emits the event for the ledger. Inventory owns "
                "issuance and revocation; Resale calls it, as an architecture decision record settled.")
    # zones
    d.zone(216, 48, 624, 328, "SEAT INVENTORY & TICKETING · INVENTORY TEAM")
    d.zone(536, 80, 288, 280, "THE OLD BARCODE ISSUER")
    # connectors first
    d.path([(168, 124), (560, 124)], kind="link", label="CHOOSE A VARIANT", at=0)
    d.path([(168, 236), (288, 236)], kind="link")
    d.label_at("reissue(request)", 228, 236, horizontal=True, side="above", kind="link")
    d.path([(480, 236), (560, 236)], kind="accent", label="ONE CALL")
    d.path([(680, 148), (680, 208)])
    d.path([(680, 296), (680, 264)], dashed=True)
    d.label_at("PINS TODAY'S BEHAVIOR", 680, 280, horizontal=False, side="right")
    # callers
    d.node(24, 96, 144, 56, "Existing callers", "today's issuance", "external")
    d.node(24, 208, 144, 56, "Resale service", "Resale team", "external")
    # the sprout
    d.node(288, 196, 192, 80, "Reissue", "new class · own tests", "focal", tag="SPROUTED")
    d.note(288, 300, "Everything new, in tested code:")
    d.note(288, 316, "· revokes the old identity")
    d.note(288, 330, "· issues a new opaque ticket_id")
    d.note(288, 344, "· emits the event for the ledger")
    # the old issuer
    d.node(560, 100, 240, 48, "issue* variants", "callers choose by channel, era")
    d.node(560, 208, 240, 56, "Pinch point", "builds and persists a ticket")
    d.node(560, 296, 240, 48, "Characterization suite", "1,400 cases · in CI", "store")
    d.legend([("focal", "New, tested code"), ("backend", "Old code"),
              ("store", "Tests"), ("arrow:link", "Caller"), ("arrow:accent", "The one call into the old code")])
    return d
