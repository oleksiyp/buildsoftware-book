"""Figure 8.5: contribution margin per resold €60 ticket, as two waterfalls (partner channel, Encore's app)."""
from html import escape

from dg import Diagram
from registry import figure

ROWS = [  # label, through a partner, in Encore's app, kind (add | sub | total | margin)
    ("BUYER'S SERVICE FEE (10%)", 6.00, 6.00, "add"),
    ("PARTNER COMMISSION (4 POINTS)", -2.40, None, "sub"),
    ("ORGANIZER SHARE (3 POINTS)", -1.80, -1.80, "sub"),
    ("ENCORE'S RETAINED FEE", 1.80, 4.20, "total"),
    ("PSP FEES ON THE €66 PAYMENT", -0.85, -0.85, "sub"),
    ("VARIABLE PLATFORM COST", -0.12, -0.12, "sub"),
    ("FRAUD LOSSES (AVERAGE)", -0.15, -0.15, "sub"),
    ("SUPPORT: 2% DISPUTED × €15", -0.30, -0.30, "sub"),
    ("CONTRIBUTION MARGIN", 0.38, 2.78, "margin"),
]


def eur(v, sign=True):
    s = f"€{abs(v):.2f}"
    return ("−" + s if v < 0 else "+" + s) if sign else s


@figure
def fig_8_5():
    d = Diagram("fig-8-5", 864, 472, "Contribution margin per resold ticket",
                "Two waterfalls for one resold €60 ticket, through a partner and in Encore's own app, using "
                "Encore's averages at the month-18 review. Through a partner: the buyer's 10% service fee is "
                "€6.00; the partner's 4 points, €2.40, and the organizer's 3 points, €1.80, are paid out, leaving "
                "Encore's retained fee of €1.80; then PSP fees on the €66 payment, €0.85, variable platform cost, "
                "€0.12, average fraud losses, €0.15, and support, €0.30 (2% of resales disputed at €15 each), "
                "leave a contribution margin of €0.38. In Encore's app there is no partner commission, so Encore "
                "retains €4.20 and, after the same costs, keeps a margin of €2.78, about seven times as much. Each "
                "additional point of dispute rate costs €0.15, so a dispute rate of about 4.5% would wipe out the "
                "partner-channel margin.")
    LX, Y0, STEP, BH, S = 24, 72, 32, 16, 36  # S: px per euro
    panels = [(256, "THROUGH A PARTNER"), (560, "IN ENCORE'S APP")]
    d.note(LX, 40, "PER RESOLD €60 TICKET · ENCORE'S AVERAGES AT THE MONTH-18 REVIEW")
    for x0, head in panels:
        d.note(x0 + 108, 60, head, anchor="middle")
    bottom = Y0 + len(ROWS) * STEP - 8
    for col, (x0, _) in enumerate(panels):
        # axis and euro ticks
        d.zones.append(f'<line class="dg-axis" x1="{x0}" y1="{Y0 - 8}" x2="{x0}" y2="{bottom}"/>')
        for e in range(0, 7):
            xx = x0 + e * S
            if e:
                d.zones.append(f'<line class="dg-grid" x1="{xx}" y1="{Y0 - 8}" x2="{xx}" y2="{bottom}"/>')
            d.zones.append(f'<text class="dg-tick" x="{xx}" y="{bottom + 14}" text-anchor="middle">€{e}</text>')
        run, prev_end = 0.0, None
        for r, (label, a, b, kind) in enumerate(ROWS):
            v = (a, b)[col]
            y = Y0 + r * STEP
            if v is None:
                d.note(x0 + 8, y + 12, "NONE: ENCORE KEEPS THE 4 POINTS")
                continue
            if kind == "add":
                lo, hi, run = 0.0, v, v
            elif kind == "sub":
                lo, hi = run + v, run
                run += v
            else:
                lo, hi = 0.0, v
                assert abs(v - run) < 0.005, (label, v, run)
            bx, bw = x0 + lo * S, (hi - lo) * S
            if prev_end is not None:  # connector from the previous bar's end
                d.zones.append(f'<line class="dg-grid" x1="{prev_end:.1f}" y1="{y - STEP + BH}" '
                               f'x2="{prev_end:.1f}" y2="{y}" stroke-dasharray="2 2"/>')
            cls = {"add": "dg-n dg-n-backend", "total": "dg-n dg-n-backend",
                   "sub": "dg-n dg-n-optional", "margin": "dg-ill-fill-accent"}[kind]
            dash = ' stroke-dasharray="4,3"' if kind == "sub" else ""
            d.nodes.append(f'<rect class="{cls}" x="{bx:.1f}" y="{y}" width="{bw:.1f}" height="{BH}" rx="2"{dash}/>')
            txt = eur(v, sign=kind in ("add", "sub"))
            tcls = "dg-label dg-l-accent" if kind == "margin" else "dg-label"
            d.extra.append(f'<text class="{tcls}" x="{x0 + hi * S + 6:.1f}" y="{y + 12}" '
                           f'style="text-anchor:start">{escape(txt)}</text>')
            prev_end = x0 + (run if kind != "margin" else v) * S
            if kind == "sub":
                prev_end = x0 + run * S
    for r, (label, *_rest, kind) in enumerate(ROWS):
        y = Y0 + r * STEP
        if kind in ("total", "margin"):
            d.extra.append(f'<text class="dg-name" x="{LX}" y="{y + 12}" style="text-anchor:start;font-size:11px">'
                           f'{escape(label.capitalize().replace("Encore", "Encore").replace("encore", "Encore"))}</text>')
        else:
            d.note(LX, y + 12, label)
    ny = bottom + 40
    d.note(256, ny, "EACH +1 POINT OF DISPUTE RATE COSTS €0.15;")
    d.note(256, ny + 14, "AT ABOUT 4.5% DISPUTES THE MARGIN IS GONE")
    d.note(560, ny, "SEVEN TIMES THE PARTNER-CHANNEL MARGIN;")
    d.note(560, ny + 14, "EVERY CHANNEL GETS THE SAME LISTINGS IN ORDER")
    d.legend([("backend", "Fee and Encore's subtotal"), ("optional", "Share paid out or cost"),
              ("focal", "Contribution margin")])
    return d
