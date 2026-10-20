"""Figure 3.4: the two loops of Freeman and Pryce, with Beck's cycle inside."""
from dg import Diagram
from registry import figure


@figure
def fig_3_4():
    d = Diagram("fig-3-4", 864, 384, "Two loops",
                "The outer loop starts with an acceptance test for a whole feature, written from the outside in "
                "the language of the domain, which fails because the feature does not exist yet; the Resale "
                "team's first was that a resold ticket moves to the buyer and the old barcode dies. Inside it runs "
                "Kent Beck's inner loop, many times per feature: write a small failing unit test, make it pass "
                "with the simplest code that works, then refactor while the tests stay green, and start again. "
                "When the acceptance test passes the feature is done and the outer loop turns once, to the next "
                "feature. Fucci and colleagues found in 2017 that small, steady cycles went with better outcomes, "
                "and that whether the test came before the code did not.")
    d.zone(248, 100, 400, 184, "INNER LOOP · BECK, 2002 · MANY TURNS PER FEATURE")
    # outer loop return, drawn first
    d.path([(768, 148), (768, 56), (112, 56), (112, 148)], label="FEATURE DONE: THE OUTER LOOP TURNS ONCE", at=1)
    d.path([(200, 156), (272, 156)])
    d.path([(432, 156), (464, 156)])
    d.path([(544, 184), (544, 236), (528, 236)])
    d.path([(368, 236), (352, 236), (352, 184)])
    d.path([(624, 156), (696, 156)], dashed=True)
    d.node(24, 148, 176, 64, "Acceptance test", "fails: feature not built", "focal", tag="OUTER LOOP")
    d.node(272, 128, 160, 56, "Failing unit test", "one small step")
    d.node(464, 128, 160, 56, "Make it pass", "simplest code that works")
    d.node(368, 208, 160, 56, "Refactor", "tests stay green")
    d.node(696, 148, 144, 64, "Feature done", "acceptance passes")
    d.note(24, 236, "written first, from outside,")
    d.note(24, 250, "in the domain's language")
    d.note(24, 270, "e.g. a resold ticket moves")
    d.note(24, 284, "and the old barcode dies")
    d.note(696, 236, "when the steps add up")
    d.note(696, 250, "to the whole feature")
    d.note(256, 312, "Fucci et al., 2017: small, steady cycles went with better outcomes;")
    d.note(256, 326, "whether the test came before the code did not.")
    d.legend([("focal", "The executable goal"), ("backend", "A small, test-backed step"),
              ("arrow:muted", "Next step"), ("arrow:muted:dashed", "Until the acceptance test passes")])
    return d
