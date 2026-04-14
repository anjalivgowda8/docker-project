from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from anjali my fiest docker compose!"

@app.route("/db")
def db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database="testdb",
        user="user",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    return f"PostgreSQL version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
