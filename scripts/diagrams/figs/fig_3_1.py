"""Figure 3.1: Ariane 501, schematic: the inertial reference systems in flight, and the world the tests assumed."""
from dg import Diagram
from registry import figure


@figure
def fig_3_1():
    d = Diagram("fig-3-1", 864, 504, "Ariane 501: the flight and the test",
                "A schematic after the inquiry board's report, in two rows. The top row is the flight of 4 June "
                "1996. The Ariane 5 trajectory, which builds horizontal velocity much faster than Ariane 4's, feeds "
                "two inertial reference systems running identical software on the same inputs. Converting the "
                "horizontal bias from a 64-bit float to a 16-bit signed integer raised an operand error; the backup "
                "unit failed first and the active unit, SRI 2, one data cycle (72 ms) later, at about 36.7 seconds "
                "after main-engine ignition, so there was nothing to switch to. The active unit's diagnostic bit "
                "pattern reached the on-board computer, which read it as flight data and commanded full nozzle "
                "deflection; the launcher broke up and was destroyed near 4 km. The bottom row is the testing. "
                "The SRI specification left out the Ariane 5 trajectory by joint agreement; in 1992 the project "
                "decided to use simulated SRI outputs instead of the real units in closed-loop system simulation; "
                "so every test passed, faithful to a world that was gone. The board's recommendations 2 and 10 "
                "ask for as much real equipment as technically feasible and for trajectory data in specifications "
                "and test requirements.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'ARIANE 501 · SCHEMATIC, AFTER THE INQUIRY BOARD\'S REPORT</text>')
    # ---- in flight -----------------------------------------------------------------------
    d.zone(16, 52, 832, 196, "IN FLIGHT · 4 JUNE 1996 · H0 + 36.7 S")
    d.path([(184, 100), (232, 100)])
    d.path([(184, 172), (232, 172)])
    d.path([(416, 100), (550, 100), (550, 144)], dashed=True, label="NOTHING TO SWITCH TO", at=0)
    d.path([(416, 172), (468, 172)], kind="accent")
    d.path([(632, 172), (688, 172)])
    d.node(32, 72, 152, 128, "Ariane 5 trajectory", "fast horizontal velocity", "input")
    d.node(232, 72, 184, 56, "Backup SRI", "fails first: operand error")
    d.node(232, 144, 184, 56, "Active SRI (SRI 2)", "fails one cycle (72 ms) later")
    d.node(468, 144, 164, 56, "On-board computer", "reads it as flight data")
    d.node(688, 144, 144, 56, "Full deflection", "nozzles; break-up", "focal")
    d.note(232, 220, "same software, same inputs:")
    d.note(232, 234, "BH, 64-bit float → 16-bit int")
    d.note(468, 220, "diagnostic bit pattern")
    d.note(468, 234, "from the failed unit")
    d.note(688, 220, "destroyed near 4 km")
    d.note(688, 234, "about H0 + 39 s")
    d.note(32, 220, "never fed to the SRI")
    d.note(32, 234, "software in any test")
    # ---- in test -------------------------------------------------------------------------
    d.zone(16, 288, 832, 128, "IN TEST · THE WORLD THE SUITE ASSUMED")
    for a, b in ((184, 232), (416, 468), (632, 688)):
        d.path([(a, 336), (b, 336)])
    d.node(32, 308, 152, 56, "SRI specification", "no Ariane 5 trajectory", "input")
    d.node(232, 308, 184, 56, "Simulated SRI outputs", "real SRIs left out, 1992", "optional")
    d.node(468, 308, 164, 56, "System simulation", "closed loop", "backend")
    d.node(688, 308, 144, 56, "Every test passes", "a world that is gone")
    d.note(32, 384, "left out by joint")
    d.note(32, 398, "agreement")
    d.note(232, 384, "SRI reused from Ariane 4,")
    d.note(232, 398, "“practically the same”")
    d.note(468, 384, "no test fed the SRI the")
    d.note(468, 398, "trajectory it would fly")
    d.note(688, 384, "faithful, with rigor,")
    d.note(688, 398, "to Ariane 4's world")
    d.note(24, 444, "Board, recommendation 2: as much real equipment as technically feasible, closed loop."
                    "  Recommendation 10: trajectory data in specs and tests.")
    d.legend([("input", "The world fed in"), ("backend", "Real equipment"),
              ("optional", "Stand-in"), ("focal", "The failure"),
              ("arrow:accent", "Diagnostic bits, read as flight data")])
    return d
