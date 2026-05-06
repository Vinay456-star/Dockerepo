from flask import Flask # type: ignore
import redis # type: ignore

app = Flask(__name__)

# 🔥 connect to Redis running on HOST (mapped port)
r = redis.Redis(host='host.docker.internal', port=6379, decode_responses=True)

@app.route("/")
def home():
    try:
        count = r.incr("counter")
        return f"Hello! You visited {count} times"
    except Exception as e:
        return f"Redis error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
