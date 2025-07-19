import os
from transformers import T5Tokenizer, T5ForConditionalGeneration
from safetensors.torch import load_file

tokenizer = T5Tokenizer.from_pretrained("t5-base")
SF_PATH = "checkpoints/my_model_safetensors/pytorch_model.safetensors"

if os.path.exists(SF_PATH):
    state_dict = load_file(SF_PATH)
    model = T5ForConditionalGeneration.from_pretrained(
        "t5-base", state_dict=state_dict
    )
else:
    model = T5ForConditionalGeneration.from_pretrained("t5-base")

def generate_response(context: str, question: str,
                      max_length: int = 128) -> str:
    prompt = f"Context: {context}\nQuestion: {question}"
    enc = tokenizer(prompt, return_tensors="pt",
                    padding=True, truncation=True)
    out = model.generate(**enc, max_length=max_length, num_beams=5)
    return tokenizer.decode(out[0], skip_special_tokens=True)