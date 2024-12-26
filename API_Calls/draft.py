# import requests
# import pymysql
# import json
# from flask import Flask, request, jsonify
#
# # Flask app to simulate an API endpoint
# app = Flask(__name__)
#
#
# # Database connection setup
# def get_connection():
#     return pymysql.connect(
#         host="localhost",
#         user="root",
#         password="Katasraj111#",
#         database="SeleniumCourses"
#     )
#
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
#
# # Simulating POST call using requests module
# def simulate_post_request():
#     try:
#         url = "http://127.0.0.1:5000/insert_record"  # Flask server running locally
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
#         # POST request using requests module
#         response = requests.post(url, json=payload)
#
#         # Response from the server
#         if response.status_code == 201:
#             print("Record inserted successfully:", response.json())
#         else:
#             print("Error:", response.json())
#     except Exception as e:
#         print(f"Error during API simulation: {e}")
#
#
# if __name__ == '__main__':
#     # Start Flask app in a separate thread
#     import threading
#
#     flask_thread = threading.Thread(target=app.run, kwargs={"debug": False})
#     flask_thread.start()
#
#     # Simulate POST request
#     simulate_post_request()
#
#


###########################################################################################################

# import requests
# import pymysql
# import json
# from flask import Flask, request, jsonify
# import threading
#
# # Flask app to simulate an API endpoint
# app = Flask(__name__)
#
# # Database connection setup
# def get_connection():
#     return pymysql.connect(
#         host="localhost",
#         user="root",
#         password="Katasraj111#",
#         database="SeleniumCourses"
#     )
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
#     shutdown_function = request.environ.get('werkzeug.server.shutdown')
#     if shutdown_function is None:
#         raise RuntimeError("Not running with the Werkzeug Server")
#     shutdown_function()
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
#     flask_thread = threading.Thread(target=app.run, kwargs={"debug": False})
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

########################################################################################################

import requests
import pymysql
import json
from flask import Flask, request, jsonify
import threading
import os
import signal

# Flask app to simulate an API endpoint
app = Flask(__name__)

# Database connection setup
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Katasraj111#",
        database="SeleniumCourses"
    )

# API route to handle POST requests
@app.route('/insert_record', methods=['POST'])
def insert_record():
    try:
        # Get JSON payload from POST request
        data = request.json

        # Extract data from the payload
        username = data.get("username")
        course_name = data.get("course_name")
        price = data.get("price")
        subscription_start_date = data.get("subscription_start_date")
        subscription_end_date = data.get("subscription_end_date")

        # Insert into the database
        conn = get_connection()
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
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Route to shut down the Flask server
@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)  # Sends a signal to terminate the process
    return jsonify({"message": "Server shutting down..."})

# Simulating POST call using requests module
def simulate_post_request():
    try:
        # API endpoint
        url = "http://127.0.0.1:5000/insert_record"

        # JSON payload
        payload = {
            "username": "John Doe",
            "course_name": "Python Basics",
            "price": 99.99,
            "subscription_start_date": "2024-01-01",
            "subscription_end_date": "2024-12-31"
        }

        # POST request
        response = requests.post(url, json=payload)

        # Response handling
        if response.status_code == 201:
            print("Record inserted successfully:", response.json())
        else:
            print("Error:", response.json())

        # Shut down the server after the request
        shutdown_url = "http://127.0.0.1:5000/shutdown"
        requests.post(shutdown_url)

    except Exception as e:
        print(f"Error during API simulation: {e}")

# Main function to start Flask server and simulate POST request
def main():
    flask_thread = threading.Thread(target=app.run, kwargs={"debug": False, "use_reloader": False})
    flask_thread.start()

    # Simulate the POST request
    simulate_post_request()

    # Wait for the Flask thread to finish
    flask_thread.join()

if __name__ == "__main__":
    main()


