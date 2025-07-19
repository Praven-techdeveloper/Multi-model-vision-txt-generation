import os, json
from glob import glob

INPUT_DIR  = "data/wiki_extracted"
OUTPUT_PATH = "data/kb/kb_texts.json"
CHUNK_SIZE  = 512
MAX_CHUNKS  = 50000

def chunk_text(text, size=CHUNK_SIZE):
    return [text[i:i+size] for i in range(0, len(text), size)]

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    kb_entries, idx = [], 0

    for fp in glob(f"{INPUT_DIR}/**/*.json", recursive=True):
        for line in open(fp, encoding="utf-8"):
            article = json.loads(line)
            for chunk in chunk_text(article["text"]):
                kb_entries.append({"id": idx, "text": chunk})
                idx += 1
                if idx >= MAX_CHUNKS:
                    break
            if idx >= MAX_CHUNKS:
                break
        if idx >= MAX_CHUNKS:
            break

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        json.dump(kb_entries, out, ensure_ascii=False, indent=2)
    print(f"KB built with {len(kb_entries)} chunks.")
    
if __name__ == "__main__":
    main()