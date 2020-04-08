# Odoo_Migration

This script is an example to help developer to understand of data migration from version to version.
in this script we used xml_rpc method and that how i subbmited in my code where i migrate from my data in localhost to a demo given by odoo site to try understanding .

in the begining u need to enter information of the source and destination data all of url, db_name , username and password , 

after that u will create a common wich contien '{url}/xmlrpc/2/object', The xmlrpc/2/common endpoint provides meta-calls which don’t require authentication, such as the authentication itself or fetching version information. To verify if the connection information is correct before trying to authenticate, the simplest call is to ask for the server’s version. The authentication itself is done through the authenticate function and returns a user identifier (uid) used in authenticated calls instead of the login.

The second endpoint is xmlrpc/2/object, is used to call methods of odoo models via the execute_kw RPC function to read , search , update or search_read.

the last function is the racord creation of model using create(). The method will create a single record and return its database identifier, all records can complete by the iteration. 


