from flask import Flask, request, jsonify
from API_Calls.configurations import getConnection
from configfiles.location_path import Path_Login
from datetime import datetime,timedelta
import threading
import signal
import os
import requests
import pymysql

class APIServer:
    def __init__(self,c,p):
        self.c = c
        self.p = p
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/insert_record', methods=['POST'])
        def insert_record():
            try:
                # Parse JSON data from request
                data = request.json
                username = data.get('username')
                course_name = data.get('course_name')
                price = data.get('price')
                subscription_start_date = data.get('subscription_start_date')
                subscription_end_date = data.get('subscription_end_date')

                # Insert into MySQL
                conn = self._get_connection()
                cursor = conn.cursor()
                query = """
                    INSERT INTO users (username, course_name, price, subscription_start_date, subscription_end_date)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (username, course_name, price, subscription_start_date, subscription_end_date))
                conn.commit()

                return jsonify({"message": "Record inserted successfully"}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

        @self.app.route('/shutdown', methods=['POST'])
        def shutdown():
            os.kill(os.getpid(), signal.SIGINT)  # Sends a signal to terminate the process
            return jsonify({"message": "Server shutting down..."})

    def _get_connection(self):
        dbconnection = getConnection()
        return dbconnection

    def start(self):
        threading.Thread(target=self.app.run, kwargs={"debug": False, "use_reloader": False}).start()

    def stop(self):
        requests.post("http://127.0.0.1:5000/shutdown")

    def today_date(self):
        today = datetime.now().date()
        formatted_date = today.strftime("%Y-%m-%d")
        return formatted_date

    def end_date(self):
        date_obj = datetime.strptime(self.today_date(), "%Y-%m-%d")
        new_date_obj = date_obj + timedelta(days=365)
        new_date_str = new_date_obj.strftime("%Y-%m-%d")
        return new_date_str


    def use_api_server(self):
        self.start()

        # Simulate a POST request to insert data
        url = "http://127.0.0.1:5000/insert_record"
        data = {
            "username": Path_Login().login_details()['username'],
            "course_name": self.c,
            "price": self.p,
            "subscription_start_date": self.today_date(),
            "subscription_end_date": self.end_date()
        }
        response = requests.post(url, json=data)

        # Handle the response
        if response.status_code == 201:
            print("Record inserted successfully:", response.json())
        else:
            print("Error:", response.json())

        # Stop the server
        self.stop()



# if __name__ == "__main__":
#     u = APIServer()
#     u.use_api_server()
