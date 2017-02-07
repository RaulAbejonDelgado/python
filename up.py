import xmlrpclib
import csv


url = 'http://localhost:8069'
username= "admin"
password = "pass"
db ="contable_demo"

sock_common =xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = sock_common.login(db,username,password)

sock = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))



#res users
reader = csv.reader(open('/home/drohne/odoo-dev/cargar_csvxmlrpc/1_res_users.csv','rb'))
for row in reader:
	print row[0:3]
	res_users= {
		'name':row[0],
		'login'	:row[1],
		'email':row[2],}
	
	user_id=sock.execute_kw(db, uid, password,'res.users', 'create',[res_users])
	

reader = csv.reader(open('/home/drohne/odoo-dev/cargar_csvxmlrpc/2_account_account.csv','rb'))
#account_account
for row in reader:
	print row[0:7]
	
	ids = sock.execute_kw(db, uid, password,'account.account.type', 'search',[[['code', '=', 'view']]],{'limit': 1})
	
	account_account={
		'active':row[0].decode('windows-1252').encode('utf-8'),
		'exchange_rate':row[1].decode('windows-1252').encode('utf-8'),
		'code':row[2].decode('windows-1252').encode('utf-8'),
		'name':row[3].decode('windows-1252').encode('utf-8'),
		'reconcile':row[4].decode('windows-1252').encode('utf-8'),
		'currency_mode':row[5].decode('windows-1252').encode('utf-8'),
		'user_type':int(ids[0]),}
		
		
	user_id=sock.execute_kw(db, uid, password,'account.account', 'create',[account_account])
	
#res partner
reader = csv.reader(open('/home/drohne/odoo-dev/cargar_csvxmlrpc/3_res_partner.csv','rb'))
for row in reader:
	print row[0:9]
	res_user={}
	
	ids = sock.execute_kw(db, uid, password,'res.users', 'search',[[['name', '=', row[8].decode('windows-1252').encode('utf-8')]]],{'limit': 1})
	ids_acc_c = sock.execute_kw(db, uid, password,'account.account', 'search',[[['name', '=', row[9].decode('windows-1252').encode('utf-8')]]],{'limit': 1})
	
	
	
	res_partner={
		'name':row[0].decode('windows-1252').encode('utf-8'),		
		'customer':row[1].decode('windows-1252').encode('utf-8'),
		'supplier':row[2].decode('windows-1252').encode('utf-8'),
		'is_company':row[3].decode('windows-1252').encode('utf-8'),
		'street':row[4].decode('windows-1252').encode('utf-8'),
		'zip':row[5].decode('windows-1252').encode('utf-8'),
		'vat':row[6].decode('windows-1252').encode('utf-8'),
		'phone':row[7].decode('windows-1252').encode('utf-8'),
		'user_id':int(ids[0]),
		'property_account_receivable':int(ids_acc_c[0]),
		'property_account_payable':int(ids_acc_c[0]),}
	user_id=sock.execute_kw(db, uid, password,'res.partner', 'create',[res_partner])
#res partner bank
reader = csv.reader(open('/home/drohne/odoo-dev/cargar_csvxmlrpc/4_res_partner_bank.csv','rb'))
for row in reader:
	print row[0:]
	
	ids = sock.execute_kw(db, uid, password,'res.country', 'search',[[['code', '=', row[2].decode('windows-1252').encode('utf-8')]]],{'limit': 1})
	ids_s = sock.execute_kw(db, uid, password,'res.partner', 'search',[[['name', '=', row[3].decode('windows-1252').encode('utf-8')]]],{'limit': 1})	

	res_partner_bank={
				
		'acc_number':row[0].decode('windows-1252').encode('utf-8'),
		'state':row[1].decode('windows-1252').encode('utf-8'),
		'acc_country_id':int(ids[0]),
		'partner_id':int(ids_s[0]),}
		
	user_id=sock.execute_kw(db, uid, password,'res.partner.bank', 'create',[res_partner_bank])
	
