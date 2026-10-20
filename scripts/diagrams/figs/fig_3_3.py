"""Figure 3.3: Khorikov's four quadrants for sorting code by the testing it deserves, with Encore's code placed."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_3_3():
    d = Diagram("fig-3-3", 864, 496, "Sorting code by what it deserves",
                "A two-by-two grid after Khorikov. The horizontal axis is the number of collaborators the code "
                "talks to, few to many; the vertical axis is its complexity or domain significance, low to high. "
                "Top left, complex with few collaborators: domain model and algorithms, which deserve thorough unit "
                "tests because that is where the bugs that matter live; Encore's fee split, made a pure function, "
                "sits here. Top right, complex and entangled with many collaborators: overcomplicated code, which "
                "deserves a refactoring before a test, because any test written now is large, slow and brittle; "
                "Encore's barcode issuance sits here. Bottom left, simple with few collaborators: trivial code such "
                "as getters and data classes, which deserves no tests, though that never covers glue where money "
                "or seats move. Bottom right, simple with many collaborators: controllers, which deserve a few "
                "integration tests of the wiring; Encore's resale purchase saga is mostly wiring and every link of "
                "it is integration-tested. An arrow shows Meszaros's Humble Object refactoring moving the decisions "
                "out of overcomplicated code into a plain testable object, leaving a thin shell behind with the "
                "controllers. A heuristic, not a measured result.")
    p = Plot(d, x=96, y=88, w=720, h=320, xr=(0, 2), yr=(0, 2))
    p.axes(xticks=[0.5, 1.5], yticks=[0.5, 1.5], grid=False,
           xlabel="NUMBER OF COLLABORATORS", ylabel="COMPLEXITY OR DOMAIN SIGNIFICANCE",
           xfmt=lambda t: "FEW" if t < 1 else "MANY", yfmt=lambda t: "LOW" if t < 1 else "HIGH")
    d.zones.append('<line class="dg-grid" x1="456" y1="88" x2="456" y2="408" stroke-dasharray="4 4"/>'
                   '<line class="dg-grid" x1="96" y1="248" x2="816" y2="248" stroke-dasharray="4 4"/>')
    d.path([(552, 104), (552, 64), (360, 64), (360, 104)], kind="accent",
           label="HUMBLE OBJECT: THE DECISIONS MOVE OUT", at=1)
    d.path([(736, 232), (736, 264)], dashed=True, label="A THIN SHELL STAYS", side="right")
    quads = [
        (112, 104, "UNIT-TEST THOROUGHLY", "Domain model and algorithms", "where the bugs that matter live",
         "Encore: the fee split, made a pure function", "backend"),
        (472, 104, "REFACTOR FIRST", "Overcomplicated code", "any test now: large, slow, brittle",
         "Encore: barcode issuance", "focal"),
        (112, 264, "NO TESTS", "Trivial code", "getters and data classes",
         "but not glue where money or seats move", "backend"),
        (472, 264, "A FEW INTEGRATION TESTS", "Controllers", "simple; tests check the wiring",
         "Encore: resale purchase saga, every link", "backend"),
    ]
    for x, y, tag, name, sub, note, kind in quads:
        d.node(x, y, 328, 128, name, sub, kind, tag=tag)
        d.note(x + 164, y + 108, note, anchor="middle")
    d.legend([("focal", "Refactor before testing"), ("arrow:accent", "Humble Object (Meszaros)"),
              ("arrow:muted:dashed", "The shell left behind is a controller")])
    return d
