import torch
from safetensors.torch import save_file
import os

# Directory of original HF checkpoint
SRC_DIR = "checkpoints/my_model"
OUT_DIR = "checkpoints/my_model_safetensors"
os.makedirs(OUT_DIR, exist_ok=True)

# Iterate all .bin files in SRC_DIR
for fname in os.listdir(SRC_DIR):
    if fname.endswith(".bin") or fname.endswith(".pt"):
        src_path = os.path.join(SRC_DIR, fname)
        out_path = os.path.join(
            OUT_DIR, fname.rsplit(".", 1)[0] + ".safetensors"
        )
        print(f"Converting {src_path} → {out_path}")
        sd = torch.load(src_path, map_location="cpu")
        save_file(sd, out_path)
print("Conversion complete.")