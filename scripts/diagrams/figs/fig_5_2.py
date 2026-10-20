"""Figure 5.2: what developers believed against what was measured, in Peng et al. and METR 2025."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_5_2():
    d = Diagram("fig-5-2", 864, 320, "Belief against measurement",
                "Two randomized trials, each plotted on one row, on a scale of how much faster developers were "
                "with AI, from 30% slower to 60% faster. Peng and colleagues, 2023, 95 freelance developers on "
                "one JavaScript task: participants guessed a gain of about 35%; the measured gain was 55.8% "
                "faster (71.17 against 160.89 minutes), so they underestimated it. METR, 2025, 16 experienced "
                "maintainers on 246 issues in their own repositories: before starting they expected a 24% "
                "speedup, afterward they believed they had been 20% faster, and the measured result was 19% "
                "slower, a gap of about 40 percentage points in the opposite direction.")
    p = Plot(d, x=240, y=56, w=576, h=176, xr=(-30, 60), yr=(0, 3))
    p.axes(xticks=[-30, -15, 0, 15, 30, 45, 60], yticks=[], grid=False,
           xlabel="FASTER WITH AI (%) · NEGATIVE = SLOWER", xfmt=lambda v: f"{v:+d}%" if v else "0")
    p.vline(0, kind="soft", dashed=True)
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'TWO RANDOMIZED TRIALS · WHAT DEVELOPERS BELIEVED, AND WHAT WAS MEASURED</text>')

    # Peng et al., 2023
    yp = 2.2
    p.line([(35, yp), (55.8, yp)], kind="soft")
    p.dot(35, yp, kind="ink", r=4)
    p.annotate(35, yp, "GUESSED ≈ 35%", dx=-8, dy=-10, anchor="end")
    p.dot(55.8, yp, kind="accent", r=5)
    p.annotate(55.8, yp, "MEASURED 55.8%", dx=-8, dy=20, kind="accent", anchor="end")
    d.note(24, int(p.py(yp)) - 2, "Peng et al., 2023")
    d.note(24, int(p.py(yp)) + 12, "95 freelancers · one task")

    # METR, 2025
    ym = 0.9
    p.line([(-19, ym), (24, ym)], kind="soft")
    p.dot(24, ym, kind="ink", r=4)
    p.annotate(24, ym, "EXPECTED +24%", dx=8, dy=-10)
    p.dot(20, ym, kind="ink", r=4)
    p.annotate(20, ym, "BELIEVED +20%", dx=8, dy=20)
    p.dot(-19, ym, kind="accent", r=5)
    p.annotate(-19, ym, "MEASURED 19% SLOWER", dx=-12, dy=20, kind="accent")
    d.note(24, int(p.py(ym)) - 2, "METR, 2025")
    d.note(24, int(p.py(ym)) + 12, "16 maintainers · 246 issues")

    d.legend([("input", "What developers expected or believed"), ("focal", "What the trial measured")])
    return d
