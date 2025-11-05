from src.app import app
import uvicorn
import os

if __name__ == "__main__":
    uvicorn.run(app, port=int(os.getenv('PORT')), reload=True)
