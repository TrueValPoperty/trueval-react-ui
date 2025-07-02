
import os
from flask import Flask, request, jsonify, send_from_directory, session, redirect, url_for
from airtable import Airtable
from functools import wraps

app = Flask(__name__, static_folder='.', static_url_path='')
app.secret_key = os.environ.get("SECRET_KEY", "changeme")

# Airtable config
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    polygon = data.get("geometry")
    land_area_m2 = data.get("area_m2")
    if not polygon or not land_area_m2:
        return jsonify({"error": "Missing polygon or area"}), 400
    result = {"estimated_units": int(float(land_area_m2) // 90)}
    return jsonify(result)

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    record = airtable.insert(data)
    return jsonify(record), 201

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

@app.route('/logs')
@login_required
def logs():
    records = airtable.get_all()
    return jsonify(records), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        if data.get("username") == "admin" and data.get("password") == "letmein":
            session["logged_in"] = True
            return redirect("/logs")
        return "Invalid credentials", 401
    return '''
        <form method="post">
            <input name="username" placeholder="Username"/><br/>
            <input name="password" type="password" placeholder="Password"/><br/>
            <input type="submit" value="Login"/>
        </form>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)
