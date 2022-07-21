from __future__ import unicode_literals
import frappe
import erpnext
from frappe.utils import flt, nowdate, add_days, cint
from frappe import _

def sample_todo():
    print("here")
    t = frappe.new_doc("ToDo")
    t.description = "This is totdo"
    t.save(ignore_permissions=True)
    frappe.db.commit()