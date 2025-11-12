import json

def get_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json(path: str, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# videos = get_json("videos.json")
# for video in videos:
#     if video['id'] == 1:
#         print("super")
#     print((video['id']))
