from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import utility

app = Flask(__name__)

@app.route('/videos')
def videos():
    videos = utility.get_json("videos.json")
    return render_template("videos2.html", videos = videos)

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

@app.route('/put/video', methods=['GET','POST'])
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

@app.route('/add', methods=['POST'])
def add_video():
    videos = utility.get_json("videos.json")
    last_id = 0
    for video in videos:
        if last_id <= video['id']:
            last_id = video['id']
    next_id = id + 1
    new_title = request.form.get('title')
    new_url = request.form.get('url')
    new_views = request.form.get('views', type=int)
    utility.write_json("videos.json",videos)
    return render_template("add_video.html", video=video)

@app.route('/delete', methods=['POST'])
def delete_video():
    id = request.args.get('id', type=int)
    if not id:
        return jsonify({"error": "Missing id parameter"}), 400

    videos = utility.get_json("videos.json")

    # Find the video to delete
    video_to_delete = None
    for v in videos:
        if v['id'] == id:
            video_to_delete = v
            break

    if not video_to_delete:
        return jsonify({"error": "Video not found"}), 404

    # delete the video
    videos.remove(video_to_delete)

    # json file saved
    utility.write_json("videos.json", videos)

    return redirect(url_for('videos'))


@app.route('/')
def home():
    return "Hello, Flask in Docker!"


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)