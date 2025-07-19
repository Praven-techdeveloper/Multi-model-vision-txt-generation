# Multi-model-vision-txt-generation
Multi-Modal Vision + Text Chatbot
A Streamlit app that ingests an image and a text query, retrieves relevant knowledge from a Wikipedia-based KB or fallback FAQs, generates an answer with a T5 Transformer, and speaks the reply via gTTS.
Features
- Joint image and text embedding using OpenAI’s CLIP
- Retrieval-Augmented Generation (RAG) over a FAISS index
- Answer generation with a pretrained T5 model
- Text-to-speech synthesis with Google gTTS
- Graceful fallback to user-provided FAQ CSV
- Robust handling of missing or corrupted data file
multimodal_chatbot/
├── data/
│   ├── kb/                   
│   └── faq/                   
│
├── scripts/
│   ├── download_wiki.sh       
│   ├── extract_wiki.sh       
│   ├── preprocess_kb.py      
│   └── create_sample_data.py  
│
├── src/
│   ├── encoders.py           
│   ├── retriever.py           
│   ├── generator.py           
│   ├── tts.py               
│   └── app.py                
│
├── requirements.txt          
├── environment.yml            
├── Dockerfile                
└── README.md                 
