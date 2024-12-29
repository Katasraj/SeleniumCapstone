from flask import Flask, request, jsonify
from API_Calls.configurations import getConnection
from configfiles.location_path import Path_Login
from datetime import datetime,timedelta
import threading
import signal
import os
import requests
import csv
import pymysql
import allure
import logging
import utilities.custom_logger as cl



@allure.description("Verifying Courses availability in MySQL Database ")
class APIServer:
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,csv_file_path=None):
        # self.c = c
        # self.p = p
        self.courses = []  # List to store course names
        self.prices = []  # List to store course prices
        self._read_csv(csv_file_path)  # Read and parse the CSV file
        self.app = Flask(__name__)
        self._test_setup_routes()


    def _read_csv(self, csv_file_path):
        """
        Reads courses and prices from the provided CSV file and populates
        the `self.courses` and `self.prices` lists.
        """
        try:
            with open(csv_file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                # Skip the header if present
                next(csv_reader, None)
                for row in csv_reader:
                    # Assuming CSV format: course_name, price
                    course_name, price = row[0], float(row[1])
                    self.courses.append(course_name)
                    self.prices.append(price)
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    @allure.step("Configuration of API calls")
    def _test_setup_routes(self):
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


        @self.app.route('/get_courses', methods=['GET'])
        def get_courses():
            """
            Retrieve all courses and their prices from the database.
            """
            try:
                # Connect to the database
                conn = self._get_connection()
                cursor = conn.cursor()

                # Execute the query
                query = "select * from users"
                cursor.execute(query)
                courses = cursor.fetchall()

                # Return the result as JSON
                return jsonify({"success": True, "data": courses}), 200


            except Exception as e:
                return jsonify({"error": str(e)}), 500
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

        @self.app.route('/delete_courses', methods=['DELETE'])
        def delete_courses():
            """
            Delete all courses and their prices from the database.
            """
            try:
                # Connect to the database
                conn = self._get_connection()
                cursor = conn.cursor()

                # Execute the query
                query = """ truncate table users """
                cursor.execute(query)
                courses = cursor.fetchall()

                # Return the result as JSON
                return jsonify({"success": True, "data": courses}), 200

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


    def insert_course(self):
        self.start()

        # Simulate a POST request to insert data
        url = "http://127.0.0.1:5000/insert_record"

        # data = {
        #     "username": Path_Login().login_details()['username'],
        #     "course_name": self.c,
        #     "price": self.p,
        #     "subscription_start_date": self.today_date(),
        #     "subscription_end_date": self.end_date()
        # }
        # response = requests.post(url, json=data)
        #
        # # Handle the response
        # if response.status_code == 201:
        #     print("Record inserted successfully:", response.json())
        # else:
        #     print("Error:", response.json())

        for c in range(len(self.courses)):

            data = {
                "username": Path_Login().login_details()['username'],
                "course_name": self.courses[c],
                "price": self.prices[c],
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

    # @allure.step("Verifying GET request to check the courses in database")
    # def get_courses_from_db(self):
    #     self.start()
    #
    #     # Simulate a POST request to insert data
    #     url = "http://127.0.0.1:5000/get_courses"
    #     res = requests.get(url)
    #     with allure.step("Ge the response code and enrolled courses"):
    #         print(res.status_code)
    #         print(res.text)
    #     # Stop the server
    #     self.stop()

    @allure.step("Verifying GET request to check the courses in database")
    def get_courses_from_db(self):
        self.start()
        try:
            # Simulate a GET request to retrieve courses
            url = "http://127.0.0.1:5000/get_courses"
            response = requests.get(url)

            # with allure.step("Log response code and enrolled courses"):
            #     allure.attach(str(res.status_code), name="Response Code", attachment_type=allure.attachment_type.TEXT)
            #     allure.attach(res.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)
            self.log.info(response.status_code)
            self.log.info(response.json())  # If response is in JSON format
            self.log.info( response.text)  # As plain text
            self.log.info(response.content)  # As raw bytes

        finally:
            # Stop the server
            self.stop()

    def delete_courses_from_db(self):
        self.start()

        # Simulate a POST request to insert data
        url = "http://127.0.0.1:5000/delete_courses"
        response = requests.delete(url)
        if response.status_code == 200:
            print("Record deleted successfully:", response.json())
        else:
            print("Error:", response.json())
        # print(res.status_code)
        # Stop the server
        self.stop()

    def _course_delete_insert(self):
        try:

            self.start()

            # Simulate a POST request to insert data
            url = "http://127.0.0.1:5000/delete_courses"
            response = requests.delete(url)
            if response.status_code == 200:
                #print("Record deleted successfully:", response.json())
                self.log.info("Record deleted successfully")
                self.log.info(response.json())
            else:
                self.log.info("Error in deleted records")
                #print("Error:", response.json())

            url_i = "http://127.0.0.1:5000/insert_record"
            for c in range(len(self.courses)):

                data = {
                    "username": Path_Login().login_details()['username'],
                    "course_name": self.courses[c],
                    "price": self.prices[c],
                    "subscription_start_date": self.today_date(),
                    "subscription_end_date": self.end_date()
                }
                response_i = requests.post(url_i, json=data)

                # Handle the response
                if response_i.status_code == 201:
                    #print("Record inserted successfully:", response.json())
                    self.log.info("Record inserted successfully")
                    self.log.info(response_i.json())
                else:
                    self.log.info("Error in inserting Records")
                    #print("Error:", response.json())

            url_g = "http://127.0.0.1:5000/get_courses"
            response_get = requests.get(url_g)
            if response_get.status_code == 200:
                self.log.info("Courses got successfully")
                self.log.info(response_get.json())
                #print("Record got successfully:", response_get.json())
            else:
                self.log.info("Error in getting courses")
                self.log.info(response_get.json())
                #print("Error:", response_get.json())

        except Exception as e:
            self.log.error(f"An unexpected error occurred: {e}")
        finally:
            # Ensure the server is stopped regardless of success or failure
            self.stop()

#if __name__ == "__main__":
    # u = APIServer()
    #u.use_api_server()
    # u.get_courses_from_db()

