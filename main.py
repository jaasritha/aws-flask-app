from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

@app.route('/')
def dashboard():
    user_rows = ""
    for u in users:
        user_rows += f"<tr><td>{u['id']}</td><td>{u['name']}</td></tr>"

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Flask API Dashboard</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .card {{ background: white; border-radius: 8px; padding: 20px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .card h2 {{ margin-top: 0; color: #333; }}
        .status {{ display: inline-block; padding: 4px 12px; border-radius: 12px; background: #4caf50; color: white; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #ddd; }}
        th {{ background: #f0f0f0; }}
        .hello {{ font-size: 24px; color: #2196f3; }}
        h1 {{ color: #333; }}
    </style>
</head>
<body>
    <h1>Flask API Dashboard</h1>

    <div class="card">
        <h2>Health Status</h2>
        <p>API Status: <span class="status">OK</span></p>
    </div>

    <div class="card">
        <h2>Hello Message</h2>
        <p class="hello">Hello, World!</p>
    </div>

    <div class="card">
        <h2>Users</h2>
        <table>
            <tr><th>ID</th><th>Name</th></tr>
            {user_rows}
        </table>
    </div>

    <div class="card">
        <h2>API Endpoints</h2>
        <table>
            <tr><th>Endpoint</th><th>Method</th><th>Description</th></tr>
            <tr><td><a href="/hello">/hello</a></td><td>GET</td><td>Returns hello message (JSON)</td></tr>
            <tr><td><a href="/users">/users</a></td><td>GET</td><td>Returns all users (JSON)</td></tr>
            <tr><td><a href="/health">/health</a></td><td>GET</td><td>Health check (JSON)</td></tr>
        </table>
    </div>
</body>
</html>"""

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="OK"), 200


if __name__ == '__main__':
    app.run(debug=True)
