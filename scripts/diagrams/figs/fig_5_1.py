"""Figure 5.1: Hopper's A-0 compiling routine, 1951–52, as a schematic of what it did."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_5_1():
    d = Diagram("fig-5-1", 864, 448, "A-0, the compiling routine",
                "Schematic, not a reproduction of any document. On the left, the mathematician's specification: "
                "a list of entries, each naming a subroutine by its call number, with its arguments. Below the "
                "centre, a catalogued library of subroutines. In the centre, the A-0 compiling routine on the "
                "UNIVAC I fetches the named subroutines from the library and adjusts their addresses so they fit "
                "together. On the right, the result: a complete machine-code program made of those subroutines, "
                "with duplicate data transfers between them, which is then run. Below it, a person removes the "
                "duplicate transfers by hand, as Hopper proposed in 1952: the machine generates, a person "
                "refines and owns the result.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'SCHEMATIC · A-0 ON THE UNIVAC I · 1951–52</text>')

    # ---- the specification sheet (left) --------------------------------------------------------
    SX, SY, SW, SH = 24, 72, 168, 200
    d.nodes.append(f'<path class="dg-ill-fill" d="M {SX},{SY} h {SW - 20} l 20,20 v {SH - 20} h -{SW} z"/>'
                   f'<path class="dg-ill-soft" d="M {SX + SW - 20},{SY} v 20 h 20"/>')
    d.extra.append(f'<text class="dg-eyebrow" x="{SX + 12}" y="{SY + 24}" style="text-anchor:start">SPECIFICATION</text>')
    for i in range(4):
        y = SY + 44 + i * 36
        d.extra.append(f'<rect class="dg-ill-soft" x="{SX + 12}" y="{y}" width="56" height="20" rx="2"/>'
                       f'<text class="dg-sub" x="{SX + 40}" y="{y + 13}">CALL NO.</text>'
                       f'<line class="dg-ill-soft" x1="{SX + 76}" y1="{y + 10}" x2="{SX + SW - 16}" y2="{y + 10}" '
                       f'stroke-dasharray="3 3"/>')
    d.note(SX + 76, SY + 40, "arguments")
    d.note(SX, SY + SH + 20, "written by the mathematician:")
    d.note(SX, SY + SH + 34, "subroutines named by call")
    d.note(SX, SY + SH + 48, "number, with their arguments")

    # ---- the library (below the centre) ----------------------------------------------------------
    LX, LY, LW, LH = 232, 304, 232, 72
    d.zone(LX, LY, LW, LH, "CATALOGUED LIBRARY")
    for i in range(6):
        x = LX + 16 + i * 34
        d.nodes.append(f'<rect class="dg-ill-fill" x="{x}" y="{LY + 20}" width="28" height="36" rx="2"/>'
                       f'<line class="dg-ill-soft" x1="{x + 6}" y1="{LY + 32}" x2="{x + 22}" y2="{LY + 32}"/>'
                       f'<line class="dg-ill-soft" x1="{x + 6}" y1="{LY + 40}" x2="{x + 18}" y2="{LY + 40}"/>')
    d.note(LX + LW // 2, LY + LH + 20, "routines once recopied by hand", anchor="middle")

    # ---- A-0 (centre) -----------------------------------------------------------------------------
    AX, AY, AW, AH = 248, 140, 200, 64
    d.path([(SX + SW, AY + 32), (AX, AY + 32)], label="READ", side="above")
    d.path([(AX + 176, LY + 20), (AX + 176, AY + AH)], label="FETCHED BY CALL NO.", side="left")
    d.node(AX, AY, AW, AH, "A-0 compiling routine", "fetch, adjust addresses", "focal", tag="UNIVAC I")

    # ---- the program (right) ----------------------------------------------------------------------
    PX, PY, PW, PH = 520, 72, 168, 200
    d.path([(AX + AW, AY + 32), (PX, AY + 32)], label="PRODUCES", side="above")
    d.nodes.append(f'<rect class="dg-ill-fill" x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="2"/>')
    d.extra.append(f'<text class="dg-eyebrow" x="{PX + 12}" y="{PY + 20}" style="text-anchor:start">'
                   'MACHINE-CODE PROGRAM</text>')
    blocks = [(PY + 32, 40), (PY + 92, 40), (PY + 152, 36)]
    for by, bh in blocks:
        d.extra.append(f'<rect class="dg-ill-soft" x="{PX + 12}" y="{by}" width="{PW - 24}" height="{bh}" rx="2"/>'
                       f'<text class="dg-sub" x="{PX + PW // 2}" y="{by + bh // 2 + 3}">subroutine</text>')
    # the duplicate data transfers between subroutines: one accent element
    dup = " ".join(f"M {PX + 40},{y} h {PW - 80} v 12 h -{PW - 80} z" for y in (PY + 76, PY + 136))
    d.extra.append(f'<path class="dg-ill-fill-accent" d="{dup}"/>')
    d.note(PX + PW + 12, PY + 148, "duplicate")
    d.note(PX + PW + 12, PY + 161, "data transfers")
    d.extra.append(f'<path class="dg-ill-soft" d="M {PX + PW - 40},{PY + 142} h 48"/>')

    # ---- run, and the hand refinement ------------------------------------------------------------
    RX, RY, RW, RH = 744, 140, 96, 64
    d.path([(PX + PW, AY + 32), (RX, AY + 32)], label="RUN", side="above")
    d.node(RX, RY, RW, RH, "Run", "on the UNIVAC", "backend")
    FX, FY, FW, FH = 520, 324, 168, 52
    d.path([(PX + PW // 2, FY), (PX + PW // 2, PY + PH)], dashed=True, label="BY HAND", side="right")
    d.node(FX, FY, FW, FH, "A person refines", "removes the duplication", "input")

    d.legend([("focal", "The compiling routine"), ("input", "A person's part"),
              ("arrow:muted", "The machine's path"), ("arrow:muted:dashed", "Refined by hand")])
    return d
