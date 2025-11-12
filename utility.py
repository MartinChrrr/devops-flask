import json

def get_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        videos = json.load(f)
    return videos

videos = get_json("videos.json")
for video in videos:
    if video['id'] == 1:
        print("super")
    print((video['id']))
