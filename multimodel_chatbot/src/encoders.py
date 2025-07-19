from transformers import CLIPProcessor, CLIPModel

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

def embed_image(image):
    inputs = processor(images=image, return_tensors="pt")
    feats = clip_model.get_image_features(**inputs)
    return feats.detach().cpu().numpy()

def embed_text(texts: list):
    inputs = processor(text=texts, return_tensors="pt",
                       padding=True, truncation=True)
    feats = clip_model.get_text_features(**inputs)
    return feats.detach().cpu().numpy()