import logging

from fastapi import APIRouter


router = APIRouter()

# Configure logging
logger = logging.getLogger(__name__)

# Health-check endpoint
@router.get("/health-check")
def read_root():
    logger.debug("Root endpoint accessed")
    return {"message": "I am OK"}

# Include the user routes
