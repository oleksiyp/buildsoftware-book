"""Figure 4.4: encore-core's CI, step by step, before and after months five to eight."""
from html import escape

from chartkit import Plot
from dg import Diagram
from registry import figure

STEPS = [
    ("Check out and set up", 3, 1, ("Shallow clone; toolchain and dependencies", "prebuilt into the runner image")),
    ("Compile", 9, 3, ("Remote cache; most modules unchanged", "by any one change")),
    ("Unit and component tests", 14, 3, ("Run only the tests the module graph", "says a change can affect")),
    ("Static analysis", 3, 1, ("Analyze changed modules only",)),
    ("Package the artifact", 2, 1, ("Cached layers",)),
]


def text(d, x, y, s, cls, anchor="start"):
    d.extra.append(f'<text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anchor}">{escape(s)}</text>')


@figure
def fig_4_4():
    d = Diagram("fig-4-4", 864, 496, "encore-core's CI before and after",
                "Paired bars for each step of continuous integration on encore-core, in minutes, before and after "
                "the work of months five to eight. Check out and set up: 3 to 1, by a shallow clone with the "
                "toolchain and dependencies prebuilt into the runner image. Compile: 9 to 3, by a remote cache, "
                "since most modules are unchanged by any one change. Unit and component tests: 14 to 3, by running "
                "only the tests the module graph says a change can affect. Static analysis: 3 to 1, by analyzing "
                "changed modules only. Package the artifact: 2 to 1, by cached layers. Total, from push to "
                "verdict: 31 to 9 minutes. Test selection and the remote cache account for 17 of the 22 minutes "
                "saved. A dashed line marks about 6 minutes, the CI time of a golden-path service.")
    p = Plot(d, x=296, y=56, w=512, h=356, xr=(0, 32), yr=(0, 1))
    p.axes(xticks=[0, 5, 10, 15, 20, 25, 30], xlabel="MINUTES", grid=False, xfmt=lambda t: f"{t}")
    for t in (5, 10, 15, 20, 25, 30):
        xx = p.px(t)
        d.zones.append(f'<line class="dg-grid" x1="{xx:.1f}" y1="{p.y}" x2="{xx:.1f}" y2="{p.y + p.h}"/>')
    text(d, 24, 40, "STEP IN ENCORE-CORE’S CI · WHAT CHANGED", "dg-eyebrow")
    text(d, 296, 40, "BEFORE AND AFTER, MINUTES", "dg-eyebrow")

    RH = 60
    x0 = p.px(0)

    def bars(y, before, after, accent=False):
        wb, wa = p.px(before) - x0, p.px(after) - x0
        d.nodes.append(f'<rect class="dg-n dg-n-input" x="{x0}" y="{y}" width="{wb:.1f}" height="14" rx="2"/>')
        d.extra.append(f'<text class="dg-tick" x="{x0 + wb + 6:.1f}" y="{y + 10}">{before}</text>')
        cls = "dg-ill-fill-accent" if accent else "dg-dot dg-dot-ink"
        d.nodes.append(f'<rect class="{cls}" x="{x0}" y="{y + 18}" width="{wa:.1f}" height="14" rx="2"/>')
        tcls = "dg-label dg-l-accent" if accent else "dg-tick"
        d.extra.append(f'<text class="{tcls}" x="{x0 + wa + 6:.1f}" y="{y + 28}" style="text-anchor:start;'
                       f'font-size:8.5px">{after}</text>')

    for i, (name, before, after, what) in enumerate(STEPS):
        y = 64 + i * RH
        text(d, 24, y + 10, name, "dg-name")
        for k, line in enumerate(what):
            text(d, 24, y + 25 + k * 12, line, "dg-note")
        bars(y, before, after)
    # total
    y = 64 + len(STEPS) * RH + 8
    d.zones.append(f'<line class="dg-rule" x1="24" y1="{y - 12}" x2="840" y2="{y - 12}"/>')
    text(d, 24, y + 10, "Total, push to verdict", "dg-name")
    text(d, 24, y + 25, "Golden-path service: about 6", "dg-note")
    bars(y, 31, 9, accent=True)
    gp = p.px(6)
    d.zones.append(f'<line class="dg-series dg-s-soft" x1="{gp:.1f}" y1="{y - 6}" x2="{gp:.1f}" y2="{y + 38}" '
                   f'stroke-dasharray="5 4"/>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="{p.px(9) + 28:.1f}" y="{y + 28}" '
                   'style="text-anchor:start;font-size:8.5px">17 OF 22 MINUTES SAVED: TEST SELECTION '
                   '+ REMOTE CACHE</text>')

    # manual legend in the book's strip style
    ly = d.h - 28
    lg = [f'<line class="dg-rule" x1="24" y1="{ly - 12}" x2="{d.w - 24}" y2="{ly - 12}"/>',
          f'<rect class="dg-n dg-n-input" x="24" y="{ly - 1}" width="16" height="10" rx="2"/>',
          f'<text class="dg-legend" x="46" y="{ly + 7}">Before</text>',
          f'<rect class="dg-dot dg-dot-ink" x="176" y="{ly - 1}" width="16" height="10" rx="2"/>',
          f'<text class="dg-legend" x="198" y="{ly + 7}">After months five to eight</text>',
          f'<line class="dg-series dg-s-soft" x1="380" y1="{ly + 4}" x2="404" y2="{ly + 4}" stroke-dasharray="5 4"/>',
          f'<text class="dg-legend" x="412" y="{ly + 7}">Golden-path CI, about 6 minutes</text>']
    d.extra.append("\n".join(lg))
    return d
