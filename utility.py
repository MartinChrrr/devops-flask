import json

def get_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        videos = json.load(f)
    return videos

print(get_json("videos.json"))

