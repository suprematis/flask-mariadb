import pymysql.cursors
from flask import Flask, render_template, request

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "172.29.0.2"
        user = "flaskuser"
        password = "flask123"
        db = "flasktest"
        charset="utf8mb4"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)

        self.cur = self.con.cursor()
    

    def list_tasks(self):
        self.cur.execute("SELECT task_id, task_title, task_status FROM tasks")
        result = self.cur.fetchall()
	
        return result

@app.route('/status')
def tasks():

    def db_query():
        db = Database()
        tsk = db.list_tasks()

        return tsk

    res = db_query() 

    return render_template('tasks.html', result=res, content_type='application/json')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
