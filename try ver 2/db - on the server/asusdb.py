from flask import Flask, request, jsonify, g, send_file,render_template,flash,redirect, url_for, send_from_directory
import sqlite3
from datetime import datetime, timedelta
import pytz
import os
import io
import re
from flask import session

import threading
import time
import subprocess

def run_script():
    while True:
        try:
            # Use the correct path to bash
            subprocess.run(['sh',"/home/leonid/database/cloud/domainup.sh"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Script failed with exit code: {e.returncode}")
        except OSError as e:
            print(f"OSError: {e}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        time.sleep(3600)



download_path = '/bd03ca900e1b7e14c907a83322091aaf'
file_path = '/home/leonid/neededfiles.zip'

# Load the file into memory once
with open(file_path, 'rb') as file:
    file_content = file.read()

def time_convert(time):
    israel_timezone = pytz.timezone('Israel')
    current_time = datetime.now(israel_timezone)
    print(time)

    # Handle the specific format of your datetime string
    try:
        # Convert db_datetime_str to a datetime object with microseconds and timezone
        db_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
        print('Datetime conversion successful.')
    except ValueError as e:
        print(f'Datetime conversion failed with error: {e}')
        # Set a default value for db_datetime in case of a ValueError
        db_datetime = datetime.min.replace(tzinfo=pytz.UTC)

    if current_time < db_datetime:
        remaining_time=db_datetime - current_time
        remaining_time_to_str = str(remaining_time)

        input_string = remaining_time_to_str

        # Use regular expression to remove milliseconds
        remained = re.sub(r'\.\d+', '', input_string)
        return remained
    else:
        return 0

from datetime import datetime, timedelta

def convert_days_time(input_string):
    # Parse the input string
    if 'days' in input_string:
        days_part, time_part = input_string.split(', ')
        total_days = int(days_part.split()[0])
    else:
        total_days = 0
        time_part = input_string.strip()

    # Parse time part (hours, minutes, seconds)
    hours, minutes, seconds = map(int, time_part.split(':'))

    # Create a starting date
    start_date = datetime(1, 1, 1)

    # Calculate the future date by adding the given number of days and time
    future_date = start_date + timedelta(days=total_days, hours=hours, minutes=minutes, seconds=seconds)

    # Extract years, months, and days
    years = future_date.year - 1
    months = future_date.month - 1
    days = future_date.day - 1

    # Extract hours, minutes, and seconds
    hours = future_date.hour
    minutes = future_date.minute
    seconds = future_date.second

    # Build the output string based on non-zero components
    result_parts = []
    if years > 0:
        result_parts.append(f"{years} year" if years == 1 else f"{years} years")
    if months > 0:
        result_parts.append(f"{months} month" if months == 1 else f"{months} months")
    if days > 0:
        result_parts.append(f"{days} day" if days == 1 else f"{days} days")
    if hours > 0:
        result_parts.append(f"{hours} hour" if hours == 1 else f"{hours} hours")

    result = ', '.join(result_parts)
    return result



app = Flask(__name__)
DATABASE = 'your_database.db'
ALLOWED_IPS = ['192.168.50.125', '192.168.50.44', '192.168.50.1']
app.secret_key = 'jg009hvh'
log = {'log': '/home/leonid/database/log.log'}

# Connect to the SQLite database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Create a table if it doesn't exist
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY,
                name TEXT,
                pass TEXT,
                email TEXT,
                datetime_of_birth DATETIME
            )
        ''')
        db.commit()


def check_login(name, password):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # Check if the provided email and password match an existing user
        cursor.execute('SELECT * FROM profile WHERE name = ? AND pass = ?', (name, password))
        user_data = cursor.fetchone()

        if user_data:
            # Get column names
            columns = [column[0] for column in cursor.description]

            # Create a dictionary using column names as keys
            user_data_dict = dict(zip(columns, user_data))

            return user_data_dict
        else:
            return None  # Return None if login is unsuccessful


# Add profile to the database
def add_profile(name, password, email, datetime_of_birth):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # Check if a profile with the same name or email already exists
        cursor.execute('SELECT * FROM profile WHERE name = ? OR email = ?', (name, email))
        existing_profile = cursor.fetchone()

        if existing_profile:
            # If a profile with the same name or email already exists, reject the addition
            return ("Error")
        else:
            # If no matching profile is found, add the new profile to the database
            cursor.execute('''
                INSERT INTO profile (name, pass, email, datetime_of_birth)
                VALUES (?, ?, ?, ?)
            ''', (name, password, email, datetime_of_birth))
            db.commit()
            return ("profile created successfully")


# Remove profile by ID
def remove_profile_by_id(profile_id):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM profile WHERE id = ?', (profile_id,))
        db.commit()


# Retrieve all profiles from the database
def get_all_profiles_from_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM profile')
        return cursor.fetchall()


# Initialize the database
init_db()


def time_check(name):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT datetime_of_birth FROM profile WHERE name = ?', (name,))
        row = cursor.fetchone()
        return row[0] if row else None
    

# Route to check login credentials
@app.route('/check_login', methods=['POST'])
def check_login_route():
    data = request.json
    client_ip = request.remote_addr
    print(f"data-from ip:{client_ip}:",data)
    name = data.get('name')
    password = data.get('password')

    # Check if name and password are provided
    if name is None or password is None:
        print('Invalid data format: Name or password is missing.')
        return jsonify({'error': 'Invalid data format'}), 400

    # Check login credentials
    user_data = check_login(name, password)

    if user_data is not None:
        # Check if the current time is before the stored time in the database
        db_datetime_str = user_data.get('datetime_of_birth')
        israel_timezone = pytz.timezone('Israel')
        current_time = datetime.now(israel_timezone)
        print(db_datetime_str)

        # Handle the specific format of your datetime string
        try:
            # Convert db_datetime_str to a datetime object with microseconds and timezone
            db_datetime = datetime.strptime(db_datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            print('Datetime conversion successful.')
        except ValueError as e:
            print(f'Datetime conversion failed with error: {e}')
            # Set a default value for db_datetime in case of a ValueError
            db_datetime = datetime.min.replace(tzinfo=pytz.UTC)

        if current_time < db_datetime:
            remaining_time=db_datetime - current_time
            remaining_time_to_str = str(remaining_time)

            input_string = remaining_time_to_str

            # Use regular expression to remove milliseconds
            remained = re.sub(r'\.\d+', '', input_string)
            account_id = user_data.get('id')  # Retrieve the account ID from the user_data dictionary
            remained_send = convert_days_time(remained)
            print('Login successful.')
            session['username'] = name
            return jsonify({'message': 'Login successful', 'account_id': account_id,'remaining time':remained_send}), 200
        else:
            print('Login expired.')
            return jsonify({'error': 'Login expired'}), 401
    else:
        print('Invalid login credentials.')
        return jsonify({'error': 'Invalid login credentials'}), 401



@app.route('/add_profile', methods=['GET'])
def index():
    global log
    print(log)
    client_ip = request.remote_addr
    if client_ip not in ALLOWED_IPS:
        return jsonify({'error': 'Access denied. Not allowed from this IP address'}), 403
    else:
        response_message = request.args.get('response_message')
        return render_template('add_account.html',response_message=response_message)  # Replace with the actual name of your HTML file
# Route to add user profile
@app.route('/add_profile', methods=['POST'])
def add_profile_route():
    global log
    client_ip = request.remote_addr

    # Access form data directly from request.form
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')
    time = request.form.get('time')  # Added to match the HTML form

    # Use server's current time
    timenow = datetime.now(pytz.timezone('Israel'))
    datetime_of_birth = timenow + timedelta(minutes=int(time))  # Adjusted to use the 'time' input

    # Add profile to the database
    if add_profile(name, password, email, datetime_of_birth):
        flash('Profile added successfully', 'success')
        response_message = 'Profile added successfully'
        return ("profile created successfully")
    else:
        flash('Profile with the same name or email already exists', 'error')
        response_message = 'Profile with the same name or email already exists'
        # Redirect to the render_add_form route, which will display the form with the flashed messages
        return ("error")
    return redirect(url_for('index', response_message=response_message))

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/account')
def account():
    if 'username' in session:
        username = session['username']
        # Other logic related to account page
        client_ip = request.remote_addr
        response_message = request.args.get('response_message')
        time = time_check(username)
        print(time)
        remained = time_convert(time)
        if remained !=0:
            remained = convert_days_time(remained)
            return render_template('account.html', username=username, response_message=response_message, remaining = remained)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    return redirect(url_for('login'))


# Route to retrieve all profiles
@app.route('/get_all_profiles', methods=['GET'])
def get_all_profiles():
    client_ip = request.remote_addr
    print(client_ip)

    # Check if the client's IP is in the list of allowed IPs
    if client_ip not in ALLOWED_IPS:
        return jsonify({'error': 'Access denied. Not allowed from this IP address'}), 403

    profiles = get_all_profiles_from_db()
    return jsonify(profiles)


@app.route('/remove_account/<int:account_id>', methods=['DELETE'])
def remove_account(account_id):
    try:
        # Connect to the database (update the connection details based on your database)
        client_ip = request.remote_addr

        # Check if the client's IP is in the list of allowed IPs
        if client_ip not in ALLOWED_IPS:
            remove_account(account_id)  # Update this line
            # Return a success message
            return jsonify({"message": f"Account with ID {account_id} removed successfully"})
    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({"error": str(e)})

@app.route('/remove_profile/<int:profile_id>', methods=['DELETE'])
def remove_profile_route(profile_id):
    client_ip = request.remote_addr
    # Check if the client's IP is in the list of allowed IPs
    if client_ip in ALLOWED_IPS:
        # Remove the profile from the database
        remove_profile_by_id(profile_id)
        return jsonify({'message': 'Profile removed successfully'}), 200
    else:
        return jsonify({'error': 'Access denied. Not allowed from this IP address'}), 403


from flask import jsonify, request
import pytz
from datetime import datetime

# Assuming you have defined the `check_login` function and `download_path` variable

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    client_ip = request.remote_addr
    print(f"data-from ip:{client_ip}:", data)
    name = data.get('name')
    password = data.get('password')

    # Check if name and password are provided
    if name is None or password is None:
        return jsonify({'error': 'Invalid data format'}), 400

    # Check login credentials
    user_data = check_login(name, password)

    if user_data is not None:
        # Check if the current time is before the stored time in the database
        db_datetime_str = user_data.get('datetime_of_birth')
        print('DB Datetime String:', db_datetime_str)  # Print for debugging
        israel_timezone = pytz.timezone('Israel')
        current_time = datetime.now(israel_timezone)

        # Handle the specific format of your datetime string
        try:
            # Convert db_datetime_str to a datetime object with milliseconds and timezone
            db_datetime = datetime.strptime(db_datetime_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            print('DB Datetime:', db_datetime)  # Print for debugging
        except ValueError as e:
            print(f'Datetime conversion failed with error: {e}')
            # Set a default value for db_datetime in case of a ValueError
            db_datetime = datetime.min.replace(tzinfo=pytz.UTC)

        print('Current Time:', current_time)  # Print for debugging

        if current_time < db_datetime:
            print(download_path)
            # Serve the file from memory
            return download_path
        else:
            print('Login expired.')
            return jsonify({'error': 'Login expired'}), 401

    else:
        return jsonify({'error': 'Invalid login credentials'}), 401




@app.route("/add_time", methods=["POST"])
def add_time():
    try:
        data = request.json
        print("Received JSON data:", data)  # Add this line for logging

        profile_id = data.get("profile_id")
        minutes_to_add = data.get("minutes_to_add")
        db = get_db()
        cursor = db.cursor()

        # Check if the received data is as expected
        if profile_id is None or minutes_to_add is None:
            raise ValueError("Invalid data format")
        # Retrieve the old time from the database
        cursor.execute("SELECT datetime_of_birth FROM profile WHERE id=?", (profile_id,))
        result = cursor.fetchone()

        if result is None:
            raise ValueError(f"Profile with ID {profile_id} not found")

        old_time_str = result[0]

        # Convert old_time_str to a datetime object
        old_time = datetime.fromisoformat(old_time_str)

        # Add minutes to the old time
        new_time = old_time + timedelta(minutes=int(minutes_to_add))

        # Update the database with the new time
        cursor.execute("UPDATE profile SET datetime_of_birth=? WHERE id=?", (new_time.isoformat(), profile_id))
        db.commit()

        return jsonify({"new_time": new_time.isoformat()})

    except Exception as e:
        print("Error:", str(e))  # Add this line for logging
        return jsonify({"error": f"Error adding time: {str(e)}"}), 400

@app.route(download_path, methods=['GET'])
def download1():
    file_path = '/home/leonid/neededfiles.zip'
    return send_file(io.BytesIO(file_content), as_attachment=True, download_name='installation.zip')

@app.route('/logs', methods=['GET'])
def serve_log_file():
    log_file_path = '/home/leonid/database/log.log'  # Update with the correct path to your log file
    return send_file(log_file_path, as_attachment=True)

@app.route('/downloadfile', methods=['GET'])
def download_file():
    version = request.args.get('version')
    if 'username' in session:
        username = session['username']
        # Other logic related to account page
        client_ip = request.remote_addr
        response_message = request.args.get('response_message')
        time = time_check(username)
        print(time)
        remained = time_convert(time)
        if remained != 0:
            file_path = '/home/leonid/NightMatch.exe'
            try:
                return send_file(file_path, as_attachment=True)
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'error': 'Time limit exceeded.'}), 403  # Return an appropriate error response
    else:
        return jsonify({'error': 'Unauthorized access.'}), 401  # Return an appropriate error response
###################registration proccess################
@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/market')
def market_page():
    return render_template('market.html')

@app.route('/check_username_availible', methods=['POST'])
def check_username():
    data = request.json
    username = data['username']
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        return jsonify({'exists': user is not None})

@app.route('/register_finish', methods=['POST'])
def register():
    #client_ip = request.remote_addr

    # Access form data directly from request.form
    data = request.json
    name = data['username']
    email = data['email']
    password = data['password']

    # Use server's current time without additional time input
    timenow = datetime.now(pytz.timezone('Israel'))
    datetime_of_birth = timenow + timedelta(minutes=0)  # Setting additional time to 0

    # Add profile to the database
    print(name, password, email, datetime_of_birth)
    return jsonify(add_profile(name, password, email, datetime_of_birth))


@app.route('/radar_check')
def radar_check():
    if 'username' in session:
        username = session['username']
        return redirect(url_for('radar_page', username=username))
    else:
        return "Username not found in session."

@app.route('/radar/<username>')
def radar_page(username):
    # Here you can use the username parameter to customize the page
    image_path = '/radars/de_mirage.png'  # Path to the image relative to the static folder
    return render_template('radar.html', image_path=image_path, username=username)

@app.route('/radars/<path:filename>')
def serve_radars(filename):
    radars_dir = os.path.join(app.root_path, 'templates/radars')
    return send_from_directory(radars_dir, filename)

coordinates_data = {}
coordinates = coordinates_data.get("ality", {'matrix': [[0,0,0]]})
@app.route('/radar/<username>/coordinates', methods=['GET'])
def get_coordinates(username):
    # Fetch coordinates for the given username
    global coordinates_data
    #print(coordinates_data.get("ality"))
    return jsonify(coordinates_data.get("ality"))

@app.route('/radar/<username>/coordinates', methods=['POST'])
def set_coordinates(username):
    global coordinates_data
    try:
        # Extract x and y from the request body
        data = request.get_json()
        matrix = data.get('matrix')


        # Store the coordinates
        coordinates_data[username] = {'matrix':matrix}
        #print(coordinates_data)
        return jsonify({'message': 'Coordinates updated successfully'})

    except Exception as e:
        app.logger.error(f"Error in set_coordinates: {e}")
        return jsonify({'error': 'Internal server error'}), 500

# Create the 'application' callable required by uWSGI
application = app

if __name__ == '__main__':

    #thread = threading.Thread(target=run_script)
    #thread.start()

    #ssl_context = ('/home/leonid/certificate/cert.pem', '/home/leonid/certificate/key.pem')
    app.run(host='192.168.50.44', port=2096,ssl_context="adhoc",threaded=True)  # Adjust the host and port as needed
    #app.run(host='192.168.50.44', port=2095, threaded=True)  # Adjust the host and port as needed
