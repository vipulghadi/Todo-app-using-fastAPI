from fastapi import Request,FastAPI
from fastapi.exceptions import HTTPException,RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from .api_response import api_response
from .validators import handle_validation_errors

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        print(exc)

        return api_response(
            status_code=exc.status_code,
            message=exc.detail,
            success=False,
            data=None,
            errors=[]
        )

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        print(exc)
        return api_response(
            status_code=422,
            message="Validation error",
            success=False,
            data=None,
            errors=handle_validation_errors(exc)
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        # Unexpected server errors should return 500
        print(exc)
        return api_response(
            status_code=500,
            message="An unexpected error occurred",
            success=False,
            data=None,
            errors=[]
        )




