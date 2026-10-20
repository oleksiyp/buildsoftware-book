"""Figure 4.3: a request-routed preview in the staging cell, for the resale journey."""
from dg import Diagram
from registry import figure


@figure
def fig_4_3():
    d = Diagram("fig-4-3", 864, 404, "A request-routed preview",
                "Encore's staging cell runs a shared baseline of every service, continuously updated; the resale "
                "journey touches four of them: the Resale service, encore-core (the Orders & Payments purchase saga "
                "and Inventory's reissue), Venue Entry's revocation feed and Notifications, which replaces the "
                "seller's wallet pass. A preview for one change deploys only the services the change altered, here "
                "Resale, encore-core and the revocation feed, three repositories under one preview key. Ordinary "
                "requests flow through the baseline. Requests carrying the key are routed by the mesh to the "
                "preview versions wherever one exists, and to the baseline elsewhere, so the key-carrying request "
                "reaches the baseline Notifications, which the change did not touch. This works because every "
                "service propagates request context, as Encore's services already propagate traceparent, and the "
                "mesh can route on headers. The preview versions are torn down when the change merges; a full "
                "slice is kept only for journeys whose test data cannot be isolated in the baseline.")
    W, H = 136, 48
    cols = [200, 368, 536, 704]
    BY, PY = 104, 216                     # baseline row, preview row
    d.zone(184, 40, 672 - 16, 108, "STAGING CELL · SHARED BASELINE, CONTINUOUSLY UPDATED")
    d.zone(184, 184, 504, 88, "PREVIEW · ONLY THE CHANGED SERVICES · TORN DOWN ON MERGE")

    # connectors (drawn before boxes)
    bm, pm = BY + H // 2, PY + H // 2
    d.path([(160, bm), (cols[0], bm)])
    d.path([(160, pm), (cols[0], pm)], kind="link")
    for a, b in zip(cols, cols[1:3]):
        d.path([(a + W, bm), (b, bm)])
        d.path([(a + W, pm), (b, pm)], kind="link")
    # Resale -> Notifications: over the top for ordinary requests, under for keyed ones
    cx0, cx3 = cols[0] + W // 2, cols[3] + W // 2
    d.path([(cx0, BY), (cx0, 76), (cx3, 76), (cx3, BY)], label="WALLET PASS", at=1)
    d.path([(cx0, PY + H), (cx0, 300), (cx3, 300), (cx3, BY + H)], kind="link",
           label="NOT CHANGED: THE KEYED REQUEST USES THE BASELINE", at=1, side="below")

    # inputs
    d.node(24, BY, 136, H, "Ordinary request", "no preview key", "input")
    d.node(24, PY, 136, H, "Keyed request", "header: preview key", "focal")
    # baseline
    d.node(cols[0], BY, W, H, "Resale service", "baseline", "backend")
    d.node(cols[1], BY, W, H, "encore-core", "saga · reissue", "backend")
    d.node(cols[2], BY, W, H, "Venue Entry", "revocation feed", "backend")
    d.node(cols[3], BY, W, H, "Notifications", "wallet passes", "backend")
    # preview
    d.node(cols[0], PY, W, H, "Resale service", "changed version", "optional")
    d.node(cols[1], PY, W, H, "encore-core", "changed version", "optional")
    d.node(cols[2], PY, W, H, "Venue Entry", "changed feed", "optional")

    d.note(24, 340, "One key covers changes in three repositories. It works because every service propagates the")
    d.note(24, 354, "request's context (Encore already propagates traceparent) and the mesh can route on headers.")
    d.legend([("backend", "Baseline service"), ("optional", "Preview of a changed service"),
              ("arrow:muted", "Ordinary request"), ("arrow:link", "Request carrying the preview key")])
    return d
