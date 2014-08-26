# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
STANDARD_USERS = ("Guest", "Administrator")

class EmailTemplate(Document):

	def send(self):
		frappe.errprint("in the send")
		frappe.errprint(self.get('customer_information'))
		customer=[]
		for d in self.get('customer_information'):
			frappe.errprint(d)
			customer.append(d.customer_email)
		frappe.errprint(customer)

		from frappe.utils.user import get_user_fullname
		from frappe.utils import get_url
		# mail_titles = frappe.get_hooks().get("login_mail_title", [])
		# title = frappe.db.get_default('company') or (mail_titles and mail_titles[0]) or ""

		# full_name = get_user_fullname(frappe.session['user'])
		# if full_name == "Guest":
		# 	full_name = "Administrator"


		# message = frappe.db.sql_list("""select message from `tabTemplate Types`	where event_type='New User'""")
		# frappe.errprint(message[0])
		# frappe.errprint(message[0].format(self.first_name or self.last_name or "user",link,self.name,full_name))

		sender = frappe.session.user not in STANDARD_USERS and frappe.session.user or None
		frappe.sendmail(recipients=customer, sender=sender, subject=self.subject,
			message=self.message)		



	 
# @frappe.whitelist()
# def get_data(from_date=None,to_date=None,currency=None):
# 	frappe.errprint(currency)
# 	# data_dict = {'cols':'name ,net_total', 'tab':'`tabSales Order`', 'cond_col': 'delivery_date','cncy':'currency'}
# 	data_dict = {'cols':'name ,net_total', 'tab':'`tabSales Order`', 'cond_col': 'delivery_date'}
# 	make_cond(data_dict, from_date, to_date)				
# 	return{
# 		"sales_order_total": make_query(data_dict)