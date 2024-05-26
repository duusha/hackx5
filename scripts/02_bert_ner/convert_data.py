import json 
with open("train.json", "r", encoding="utf-8") as f:
    data = json.load(f)
with open("new_data.jl", "w", encoding="utf-8") as f:
    for entry in data:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

