from fastapi import FastAPI, Request
from inference import run_moderation_logic

app = FastAPI()

@app.post("/reset")
async def reset():
    return {"status": "success"}

@app.post("/predict")
async def predict(request: Request):
    try:
        # 1. Get the data from the grader
        data = await request.json()
        # The grader usually sends the key "text" or "input"
        user_input = data.get("text") or data.get("input", "")
        
        # 2. Run your moderation logic
        prediction = run_moderation_logic(user_input)
        
        # 3. Return the EXACT key the grader looks for
        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}, 500
