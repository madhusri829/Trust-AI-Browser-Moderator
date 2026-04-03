from fastapi import FastAPI, Request
from inference import run_moderation_logic

app = FastAPI()

@app.post("/reset")
async def reset():
    return {"status": "success"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    # Handle both "text" or "input" keys just in case
    user_input = data.get("text") or data.get("input") or ""
    
    # Run your moderation logic
    result = run_moderation_logic(user_input)
    
    # CRITICAL: The key must be "prediction"
    return {"prediction": result}
