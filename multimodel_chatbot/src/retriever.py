import os, json, faiss, pandas as pd

def load_kb(path="data/kb/kb_texts.json"):
    if not os.path.isfile(path):
        return [], []
    try:
        raw = open(path, encoding="utf-8").read().strip()
        if not raw:
            return [], []
        kb = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
        return [], []
    texts = [e.get("text", "") for e in kb
             if isinstance(e, dict) and e.get("text")]
    return kb, texts

def load_kb_or_faq(kb_path="data/kb/kb_texts.json",
                   faq_path="data/faq/faq.csv"):
    kb, texts = load_kb(kb_path)
    if texts:
        return kb, texts

    if os.path.isfile(faq_path):
        for enc in ("utf-8", "latin-1"):
            try:
                df = pd.read_csv(faq_path, encoding=enc)
                break
            except UnicodeDecodeError:
                continue
        else:
            return [], []

        faq_kb, faq_texts = [], []
        for idx, row in df.iterrows():
            q = str(row.get("question", "")).strip()
            a = str(row.get("answer", "")).strip()
            if q and a:
                entry = {"id": idx, "text": f"Q: {q}\nA: {a}"}
                faq_kb.append(entry)
                faq_texts.append(entry["text"])
        if faq_texts:
            return faq_kb, faq_texts

    return [], []

def build_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return index

def search_index(index, query_vec, k=5):
    _, ids = index.search(query_vec, k)
    return ids[0]