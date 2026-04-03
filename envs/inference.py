import os
import json
from openai import OpenAI

# 1. ENVIRONMENT VARIABLES (Satisfies Screenshots 1 & 2)
# Defaults are set ONLY for API_BASE_URL and MODEL_NAME
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
# HF_TOKEN has NO default value (Satisfies Screenshot 195501)
HF_TOKEN = os.getenv("HF_TOKEN") 

# Optional variable for Docker-based deployments
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME")

# 2. CONFIGURE OPENAI CLIENT (Satisfies Screenshot 3)
# All LLM calls MUST use this configured client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_moderation_logic(user_input):
    """
    Core logic for the Trust AI Browser Moderator.
    Detects PII and malicious intent in browser content.
    """
    # 3. STRUCTURED LOGGING: START (Satisfies Screenshot 195506)
    print(f"START: Processing input for {MODEL_NAME}")
    
    try:
        # 4. LLM CALL VIA OPENAI CLIENT
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a Trust AI Moderator. Identify PII or malicious links. "
                               "Respond with 'SAFE' or 'UNSAFE' and a brief reason."
                },
                {"role": "user", "content": user_input}
            ]
        )
        prediction = response.choices[0].message.content
        
        # 5. STRUCTURED LOGGING: STEP
        print(f"STEP: Model inference completed successfully")
        
        return prediction

    except Exception as e:
        # 6. STRUCTURED LOGGING: STEP (Error case)
        print(f"STEP: Error encountered - {str(e)}")
        return f"MODERATION_ERROR: {str(e)}"
    
    finally:
        # 7. STRUCTURED LOGGING: END
        print("END: Moderation task complete")

# Standalone execution block for testing
if __name__ == "__main__":
    test_text = "Please visit http://malicious-site.com or email me at user@example.com"
    result = run_moderation_logic(test_text)
    print(f"\n--- Final Result ---\n{result}")
