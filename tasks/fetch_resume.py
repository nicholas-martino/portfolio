import psycopg2
import sqlite3

# DATABASE_URL=$(heroku config:get DATABASE_URL -a your-app) your_process
DATABASE_URL = 'postgres://oclekeinjrewoq:70417736b4201297098f6d8e8085cba15efab34ed21a8af08a425c52112f3845@ec2-3-214-136-47.compute-1.amazonaws.com:5432/d4hjtefv833vil'


conn = psycopg2.connect(
	DATABASE_URL,
	user='oclekeinjrewoq',
	password='70417736b4201297098f6d8e8085cba15efab34ed21a8af08a425c52112f3845',
	host='ec2-3-214-136-47.compute-1.amazonaws.com',
	port='5432',
	sslmode='require'
)
cursor = conn.cursor()

sql = "SELECT * FROM d4hjtefv833vil.public.positions_position;"
cursor.execute(sql)
positions = cursor.fetchall()

sql = "SELECT * FROM d4hjtefv833vil.public.projects_project;"
cursor.execute(sql)
projects = cursor.fetchall()


sql = ""
conn = sqlite3.connect('db.sqlite3')
