from flask import Flask, render_template, jsonify, request
import json
import os
import utility

app = Flask(__name__)

@app.route('/videos')
def videos():
    videos = utility.get_json("videos.json")
    return render_template("videos.html", videos = videos)

@app.route('/get/video')
def get_video():
    id = request.args.get('id')
    if not id:
        return jsonify({"error": "Missing id parameter"}), 400
    videos = utility.get_json("videos.json")
    for v in videos:
        if v['id'] == int(id):
            video = v 
    return render_template("video_details.html", video=video)

@app.route('/put/video', methods=['POST'])
def edit_video():
    #get id and check if id is missing
    id = request.args.get('id')
    if not id:
        return jsonify({"error": "Missing id parameter"}), 400
    
    #get video and check if video_id is in videos
    videos = utility.get_json("videos.json")
    for v in videos:
        if v['id'] == int(id):
            video = v 
    if not video:
        return jsonify({"error": "Video not found"}), 404
    #end
    
    new_title = request.form.get('title')
    new_url = request.form.get('url')
    new_views = request.form.get('views', type=int)

    if new_title:
        video['title'] = new_title
    if new_url:
        video['url'] = new_url
    if new_views is not None:
        video['views'] = new_views

    # Sauvegarde
    utility.write_json("videos.json",videos)

    return render_template("edit_video.html", video=video)

@app.route('/')
def home():
    return "Hello, Flask in Docker!"


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)