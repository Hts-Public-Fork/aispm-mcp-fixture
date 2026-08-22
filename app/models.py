"""A real HuggingFace model id, loaded the way model ids are actually loaded."""
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModel.from_pretrained("meta-llama/Llama-2-7b-hf")
