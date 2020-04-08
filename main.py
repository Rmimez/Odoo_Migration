#in this case we are using xmlrpc
import xmlrpc.client 

#source inforamtion
url_source = "http://localhost:8069" #write here database url 
db_source = "" #write here database name
username_source = '' #write here database username
password_source = "" #write here database password
common_source = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_source))
uid_source = common_source.authenticate(db, username, password, {})
print('uid_source...',uid_source)

#destination as example is  a demo got given from odoo web site 
info_dest = xmlrpc.client.ServerProxy('https://demo5.odoo.com/start').start()
url_dest, db_dest, username_dest, password_dest ='https://rmzi.odoo.com/web', 'rmzi', username, 'IMEhcah@fa++'
common_dest = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_dest))
uid_dest = common_dest.authenticate(db_dest, username_dest, password_dest, {})
print('uid_dest...',uid_dest)

models_source = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_source))
models_dest = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_dest))

#note we chosed crm.lead as an example

leads=models_source.execute_kw(db, uid, password, 'crm.lead', 'search_read',[[]], {'fields':['id','name']})
cont=0
for lead in leads:
	cont+=1
	print("lead.. ",lead)
	new_lead=models_dest.execute_kw(db1, uid1, password1, 'crm.lead', 'create',[lead], {}) #Create all leads in destination

