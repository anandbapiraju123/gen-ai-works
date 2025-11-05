import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    AZURE_OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
    OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
    AZURE_DEPLOYMENT_NAME= os.getenv("AZURE_DEPLOYMENT_NAME")

    #Figma creds
    FIGMA_TOKEN=os.getenv("FIGMA_TOKEN")


settings = Settings()