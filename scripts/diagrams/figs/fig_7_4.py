"""Figure 7.4: Encore's tenant lifecycle as a state machine, with what each state means."""
from dg import Diagram
from registry import figure


@figure
def fig_7_4():
    d = Diagram("fig-7-4", 864, 476, "Encore's tenant lifecycle",
                "Five states owned by the tenant directory, left to right. Trial, entered by sign-up: no public "
                "sales yet; services allow setup and test sales only. Live, entered when onboarding's verify step "
                "passes: normal sales and resale; services serve normally. Suspended, highlighted, entered only by "
                "a person's decision with a reason (event TenantSuspended): valid tickets stay valid and there are "
                "no new sales; services stop new sales, pause resale listings and hold payouts. A suspended tenant "
                "can be reinstated to live (TenantReinstated). Offboarding, entered from live by notice of "
                "termination or a switch (TenantOffboardingStarted): future events are honored or re-homed; "
                "services run the export, stop new events and keep serving existing tickets. Closed, entered when "
                "the retrieval period ends and irreversible: no tickets remain; services erase per schedule and "
                "issue a deletion record. Each transition is an event, and each consumer's handling of it is "
                "checked by a contract test. Separately, an event can be in the sub-state resale paused.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'OWNED BY THE TENANT DIRECTORY · EVERY TRANSITION IS AN EVENT</text>')
    xs = [28, 196, 364, 532, 700]
    W, Y, H = 136, 120, 48
    cx = [x + W // 2 for x in xs]
    CY = Y + H // 2
    # transitions (drawn before states)
    d.start(cx[0], 68)
    d.path([(cx[0], 74), (cx[0], Y)])
    d.path([(xs[0] + W, CY), (xs[1], CY)])
    d.path([(xs[1] + W, CY), (xs[2], CY)])
    d.path([(cx[2], Y + H), (cx[2], 196), (cx[1], 196), (cx[1], Y + H)],
           label="REINSTATED", at=1, side="below")
    d.path([(cx[1] + 24, Y), (cx[1] + 24, 84), (cx[3], 84), (cx[3], Y)],
           label="NOTICE OF TERMINATION OR SWITCH", at=1, side="above")
    d.path([(xs[3] + W, CY), (xs[4], CY)])
    states = [("trial", None, "backend"), ("live", None, "backend"), ("suspended", "only by a person", "focal"),
              ("offboarding", None, "backend"), ("closed", "irreversible", "backend")]
    for x, (name, sub, kind) in zip(xs, states):
        d.state(x, Y, W, H, name, sub, kind)
    rows = [("ENTERED BY", 240, [["Sign-up"], ["Onboarding's verify", "step passes"],
                                 ["A person's decision,", "with reason"], ["Notice of termination", "or switch"],
                                 ["Retrieval period ends"]]),
            ("WHAT IT MEANS FOR FANS", 300, [["No public sales yet"], ["Normal sales and resale"],
                                            ["Valid tickets stay", "valid; no new sales"],
                                            ["Future events honored", "or re-homed"], ["None remain"]]),
            ("WHAT EVERY SERVICE MUST DO", 360, [["Allow setup and", "test sales only"], ["Serve normally"],
                                                ["Stop new sales; pause", "resale listings;", "hold payouts"],
                                                ["Run export; stop new", "events; keep serving", "existing tickets"],
                                                ["Erase per schedule;", "issue deletion record"]])]
    for head, y, cells in rows:
        d.zones.append(f'<line class="dg-rule" x1="24" y1="{y - 16}" x2="840" y2="{y - 16}"/>')
        d.extra.append(f'<text class="dg-eyebrow" x="24" y="{y - 4}" style="text-anchor:start">{head}</text>')
        for x, lines in zip(xs, cells):
            for k, t in enumerate(lines):
                d.note(x, y + 12 + k * 13, t)
    d.note(24, 432, "Resale paused is a separate sub-state of one event: listings hidden, primary sales and "
           "valid tickets untouched.")
    d.legend([("backend", "Lifecycle state"), ("focal", "The delicate state"),
              ("arrow:muted", "Transition, published as an event")])
    return d
