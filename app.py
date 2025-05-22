from flask import Flask, jsonify
import random

app = Flask(__name__)

# Danh sách video (bạn có thể thêm bao nhiêu tùy ý)
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
    app.run()
