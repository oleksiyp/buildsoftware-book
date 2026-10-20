"""Figure 7.1: Force.com's metadata-driven multitenancy, as the 2008 whitepaper describes it (schematic)."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_7_1():
    d = Diagram("fig-7-1", 864, 556, "Tenants that differ only in data",
                "A schematic of Salesforce's Force.com multitenant design as its 2008 whitepaper and the 2009 "
                "SIGMOD paper describe it, not a drawing of any real screen or table. At the top left, the "
                "universal data dictionary holds every tenant's objects, fields, forms, workflows and access rules "
                "as metadata. One shared runtime engine reads that metadata and generates each tenant's "
                "'virtual' application at runtime, so no real table is created and no code is compiled per "
                "tenant; governors cap the processor time, memory and queries any one tenant's code may use in "
                "a single execution. Below, all tenant data sits in one shared table: an OrgID column, then "
                "hundreds of generic variable-length flex columns, Value0 to Value500, onto which each tenant's "
                "custom fields are mapped, so Org A's first custom field and Org B's first custom field share the "
                "column Value0. An IsDeleted flag makes deletes soft, sending rows to a recycle bin. Indexes are "
                "kept in separate pivot tables, MT_Indexes, copied synchronously. The OrgID, highlighted, leads "
                "every index and partitions every table, and every query the engine runs is filtered by it. The "
                "organization names and field placements in the table are illustrative.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'FORCE.COM AS PUBLISHED IN 2008 · SCHEMATIC</text>')
    # ---- top: dictionary -> engine -> virtual applications ----------------------------------
    d.zone(24, 64, 248, 196, "METADATA · UNIVERSAL DATA DICTIONARY")
    for i, name in enumerate(["Objects", "Fields", "Forms", "Workflows", "Access rules"]):
        d.node(44, 80 + i * 36, 208, 28, name, None, "backend")
    d.path([(272, 164), (332, 164)], label="READ", side="above")
    d.node(332, 128, 200, 72, "Runtime engine", "one shared copy of the code", "focal")
    d.path([(532, 148), (560, 148), (560, 120), (592, 120)])
    d.path([(532, 180), (560, 180), (560, 204), (592, 204)])
    d.node(592, 92, 248, 56, "Org A's application", "virtual, generated at runtime", "input")
    d.node(592, 176, 248, 56, "Org B's application", "virtual, generated at runtime", "input")
    d.note(716, 252, "no real table created,", anchor="middle")
    d.note(716, 266, "no code compiled per tenant", anchor="middle")
    d.note(424, 236, "GOVERNORS: CPU, MEMORY,", anchor="end")
    d.note(424, 250, "QUERIES PER EXECUTION", anchor="end")
    # engine -> data
    d.path([(432, 200), (432, 340)], label="EVERY QUERY FILTERED BY ORGID", at=0, side="right")
    # ---- bottom: the one shared data table ---------------------------------------------------
    d.zone(24, 300, 816, 200, "DATA · ONE SHARED TABLE FOR EVERY TENANT")
    cols = [("OrgID", 48, 88), ("Value0", 136, 88), ("Value1", 224, 88), ("Value2", 312, 88),
            ("…", 400, 48), ("Value500", 448, 88), ("IsDeleted", 536, 88)]
    rows = [("Org A", ["A · field 1", "A · field 2", "", "", "", "0"]),
            ("Org A", ["A · field 1", "A · field 2", "", "", "", "0"]),
            ("Org B", ["B · field 1", "", "", "", "", "1"]),
            ("Org C", ["C · field 1", "C · field 2", "C · field 3", "", "", "0"])]
    TY, RH = 340, 24
    out = [f'<rect class="dg-ill-fill" x="48" y="{TY}" width="576" height="{RH}"/>']
    for r in range(len(rows)):
        out.append(f'<rect class="dg-ill-soft" x="48" y="{TY + RH * (r + 1)}" width="576" height="{RH}"/>')
    for name, x, w in cols[1:]:
        out.append(f'<line class="dg-ill-soft" x1="{x}" y1="{TY}" x2="{x}" y2="{TY + RH * 5}"/>')
    for name, x, w in cols:
        out.append(f'<text class="dg-sub" x="{x + w // 2}" y="{TY + 16}" style="font-weight:600">{escape(name)}</text>')
    for r, (org, cells) in enumerate(rows):
        y = TY + RH * (r + 1) + 16
        out.append(f'<text class="dg-sub" x="92" y="{y}">{org}</text>')
        for (name, x, w), c in zip(cols[1:], cells):
            if c:
                out.append(f'<text class="dg-sub" x="{x + w // 2}" y="{y}">{escape(c)}</text>')
    d.nodes.append("\n".join(out))
    # the tenant key: one accent element over the whole OrgID column
    d.nodes.append(f'<rect class="dg-ill-fill-accent" x="48" y="{TY}" width="88" height="{RH * 5}" rx="2"/>')
    d.path([(624, 376), (680, 376)])
    d.path([(624, 424), (680, 424)])
    d.node(680, 344, 144, 48, "MT_Indexes", "pivot tables, synced", "store")
    d.node(680, 400, 144, 48, "Recycle bin", "soft deletes", "store")
    d.note(48, 480, "OrgID leads every index and partitions every table · Value0 … Value500: variable-length "
           "flex columns")
    d.legend([("backend", "Metadata"), ("focal", "Shared engine; the tenant key"),
              ("input", "A tenant's virtual application"), ("store", "Supporting store")])
    return d
