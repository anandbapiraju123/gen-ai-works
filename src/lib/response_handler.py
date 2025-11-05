from pip._internal import configuration
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Optional, Union, Dict, Any, List


class SuccessResponse(BaseModel):
    status: int
    message: str
    data: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None


class FailureResponse(BaseModel):
    status: int
    message: str

    @staticmethod
    def from_exception(exception: Exception, status: int = 500):
        return JSONResponse(
            content={
                "status": status,
                "message": str(exception),
            },
            status_code=status,
        )
