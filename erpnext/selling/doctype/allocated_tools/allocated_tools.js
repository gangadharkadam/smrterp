



cur_frm.add_fetch('employee', 'employee_name', 'employee_name');


cur_frm.cscript.refresh = function(doc,cdt,cdn){
	console.log(" in the js");

}




// cur_frm.cscript.emp_code = function(doc, cdt, cdn) {
// 	var d = locals[cdt][cdn];
// 	if (d.item_code) {
// 		return get_server_fields('get_employee_details', d.emp_code,
// 			'tools_information', doc, cdt, cdn, 1);
// 	}
// }