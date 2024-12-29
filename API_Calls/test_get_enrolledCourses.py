from API_Calls.POST_call_setup import APIServer
from utilities.read_data import ReadData
from ddt import data,ddt,unpack
import unittest
import time
import allure
import pytest
import requests
#
# @pytest.fixture(scope="class")
# def api_server():
#     server = APIServer()
#     server.start()
#     yield server
#     server.stop()
#
# class TestAPIServer:
#     @allure.step("Verifying GET request to check the courses in database")
#     def test_get_courses(self, api_server):
#         #url = "http://127.0.0.1:5000/get_courses"
#         response = APIServer().get_courses_from_db()
#         assert response.status_code == 200



#APIServer().delete_courses_from_db()

#APIServer("F:\\PycharmProjects\\SeleniumCapstone\\configfiles\\testdata.csv").insert_course()

def test_get_courses():
    with allure.step("Get Enrolled Courses"):
        with allure.step("Initiating test to fetch enrolled courses"):
            response = APIServer().get_courses_from_db()
            assert response.status_code == 200




# @ddt
# class TestInsertDB(unittest.TestCase):
#     # Combine course names and prices into a single list of tuples
#     @data(*ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").getCombinedData())
#     @
#     def test_insert_DB(self,courseName,prices):
#         print(f"Inserting course: {courseName} with price: {prices}")
#         APIServer(courseName,prices).use_api_server()

# if __name__ == "__main__":
#     unittest.main()
# d = ReadData("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").getCombinedData()
# print(d)
# for c,p in d:
#     print(c)
#     print(p)
#     APIServer(c,p).use_api_server()
# t = APIServer("Selenium WebDriver 4 With Java",15)
# u.use_api_server()
#s.use_api_server()
# t.use_api_server()

# APIServer("F:\\PycharmProjects\\SeleniumCapstone\\testdata.csv").insert_course()
# time.sleep(2)
# time.sleep(2)
# APIServer().delete_courses()

#print(Path_Login().login_details()['username'])


# def today_date():
#     today = datetime.now().date()
#     formatted_date = today.strftime("%Y-%m-%d")
#     return formatted_date
#
#
# def end_date():
#     date_obj = datetime.strptime(today_date(), "%Y-%m-%d")
#     new_date_obj = date_obj + timedelta(days=365)
#     new_date_str = new_date_obj.strftime("%Y-%m-%d")
#     return new_date_str

# print(today_date())
# print(end_date())


'''
How It Works
Class Structure: The APIServer class encapsulates all the server-related logic. 
The _setup_routes method defines the API routes.
start and stop Methods: These methods allow the server to be started and stopped programmatically.
Reusable: The server can now be instantiated and used in any file or function, making it modular and testable.

Advantages of Using a Class
Encapsulation: Keeps server-related logic in one place.
Reusability: The server can be instantiated multiple times if needed.
Ease of Maintenance: Routes, configurations, and database logic are all within the class.
If you don't want to use a class, you can still achieve modularity by defining functions for start_server 
and stop_server instead. Let me know if you'd like an example without a class!

@pytest.mark.run(order=1) and @pytest.mark.run(order=2) may not always work as intended with pytest 
in combination with ddt

In pytest, you can use the pytest-dependency plugin to establish dependencies between tests in different classes.
'''

# import requests
# import pymysql
# from flask import Flask, request, jsonify
# from API_Calls.configurations import getConnection
# import threading
# import os
# import signal
#
#
# # Flask app to simulate an API endpoint
# app = Flask(__name__)
#
# # Database connection setup
# def get_connection():
#     dbconnection = getConnection()
#     return dbconnection
#
# # API route to handle POST requests
# @app.route('/insert_record', methods=['POST'])
# def insert_record():
#     try:
#         # Get JSON payload from POST request
#         data = request.json
#
#         # Extract data from the payload
#         username = data.get("username")
#         course_name = data.get("course_name")
#         price = data.get("price")
#         subscription_start_date = data.get("subscription_start_date")
#         subscription_end_date = data.get("subscription_end_date")
#
#         # Insert into the database
#         conn = get_connection()
#         cursor = conn.cursor()
#
#         query = """
#         INSERT INTO users (username, course_name, price, subscription_start_date, subscription_end_date)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(query, (username, course_name, price, subscription_start_date, subscription_end_date))
#         conn.commit()
#
#         return jsonify({"message": "Record inserted successfully"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
# # Route to shut down the Flask server
# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#     os.kill(os.getpid(), signal.SIGINT)  # Sends a signal to terminate the process
#     return jsonify({"message": "Server shutting down..."})
#
# # Simulating POST call using requests module
# def simulate_post_request():
#     try:
#         # API endpoint
#         url = "http://127.0.0.1:5000/insert_record"
#
#         # JSON payload
#         payload = {
#             "username": "John Doe",
#             "course_name": "Python Basics",
#             "price": 99.99,
#             "subscription_start_date": "2024-01-01",
#             "subscription_end_date": "2024-12-31"
#         }
#
#         # POST request
#         response = requests.post(url, json=payload)
#
#         # Response handling
#         if response.status_code == 201:
#             print("Record inserted successfully:", response.json())
#         else:
#             print("Error:", response.json())
#
#         # Shut down the server after the request
#         shutdown_url = "http://127.0.0.1:5000/shutdown"
#         requests.post(shutdown_url)
#
#     except Exception as e:
#         print(f"Error during API simulation: {e}")
#
# # Main function to start Flask server and simulate POST request
# def main():
#     flask_thread = threading.Thread(target=app.run, kwargs={"debug": False, "use_reloader": False})
#     flask_thread.start()
#
#     # Simulate the POST request
#     simulate_post_request()
#
#     # Wait for the Flask thread to finish
#     flask_thread.join()
#
# if __name__ == "__main__":
#     main()

