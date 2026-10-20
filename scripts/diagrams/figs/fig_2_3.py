"""Figure 2.3: Encore's hotspot run on the purchase path, size against changes, one year of history."""
from chartkit import Plot
from dg import Diagram, label_width
from registry import figure

FILES = [  # rank, path, changes in 12 months, lines, share of changes by top author, label side
    (1, "ticketing/barcode/BarcodeIssuer.kt", 214, 3900, 88, "left"),
    (2, "orders/saga/PurchaseSaga.kt", 187, 2600, 21, "left"),
    (3, "ticketing/barcode/BarcodeFormats.kt", 131, 1450, 91, "left"),
    (4, "inventory/holds/HoldService.kt", 96, 1700, 34, "right"),
    (5, "orders/psp/PspRouter.kt", 88, 1100, 29, "below"),
]


@figure
def fig_2_3():
    d = Diagram("fig-2-3", 864, 384, "Hotspots on the purchase path",
                "A scatter chart of Encore's top five hotspots on the purchase path over twelve months, with size "
                "in lines across and number of changes up. 1: ticketing/barcode/BarcodeIssuer.kt, 214 changes, "
                "3,900 lines, 88% of changes by its top author. 2: orders/saga/PurchaseSaga.kt, 187 changes, "
                "2,600 lines, 21%. 3: ticketing/barcode/BarcodeFormats.kt, 131 changes, 1,450 lines, 91%. "
                "4: inventory/holds/HoldService.kt, 96 changes, 1,700 lines, 34%. 5: orders/psp/PspRouter.kt, "
                "88 changes, 1,100 lines, 29%. The two barcode files are highlighted: nearly all their changes "
                "come from one person, while the saga's are spread across many authors.")
    p = Plot(d, x=88, y=48, w=720, h=240, xr=(0, 4000), yr=(0, 250))
    p.axes(xticks=[0, 1000, 2000, 3000, 4000], yticks=[0, 50, 100, 150, 200, 250],
           xlabel="SIZE (LINES)", ylabel="CHANGES IN 12 MONTHS",
           xfmt=lambda v: f"{v:,}")
    for rank, path, changes, lines, share, side in FILES:
        barcode = path.startswith("ticketing/barcode")
        p.dot(lines, changes, kind="accent" if barcode else "ink", r=5 if barcode else 4)
        top = f"{rank} · {path}"
        bottom = f"{changes} CHANGES · {lines:,} LINES · TOP AUTHOR {share}%"
        if side == "left":
            w = max(label_width(top), label_width(bottom))
            p.annotate(lines, changes, top, dx=-10 - (w - label_width(top)), dy=-2, anchor="end")
            p.annotate(lines, changes, bottom, dx=-10 - (w - label_width(bottom)), dy=11, anchor="end")
        elif side == "below":
            p.annotate(lines, changes, top, dx=10, dy=20)
            p.annotate(lines, changes, bottom, dx=10, dy=33)
        else:
            p.annotate(lines, changes, top, dx=10, dy=-2)
            p.annotate(lines, changes, bottom, dx=10, dy=11)
    d.legend([("focal", "Barcode issuance: 88% and 91% of changes by one person"),
              ("backend", "Other purchase-path file")])
    return d
