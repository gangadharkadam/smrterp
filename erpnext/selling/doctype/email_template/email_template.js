cur_frm.add_fetch('plan', 'subject', 'subject');
cur_frm.add_fetch('plan', 'message', 'message');


// console.log("in the js");

// cur_frm.cscript.send = function(doc, cdt, cdn) {
// 	console.log("in the send")
// 	console.log()
// 	var d = locals[cdt][cdn];
// 	if (d.item_code) {
// 		return get_server_fields('get_item_details', d.item_code,
// 			'enquiry_details', doc, cdt, cdn, 1);
// 	}
// }



// cur_frm.cscript.master_type = function(doc, cdt, cdn) {
// 	cur_frm.toggle_display(['credit_days', 'credit_limit'], in_list(['Customer', 'Supplier'],
// 		doc.master_type));

// 	cur_frm.toggle_display('master_name', doc.account_type=='Warehouse' ||
// 		in_list(['Customer', 'Supplier'], doc.master_type));
// }