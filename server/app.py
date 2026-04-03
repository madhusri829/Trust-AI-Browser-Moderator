import uvicorn
from envs.server import app

def main():
    """Main entry point for the OpenEnv validator."""
    uvicorn.run(app, host="0.0.0.0", port=8004)

if __name__ == "__main__":
    main()
