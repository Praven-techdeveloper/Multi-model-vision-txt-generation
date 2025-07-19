import streamlit as st
from PIL import Image
import numpy as np

from encoders  import embed_image, embed_text
from retriever import load_kb_or_faq, build_index, search_index
from generator import generate_response
from tts       import synthesize_voice

st.set_page_config(page_title="Multi-Modal Chatbot", layout="wide")

@st.cache_data(show_spinner=False)
def init_kb():
    kb, texts = load_kb_or_faq()
    if not texts:
        st.error(
            "No KB or FAQ found. Populate data/kb/kb_texts.json "
            "or data/faq/faq.csv and rerun."
        )
        st.stop()
    embs     = embed_text(texts)
    faiss_ix = build_index(embs)
    return kb, texts, faiss_ix

kb_entries, kb_texts, faiss_idx = init_kb()

st.title("🖼️📖 Multi-Modal Vision + Text Chatbot")
col1, col2 = st.columns(2)

with col1:
    img_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
with col2:
    query = st.text_input("Enter your question:")

if img_file and query:
    image = Image.open(img_file).convert("RGB")
    st.image(image, use_column_width=True)

    img_vec   = embed_image(image)
    txt_vec   = embed_text([query])
    img_norm  = img_vec / np.linalg.norm(img_vec)
    txt_norm  = txt_vec / np.linalg.norm(txt_vec)
    q_vec     = img_norm + txt_norm

    ids       = search_index(faiss_idx, q_vec, k=5)
    context   = " ".join(kb_texts[i] for i in ids)

    with st.spinner("Generating…"):
        answer = generate_response(context, query)
    st.subheader("Answer")
    st.write(answer)

    with st.spinner("Synthesizing voice…"):
        audio_path = synthesize_voice(answer)
    st.audio(audio_path, format="audio/mp3")

    feedback = st.radio("Helpful?", ("👍 Yes", "👎 No"))
    if st.button("Submit Feedback"):
        st.success("Thanks for your feedback!")