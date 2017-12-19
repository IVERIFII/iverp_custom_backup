from frappe.model.naming import make_autoname
import frappe

def sales_invoice_autoname(doc, method):
    warehouse = frappe.get_doc("Warehouse", doc.iverifii_doc_location)
    doc.iverifii_location_running_number = make_autoname(doc.naming_series + warehouse.warehouse_name + '-.#####')

def before_insert(doc, method):
    print("before insert")
    print(doc.is_new() and doc.amended_from)

def before_cancel(doc, method):
    doc.iverifii_location_running_number = None