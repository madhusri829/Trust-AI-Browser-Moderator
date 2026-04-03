from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="TrustAI Moderator",
    description="Transparent and Secure AI-driven browser moderator."
)

# Enable CORS for dashboard accessibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Internal State tracking
env_state = {
    "spam_count": 0,
    "status": "TRUST_INITIALIZED",
    "verified": True
}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "trust-ai-moderator"}

@app.post("/step")
async def step(request: Request):
    data = await request.json()
    action = data.get("action")
    content = data.get("input", "")
    reward = 0.0

    # Trust AI Logic: Privacy-First Scan
    if action == "run_deep_scan":
        # Detection logic for PII (@) or Links (http)
        if "@" in content or "http" in content:
            env_state["status"] = "FLAGGED_UNTRUSTED"
            env_state["spam_count"] += 1
            reward = 1.0
        else:
            env_state["status"] = "VERIFIED_SAFE"
            reward = 0.5
    
    return {
        "observation": env_state,
        "reward": reward,
        "done": False,
        "identity": "TrustAI-Agent-v1"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8004)