"""Figure 8.3: the listing state machine, with every rule checked on a transition."""
from dg import Diagram
from registry import figure


@figure
def fig_8_3():
    d = Diagram("fig-8-3", 864, 548, "The listing state machine",
                "A listing's states and transitions in Verified Resale. A seller lists on a partner or in Encore's "
                "app, and the listing becomes listed if it passes Gate provenance, the per-fan listing limit, a "
                "price at or below the cap, resale enabled for the event, the resale window open, and step-up "
                "sign-in after a recent credential change; owner Resale. When a buyer starts checkout the listing "
                "moves from listed to reserved, guarded by Bot Screening, the per-buyer limit and the window being "
                "open; owners Resale and Bot Screening. If payment is not authorized within 5 minutes it returns "
                "from reserved to listed. When payment is authorized with strong customer authentication it moves "
                "from reserved to sold, guarded by the primary payment service provider being available; owner "
                "Orders & Payments. When the sale is recorded it moves from sold to reissued: the old ticket "
                "identity is voided and a new one issued in one step; owner Inventory. From listed, a listing is "
                "withdrawn when the seller withdraws, the organizer disables resale, a rule change makes it "
                "invalid or the event is cancelled, and it expires when the window closes two hours before doors. "
                "The return, withdrawn and expired transitions have no guards and are owned by Resale. Partners "
                "are told of every transition by webhook and reconcile their copies hourly.")
    CY = 192  # main row centre
    # exits from listed, up to the two terminal states
    d.path([(120, 168), (120, 88)])
    d.path([(184, 168), (184, 128), (264, 128), (264, 88)])
    # the happy path
    d.start(28, CY)
    d.path([(34, CY), (96, CY)])
    d.path([(200, CY), (320, CY)], label="2 · CHECKOUT")
    d.path([(424, CY), (552, CY)], label="3 · PAID WITH SCA")
    d.path([(648, CY), (744, CY)], label="4 · RECORDED", kind="accent")
    d.path([(372, 216), (372, 248), (148, 248), (148, 216)], at=1, side="below",
           label="NOT PAID WITHIN 5 MINUTES")
    d.label_at("1 · LIST", 64, CY - 16, horizontal=True, side="above")
    d.state(96, 168, 104, 48, "listed")
    d.state(320, 168, 104, 48, "reserved")
    d.state(552, 168, 96, 48, "sold")
    d.state(744, 168, 96, 48, "reissued", "new identity", kind="focal")
    d.state(40, 40, 128, 48, "withdrawn", kind="optional")
    d.state(216, 40, 96, 48, "expired", kind="optional")
    # the unguarded exits, explained in the empty top right
    for i, line in enumerate(["WITHDRAWN: THE SELLER WITHDRAWS, THE ORGANIZER DISABLES RESALE,",
                              "A RULE CHANGE MAKES THE LISTING INVALID, OR THE EVENT IS CANCELLED",
                              "EXPIRED: THE WINDOW CLOSES, TWO HOURS BEFORE DOORS",
                              "NO GUARDS ON THESE EXITS OR ON THE RETURN · OWNER: RESALE"]):
        d.note(344, 52 + i * 15, line)
    # guard cards for the four guarded transitions
    cards = [("1 · → LISTED", "SELLER LISTS ON A PARTNER", "OR IN ENCORE'S APP",
              ["Gate provenance", "per-fan listing limit", "price at or below cap", "resale enabled",
               "window open", "step-up sign-in after", "a recent credential", "change"], "RESALE"),
             ("2 · LISTED → RESERVED", "BUYER STARTS CHECKOUT", None,
              ["Bot Screening", "per-buyer limit", "window open"], "RESALE, BOT SCREENING"),
             ("3 · RESERVED → SOLD", "PAYMENT AUTHORIZED WITH", "STRONG CUSTOMER AUTHENTICATION",
              ["primary PSP available"], "ORDERS & PAYMENTS"),
             ("4 · SOLD → REISSUED", "SALE RECORDED", None,
              ["old identity voided,", "new one issued,", "in one step"], "INVENTORY")]
    for i, (head, t1, t2, guards, owner) in enumerate(cards):
        x, y = 24 + i * 208, 292
        d.zone(x, y, 192, 176, head)
        d.note(x + 12, y + 22, t1)
        if t2:
            d.note(x + 12, y + 35, t2)
        gy = y + 56
        for k, g in enumerate(guards):
            if k == 0:
                d.note(x + 12, gy, "GUARDS")
            d.note(x + 56, gy + k * 13, g)
        d.note(x + 12, y + 164, "OWNER: " + owner)
    d.note(432, 496, "PARTNERS ARE TOLD OF EVERY TRANSITION BY WEBHOOK AND RECONCILE THEIR COPIES HOURLY",
           anchor="middle")
    d.legend([("start", "Created"), ("backend", "Live state"), ("optional", "Terminal, no sale"),
              ("focal", "The trust step")])
    return d
