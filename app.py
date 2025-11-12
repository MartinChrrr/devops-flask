from flask import Flask, render_template, jsonify
import json
import os
import utility

app = Flask(__name__)

@app.route('/videos')
def videos():
    videos = utility.get_json("videos.json")
    return render_template("videos.html", videos = videos)

@app.route('/')
def home():
    return "Hello, Flask in Docker!"


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)