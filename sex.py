from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

videos = [
    "https://i.imgur.com/7Ga5xaZ.mp4",
    "https://i.imgur.com/abcdefj.mp4",
]

@app.route("/api/sex", methods=["GET"])
def sex():
    return jsonify({
        "video_url": random.choice(videos)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)