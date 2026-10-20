"""Figure 11.4: Y2K windowing (Thomas's example, pivot 20) beside Encore's own pivot year, INV-DEBT-031."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_11_4():
    d = Diagram("fig-11-4", 864, 440, "Two pivot years",
                "Schematic in two parts. Top, Y2K windowing in the example Martyn Thomas gives: a year stored as two "
                "digits, 00 to 99, is read through a pivot at 20. Stored years 00 to 19 are read as 2000 to 2019, "
                "and 20 to 99 as 1920 to 1999, so the stored order and the century order no longer match. Cheaper "
                "than expanding to four digits and simpler to test, it was not a permanent solution: the pivot "
                "year is its built-in trigger. Bottom, Encore's pivot year on a month scale from 0 to 30. The "
                "partner API accepts old-format references from the notice in month 2 until month 14, twelve "
                "months' notice. INV-DEBT-031 is entered in the debt register in month 6. From launch in month 12, "
                "old-format tickets (identity derived from order and seat) are still accepted, so every gate "
                "validator and the issuer carry two paths; the engineering review at month 24 finds the debt still "
                "open, as planned. The trigger is the day after the last event holding an old-format ticket, "
                "month 29, when both old paths and their replay tests are deleted in one change.")
    tx = lambda x, y, t, cls="dg-eyebrow", a="start": d.extra.append(  # noqa: E731
        f'<text class="{cls}" x="{x}" y="{y}" style="text-anchor:{a}">{escape(t)}</text>')
    # ---- top: windowing ------------------------------------------------------------------
    d.zone(24, 40, 816, 152, "Y2K WINDOWING · THOMAS'S EXAMPLE · SCHEMATIC")
    X0, X1 = 160, 800
    W = X1 - X0
    px = lambda v: X0 + int(round(v * W / 100 / 4)) * 4  # noqa: E731  two-digit value 0..100
    piv = px(20)
    tx(40, 92, "STORED", "dg-label", "start")
    tx(40, 104, "two digits", "dg-note", "start")
    tx(40, 156, "READ AS", "dg-label", "start")
    tx(40, 168, "through the pivot", "dg-note", "start")
    # stored bar: 00-19 shaded, 20-99 plain
    d.nodes.append(f'<rect class="dg-n dg-n-input" x="{X0}" y="80" width="{piv - X0}" height="28" rx="4"/>')
    d.nodes.append(f'<rect class="dg-n dg-n-backend" x="{piv}" y="80" width="{X1 - piv}" height="28" rx="4"/>')
    tx((X0 + piv) // 2, 98, "00 – 19", "dg-name", "middle")
    tx((piv + X1) // 2, 98, "20 – 99", "dg-name", "middle")
    # read-as bar: 1920-1999 plain (left 80%), 2000-2019 shaded (right 20%)
    split = px(80)
    d.nodes.append(f'<rect class="dg-n dg-n-backend" x="{X0}" y="144" width="{split - X0}" height="28" rx="4"/>')
    d.nodes.append(f'<rect class="dg-n dg-n-input" x="{split}" y="144" width="{X1 - split}" height="28" rx="4"/>')
    tx((X0 + split) // 2, 162, "1920 – 1999", "dg-name", "middle")
    tx((split + X1) // 2, 162, "2000 – 2019", "dg-name", "middle")
    # pivot marker (accent 1)
    d.nodes.append(f'<line class="dg-ill-accent" x1="{piv}" y1="68" x2="{piv}" y2="120"/>')
    d.label_at("PIVOT 20", piv, 68, horizontal=True, side="above", kind="accent")
    tx(X1, 132, "not a permanent solution: the pivot year is the trigger", "dg-note", "end")
    # ---- bottom: Encore ------------------------------------------------------------------
    d.zone(24, 224, 816, 196, "ENCORE'S PIVOT YEAR · INV-DEBT-031 · MONTHS")
    M0, M1 = 160, 800
    mx = lambda m: M0 + int(round(m * (M1 - M0) / 30 / 4)) * 4  # noqa: E731
    AY = 380
    ax = [f'<line class="dg-axis" x1="{M0}" y1="{AY}" x2="{M1}" y2="{AY}"/>']
    for m in range(0, 31, 2):
        ax.append(f'<line class="dg-axis" x1="{mx(m)}" y1="{AY}" x2="{mx(m)}" y2="{AY + 4}"/>')
        ax.append(f'<text class="dg-tick" x="{mx(m)}" y="{AY + 16}" text-anchor="middle">{m}</text>')
    d.zones.append("\n".join(ax))
    rows = [(256, "Partner API", "old format accepted"), (300, "Gates + issuer", "two paths, old and new")]
    for y, name, sub in rows:
        d.extra.append(f'<text class="dg-name" x="40" y="{y + 12}" style="text-anchor:start">{escape(name)}</text>')
        d.note(40, y + 24, sub)
    d.node(mx(2), 256, mx(14) - mx(2), 28, "12 months' notice", None, "input")
    d.node(mx(12), 300, mx(29) - mx(12), 28, "Old-format tickets still accepted", None, "input")
    # markers on the axis
    for m, lab in [(6, "DEBT ENTERED"), (12, "LAUNCH"), (24, "REVIEW")]:
        d.zones.append(f'<line class="dg-ill-soft" x1="{mx(m)}" y1="336" x2="{mx(m)}" y2="{AY}"/>')
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{mx(m)}" cy="{AY}" r="3.5"/>')
        d.label_at(lab, mx(m), 356, horizontal=True, side="below")
    # trigger (accent 2)
    d.nodes.append(f'<line class="dg-ill-accent" x1="{mx(29)}" y1="288" x2="{mx(29)}" y2="{AY}"/>')
    d.label_at("TRIGGER · MONTH 29", mx(29) - 52, 344, horizontal=True, side="below", kind="accent")
    return d
