"""Figure 11.3: the barcode core's identity before and after the seam."""
from dg import Diagram
from registry import figure


@figure
def fig_11_3():
    d = Diagram("fig-11-3", 864, 540, "The identity, before and after the seam",
                "Two panels. Before the change: every reader reaches the ticket identity derived from order and "
                "seat directly. The issuer computes it in each of its 19 public variants; four other places in "
                "Encore's code recompute it; 60 call sites in 11 repositories owned by seven teams parse it out of "
                "the barcode; and copies outside Encore's repositories read it too, among them a partner's parser "
                "of the old event-code prefix and a vendor's turnstile firmware that computes it from order and seat. "
                "After the seam: the issuer's computation sits in the one pinch point every variant calls, the four "
                "other places and the migrated call sites ask one identity interface instead of computing or parsing, "
                "and partners receive an opaque ticket_id through the API while the turnstile vendor ships corrected "
                "firmware. Behind the interface sits the opaque identity with its lookup. Before it was trusted, a "
                "parallel run in month 8 computed the identity both ways on every issuance for three weeks, served "
                "the old result and logged two mismatches, both for tickets issued while an event was being rescheduled.")
    XS = [40, 240, 440, 640]
    NW, NH = 184, 44

    def panel(y0, label, readers, target, sub, kind, zh=172):
        d.zone(24, y0, 816, zh, label)
        for x, (name, s, k) in zip(XS, readers):
            d.node(x, y0 + 24, NW, NH, name, s, k)
            d.path([(x + NW // 2, y0 + 24 + NH), (x + NW // 2, y0 + 116)],
                   kind="link" if k == "external" else "muted")
        d.node(40, y0 + 116, 784, 40, target, sub, kind)

    panel(40, "BEFORE · EVERY READER REACHES THE REPRESENTATION",
          [("Issuer", "19 public variants compute it", "backend"),
           ("Four other places", "recompute it", "backend"),
           ("60 call sites", "11 repos · 7 teams · parse it", "backend"),
           ("Outside the repos", "partner parser · turnstiles", "external")],
          "Derived identity", "order + seat, readable by anyone", "store")
    panel(248, "AFTER · EVERY READER ASKS THE SEAM",
          [("Issuer", "in the one pinch point", "backend"),
           ("Four other places", "ask, never recompute", "backend"),
           ("60 call sites", "56 by month 8 · last 4 by m15", "backend"),
           ("Outside the repos", "API ticket_id · fixed firmware", "external")],
          "Identity interface", "the seam", "focal", zh=236)
    # behind the interface
    d.path([(432, 404), (432, 432)], kind="muted")
    d.node(240, 432, 384, 32, "Opaque identity + lookup", None, "store")
    d.note(640, 446, "PARALLEL RUN · MONTH 8 · 3 WEEKS")
    d.note(640, 460, "both ways · old result served")
    d.note(640, 474, "2 mismatches, both in reschedules")
    d.legend([("backend", "Encore code"), ("external", "Code outside Encore's repositories"),
              ("store", "The representation"), ("focal", "The seam")])
    return d
