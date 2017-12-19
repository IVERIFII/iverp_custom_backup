import frappe
# Implementation copied from erpnext.utilities.transaction_base
def validate_with_previous_doc(doc, ref):
    for key, val in ref.items():
        is_child = val.get("is_child_table")
        ref_doc = {}
        item_ref_dn = []
        for d in doc.get_all_children(doc.doctype + " Item"):
            ref_dn = d.get(val["ref_dn_field"])
            if ref_dn:
                if is_child:
                    doc.compare_values({key: [ref_dn]}, val["compare_fields"], d)
                    if ref_dn not in item_ref_dn:
                        item_ref_dn.append(ref_dn)
                    elif not val.get("allow_duplicate_prev_row_id"):
                        frappe.throw(_("Duplicate row {0} with same {1}").format(d.idx, key))
                elif ref_dn:
                    ref_doc.setdefault(key, [])
                    if ref_dn not in ref_doc[key]:
                        ref_doc[key].append(ref_dn)
        if ref_doc:
            doc.compare_values(ref_doc, val["compare_fields"])

def delivery_note_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Sales Order": {
            "ref_dn_field": "against_sales_order",
            "compare_fields": [["iverifii_doc_location", "="]]
        },
        "Sales Invoice": {
            "ref_dn_field": "against_sales_invoice",
            "compare_fields": [["iverifii_doc_location", "="]]
        }
    })

def sales_invoice_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Sales Order": {
            "ref_dn_field": "sales_order",
            "compare_fields": [["iverifii_doc_location", "="]]
        },
        "Delivery Note": {
            "ref_dn_field": "delivery_note",
            "compare_fields": [["iverifii_doc_location", "="]]
        }
	})

def sales_order_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Quotation": {
            "ref_dn_field": "prevdoc_docname",
            "compare_fields": [["iverifii_doc_location", "="]]
        }
    })

def purchase_invoice_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Purchase Order": {
            "ref_dn_field": "purchase_order",
            "compare_fields": [["iverifii_doc_location", "="]],
        },
        "Purchase Receipt": {
            "ref_dn_field": "purchase_receipt",
            "compare_fields": [["iverifii_doc_location", "="]],
        }
    })

def purchase_order_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Supplier Quotation": {
            "ref_dn_field": "supplier_quotation",
            "compare_fields": [["iverifii_doc_location", "="]]
        }
    })

def purchase_receipt_validate_with_previous_doc(doc, method):
    validate_with_previous_doc(doc, {
        "Purchase Order": {
            "ref_dn_field": "purchase_order",
            "compare_fields": [["iverifii_doc_location", "="]]
        }
    })


