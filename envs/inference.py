import os
import json
from openai import OpenAI

# 1. Environment Variables (AS PER CHECKLIST)
# Note: Defaults are only set for BASE_URL and MODEL_NAME
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
HF_TOKEN = os.getenv("HF_TOKEN") # No default for token!

# Optional - if using from_docker_image()
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

# 2. Configure OpenAI Client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_moderation_logic(user_input):
    """
    Standardized logic for content moderation.
    """
    # Required Structured Logging: START
    print(f"START: Processing input for {MODEL_NAME}")
    
    try:
        # Example LLM Call (All calls MUST use the configured client)
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a Trust AI Moderator. Identify PII or malicious links."},
                {"role": "user", "content": user_input}
            ]
        )
        prediction = response.choices[0].message.content
        
        # Required Structured Logging: STEP
        print(f"STEP: Model responded successfully")
        
        return prediction

    except Exception as e:
        print(f"STEP: Error encountered - {str(e)}")
        return "ERROR"
    
    finally:
        # Required Structured Logging: END
        print("END: Moderation task complete")

if __name__ == "__main__":
    test_text = "Sample user content here."
    result = run_moderation_logic(test_text)
    print(f"Final Prediction: {result}")
