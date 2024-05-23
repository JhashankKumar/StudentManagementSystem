import json
import tornado.web
from db import connection
from utils import hash_password, check_password

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")

class SignupHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        email = data['email']
        password = hash_password(data['password'])
        role = data.get('role', 'teacher')
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (email, password, role) VALUES (%s, %s, %s)", (email, password, role))
        connection.commit()
        self.write(json.dumps({"success": True}))

class LoginHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        email = data['email']
        password = data['password']
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, password, role FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
        if user and check_password(password, user['password']):
            self.write(json.dumps({"success": True, "role": user['role']}))
        else:
            self.write(json.dumps({"success": False}))

class ResultsHandler(BaseHandler):
    def get(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM results")
                results = cursor.fetchall()
            self.write(json.dumps(results))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"error": str(e)}))

    def post(self):
        try:
            data = json.loads(self.request.body)
            student_name = data['studentName']
            telugu = data['telugu']
            hindi = data['hindi']
            english = data['english']
            maths = data['maths']
            attendance = data['attendance']
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO results (studentName, telugu, hindi, english, maths, attendance) VALUES (%s, %s, %s, %s, %s, %s)", (student_name, telugu, hindi, english, maths, attendance))
            connection.commit()
            self.write(json.dumps({"success": True}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"error": str(e)}))

class ResultHandler(BaseHandler):
    def delete(self, id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM results WHERE id = %s", (id,))
            connection.commit()
            self.write(json.dumps({"success": True}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"error": str(e)}))
