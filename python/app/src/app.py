import MySQLdb as mdb
from flask import Flask
from flask import request
import subprocess

db=mdb.connect('db','flaskuser','flask123','flasktest')
app = Flask('flask-mysql')
#ip_whitelist = ['127.0.0.1']
query_success = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Success'"
query_pending = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Pending'"
query_failed = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Failed'"
cur = db.cursor()
def sql_queries(ref):
     def success():
         cur.execute(query_success)
         return query_success
     def pending():
         return query_pending
     def failed():
         return query_failed
     if ref == 1:
         return success
     else:
         return pending
    	

@app.route('/status/')
def get_status( success, pending ):
        return ( success, pending );


 
pending = cur.execute(query_pending)
get_status( success, pending ) 

print ( success, pending )
#return 'Success %s, Pending %s' % (command_success, command_pending)
#        return 'Success %s, Pending %s, Failed %s' % (result_success, result_pending, result_failed)
#    else:
#        return """<title>404 Not Found</title>
#               <h1>Not Found</h1>
#               <p>The requested URL was not found on the server.
#               If you entered the URL manually please check your
#               spelling and try again.</p>""", 404
#

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
