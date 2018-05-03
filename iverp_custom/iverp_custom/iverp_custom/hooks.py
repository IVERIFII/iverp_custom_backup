# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "iverifii_customizations"
app_title = "Iverifii Customizations"
app_publisher = "nchenbang@iverifii"
app_description = "Store all customizations on erpnext app by Iverifii"
app_icon = "fa fa-star"
app_color = "grey"
app_email = "ngo@iverifii.com"
app_license = "MIT"

fixtures = ["Custom Script"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iverifii_customizations/css/iverifii_customizations.css"
# app_include_js = "/assets/iverifii_customizations/js/iverifii_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/iverifii_customizations/css/iverifii_customizations.css"
# web_include_js = "/assets/iverifii_customizations/js/iverifii_customizations.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Delivery Note" : "public/js/delivery_note.js",
	"Payment Entry" : "public/js/payment_entry.js",
	"Quotation" : "public/js/quotation.js",
	"Sales Invoice " : "public/js/sales_invoice.js",
	"Sales Order" : "public/js/sales_order.js",
	"Purchase Invoice" : "public/js/purchase_invoice.js",
	"Purchase Order" : "public/js/purchase_order.js",
	"Purchase Receipt" : "public/js/purchase_receipt.js",
	"Supplier Quotation" : "public/js/supplier_quotation.js",
	"Journal Entry": "public/js/journal_entry.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "iverifii_customizations.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "iverifii_customizations.install.before_install"
# after_install = "iverifii_customizations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iverifii_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Delivery Note": {
		"validate": "iverifii_customizations.iverifii_hooks.validations.delivery_note_validate_with_previous_doc"
	},
	"Sales Invoice": {
		"before_submit": "iverifii_customizations.iverifii_hooks.autoname.sales_invoice_autoname",
		"before_insert": "iverifii_customizations.iverifii_hooks.autoname.before_insert",
		"validate": "iverifii_customizations.iverifii_hooks.validations.sales_invoice_validate_with_previous_doc"
	},
	"Sales Order": {
		"validate": "iverifii_customizations.iverifii_hooks.validations.sales_order_validate_with_previous_doc"
	},
	"Purchase Invoice": {
		"validate": "iverifii_customizations.iverifii_hooks.validations.purchase_invoice_validate_with_previous_doc"
	},
	"Purchase Order": {
		"validate": "iverifii_customizations.iverifii_hooks.validations.purchase_order_validate_with_previous_doc"
	},
	"Purchase Receipt": {
		"validate": "iverifii_customizations.iverifii_hooks.validations.purchase_receipt_validate_with_previous_doc"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"iverifii_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"iverifii_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"iverifii_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iverifii_customizations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"iverifii_customizations.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "iverifii_customizations.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iverifii_customizations.event.get_events"
# }

