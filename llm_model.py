import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

#google/flan-t5-small
#TinyLlama/TinyLlama-1.1B-Chat-v1.0
def load_mistral_model(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
    token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    tokenizer=AutoTokenizer.from_pretrained(model_id,use_auth_token=token)

    #load model with CPU settings
    model=AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float32, #use full precision for CPU
        device_map=None,
        use_auth_token=token
    )

    pipe=pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1,
        max_new_tokens=512
    )

    return pipe

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def load_flan_model(model_id="google/flan-t5-small"):
    model_id = "google/flan-t5-small"
    token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    tokenizer = AutoTokenizer.from_pretrained(model_id,use_auth_token=token)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id,
        torch_dtype=torch.float32, #use full precision for CPU
        device_map=None,
        use_auth_token=token
        )

    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float32,
        device=-1,  # CPU
    )
    return pipe