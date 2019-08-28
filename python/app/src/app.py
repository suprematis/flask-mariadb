import MySQLdb as mdb
from flask import Flask
from flask import request
from flask import Flask, render_template
import subprocess


app = Flask(__name__)
#ip_whitelist = ['127.0.0.1']
#query_success = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Success'"
#query_pending = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Pending'"
#query_failed = "SELECT COUNT(*) FROM flasktest.tasks WHERE task_status='Failed'"

class Database:
    def __init__(self):
        host = "mariadb"
        user = "flaskuser"
        password = "flask123"
        db = "flasktest"
        self.con = mdb.connect(host=host, user=user, password=password, db=db)
        self.cur = self.con.cursor()
    def list_tasks(self):
        self.cur.execute("SELECT task_id, task_title, task_status FROM tasks LIMIT 50")
        result = self.cur.fetchall()
        return result


@app.route('/status/')
def tasks():

    def db_query():
        db = Database()
        tasks = db.list_tasks()

        return tasks

    res = db_query() 

    return render_template('tasks.html', result=res, content_type='application/json')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
