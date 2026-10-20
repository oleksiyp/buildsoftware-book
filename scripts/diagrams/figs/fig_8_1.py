"""Figure 8.1: the four-party card system under NBI, with the network's default fee, and the road to Visa."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_8_1():
    d = Diagram("fig-8-1", 864, 576, "The four-party system and its default fee",
                "Schematic. Top: the four-party system the Eleventh Circuit described. A cardholder buys with "
                "the card from a merchant; the bank that issued the card issued it to the cardholder; the merchant "
                "passes the charge to its own bank, the merchant's bank. Inside National BankAmericard Inc. (NBI), "
                "formed in 1970 and owned by its member banks, who went on competing for cardholders and merchants, "
                "the charge clears from the merchant's bank through NBI to the issuing bank. From late 1971 the "
                "merchant's bank pays the issuer a uniform fee set by the network on every transaction that clears "
                "through NBI, to carry part of the issuer's costs: credit losses, the interest-free period and the "
                "absence of a cardholder fee. The fee is a default: two banks could bypass the network's clearing "
                "and negotiate another rate privately. Bottom: a timeline of events in order, not to scale. 1958, "
                "BankAmericard launched in California. 1966, licensed to banks across the United States. 1968, "
                "Columbus, Ohio meeting; Hock heads a committee. 1969, Sausalito design meetings. 1970, NBI formed "
                "with Hock as president. Late 1971, the uniform interchange fee. 1973, VisaNet. 1976, renamed Visa. "
                "1984, Hock resigns and the district court finds for Visa in NaBanco's suit. 1986, the Eleventh "
                "Circuit affirms.")
    # ---- the four parties ----------------------------------------------------------------------
    d.zone(24, 136, 816, 192, "THE NETWORK (1970)")
    d.path([(224, 64), (640, 64)], label="BUYS WITH THE CARD")
    d.path([(176, 160), (176, 88)], label="ISSUES THE CARD", side="right")
    d.path([(728, 88), (728, 160)], label="THE CHARGE", side="left")
    d.path([(640, 184), (520, 184)], label="CLEARS")
    d.path([(344, 184), (224, 184)], label="CLEARS")
    d.path([(728, 208), (728, 256), (136, 256), (136, 208)], kind="accent", at=1,
           label="UNIFORM FEE, SET BY THE NETWORK (LATE 1971)")
    d.path([(784, 208), (784, 304), (80, 304), (80, 208)], dashed=True, at=1,
           label="OR A RATE THE TWO BANKS NEGOTIATE PRIVATELY")
    d.node(48, 40, 176, 48, "Cardholder", "pays no card fee", "input")
    d.node(640, 40, 176, 48, "Merchant", None, "input")
    d.node(48, 160, 176, 48, "Issuing bank", "issued the card")
    d.node(344, 160, 176, 48, "NBI", "shared rules · clearing", "store")
    d.node(640, 160, 176, 48, "Merchant's bank", "serves the merchant")
    d.note(432, 352, "NBI WAS OWNED BY ITS MEMBER BANKS, WHO WENT ON COMPETING FOR CARDHOLDERS AND MERCHANTS.",
           anchor="middle")
    d.note(432, 366, "THE FEE CARRIED PART OF THE ISSUER'S COSTS: CREDIT LOSSES, THE INTEREST-FREE PERIOD,",
           anchor="middle")
    d.note(432, 380, "AND NO FEE FROM THE CARDHOLDER. A DEFAULT, SO NOBODY HAD TO NEGOTIATE.", anchor="middle")
    # ---- the timeline --------------------------------------------------------------------------
    d.note(24, 404, "HOW THE LICENSEES BECAME A NETWORK · EVENTS IN ORDER, NOT TO SCALE")
    events = [("1958", "BANKAMERICARD", "IN CALIFORNIA"), ("1966", "LICENSED ACROSS", "THE U.S."),
              ("1968", "COLUMBUS:", "HOCK'S COMMITTEE"), ("1969", "SAUSALITO", "DESIGN MEETINGS"),
              ("1970", "NBI FORMED,", "HOCK PRESIDENT"), ("1971", "UNIFORM", "INTERCHANGE FEE"),
              ("1973", "VISANET", None), ("1976", "RENAMED VISA", None),
              ("1984", "HOCK RESIGNS;", "COURT FOR VISA"), ("1986", "ELEVENTH CIRCUIT", "AFFIRMS")]
    LY, X0, STEP = 468, 108, 72
    d.zones.append(f'<line class="dg-ill-soft" x1="48" y1="{LY}" x2="816" y2="{LY}"/>')
    for i, (year, t1, t2) in enumerate(events):
        x = X0 + i * STEP
        hot = year == "1971"
        if hot:
            d.nodes.append(f'<circle class="dg-dot dg-dot-accent" cx="{x}" cy="{LY}" r="5"/>')
        else:
            d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{x}" cy="{LY}" r="3.5"/>')
        above = i % 2 == 0
        lines = [t for t in (t1, t2) if t]
        if above:
            yy, ys = 452, [436 - 13 * (len(lines) - 1 - k) for k in range(len(lines))]
        else:
            yy, ys = 492, [506 + 13 * k for k in range(len(lines))]
        d.extra.append(f'<text class="dg-name" x="{x}" y="{yy}">{year}</text>')
        for t, ty in zip(lines, ys):
            d.note(x, ty, t, anchor="middle")
    d.legend([("arrow:muted", "The card and its charge"), ("arrow:accent", "Network-set default fee"),
              ("arrow:muted:dashed", "Private bilateral rate"), ("store", "The network")])
    return d
