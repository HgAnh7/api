from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

videos = [
    "https://i.imgur.com/H8BnrhM.mp4",
    "https://i.imgur.com/aBcDeFg.mp4",
    "https://i.imgur.com/xYzXwVu.mp4"
]

@app.route("/api/random-video", methods=["GET"])
def random_video():
    return jsonify({
        "video_url": random.choice(videos)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
