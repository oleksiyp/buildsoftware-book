"""Figure 1.3: the six commonest answers in Encore's developer survey, as bars, with the chapter for each."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_1_3():
    d = Diagram("fig-1-3", 864, 412, "What slows Encore's engineers",
                "Horizontal bars give the share of engineers naming each answer in their top three, in Encore's "
                "latest quarterly survey, which about 68% answered. Waiting for CI on the shared repository, 54%, "
                "Chapter 4. Waiting for review, especially from other teams, 46%, Chapters 4 and 10. Flaky "
                "end-to-end tests that fail for no reason anyone can find, 39%, Chapter 3. Fear of changing old "
                "code nobody fully understands, 31%, Chapter 2, highlighted because Verified Resale must change "
                "the oldest code. Building plumbing the platform should provide, such as partner webhooks, 24%, "
                "Chapter 6. New engineers taking about a quarter to make a meaningful change, 21%, Chapter 9.")
    rows = [("Waiting for CI", "on the shared repository", 54, "CHAPTER 4"),
            ("Waiting for review", "especially from other teams", 46, "CHAPTERS 4 AND 10"),
            ("Flaky end-to-end tests", "that fail for no reason anyone can find", 39, "CHAPTER 3"),
            ("Fear of changing old code", "nobody fully understands", 31, "CHAPTER 2"),
            ("Building plumbing", "the platform should provide, like webhooks", 24, "CHAPTER 6"),
            ("New engineers' first change", "about a quarter to make a meaningful one", 21, "CHAPTER 9")]
    BX, BW, Y0, RH = 312, 400, 64, 44   # bar origin, px for 60%, first row, row pitch
    px = lambda v: BX + v / 60 * BW      # noqa: E731
    AY = Y0 + len(rows) * RH + 4
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'ENCORE DEVELOPER SURVEY · LATEST QUARTER · ABOUT 68% ANSWERED</text>')
    d.extra.append('<text class="dg-eyebrow" x="840" y="36" style="text-anchor:end">WHERE THE BOOK TAKES IT UP</text>')
    for t in (0, 20, 40, 60):
        x = px(t)
        if t:
            d.zones.append(f'<line class="dg-grid" x1="{x:g}" y1="{Y0 - 12}" x2="{x:g}" y2="{AY}"/>')
        d.zones.append(f'<line class="dg-axis" x1="{x:g}" y1="{AY}" x2="{x:g}" y2="{AY + 4}"/>')
        d.extra.append(f'<text class="dg-tick" x="{x:g}" y="{AY + 16}" text-anchor="middle">{t}%</text>')
    d.zones.append(f'<line class="dg-axis" x1="{BX}" y1="{AY}" x2="{px(60):g}" y2="{AY}"/>')
    d.zones.append(f'<line class="dg-axis" x1="{BX}" y1="{Y0 - 12}" x2="{BX}" y2="{AY}"/>')
    d.extra.append(f'<text class="dg-axis-label" x="{px(60):g}" y="{AY + 32}" text-anchor="end">'
                   'SHARE NAMING IT IN THEIR TOP THREE</text>')
    for i, (name, sub, v, ch) in enumerate(rows):
        y = Y0 + i * RH
        acc = i == 3
        cls = "dg-ill-fill-accent" if acc else "dg-ill-fill"
        d.nodes.append(f'<rect class="{cls}" x="{BX}" y="{y}" width="{px(v) - BX:g}" height="24" rx="2"/>')
        d.extra.append(f'<text class="dg-name" x="24" y="{y + 10}" style="text-anchor:start">{escape(name)}</text>')
        d.extra.append(f'<text class="dg-sub" x="24" y="{y + 24}" style="text-anchor:start">{escape(sub)}</text>')
        lc = "dg-label dg-l-accent" if acc else "dg-label"
        d.extra.append(f'<text class="{lc}" x="{px(v) + 8:g}" y="{y + 15}" style="text-anchor:start;font-size:10px">'
                       f'{v}%</text>')
        d.extra.append(f'<text class="dg-label" x="840" y="{y + 15}" style="text-anchor:end">{ch}</text>')
    d.legend([("backend", "Share naming the answer"),
              ("focal", "The pain Verified Resale meets first: old code")])
    return d
