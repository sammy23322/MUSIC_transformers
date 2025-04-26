from fastapi import FastAPI
from  transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi.responses import PlainTextResponse

app = FastAPI()

# model_name = "asigalov61/Allegro-Music-Transformer"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# @app.get("/")
# def root():
#     return {"message": "Allegro Music Transformer API is running!"}


# @app.post("/generate")
# def generate_music(prompt: str):
#     input_ids = tokenizer.encode(prompt, return_tensors="pt")
#     output = model.generate(input_ids, max_length=128, do_sample=True)
#     result = tokenizer.decode(output[0], skip_special_tokens=True)
#     return PlainTextResponse(content=result)

@app.get("/")
def root():
    return {"message": "Backend is running (model not loaded yet)."}

@app.post("/generate")
def generate_music(prompt: str):
    # Fake output for now (later we add model)
    return {"generated_music": f"Fake music generated from prompt: {prompt}"}