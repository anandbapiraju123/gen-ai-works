import logging

from openai import AzureOpenAI

from ...src.config.configuration import settings


class LLM:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            azure_deployment=settings.AZURE_DEPLOYMENT_NAME,
            api_version=settings.AZURE_OPENAI_API_VERSION,
            api_key=settings.AZURE_OPENAI_API_KEY,
        )
        self.logger = logging.getLogger(__name__)

