import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException

from .logger import setup_logging


def setup_auto_logger(
    app: FastAPI,
    logfile: str | None = None
):
    setup_logging(logfile)
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        logging.error(str(exc))
        return JSONResponse(
            status_code=400,
            content={"detail": exc.errors()},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        logging.error(str(exc))
        return JSONResponse(content={'detail': str(exc)}, status_code=exc.status_code)

    @app.exception_handler(Exception)
    async def server_exception_handler(request, exc):
        logging.exception(str(exc))
        return JSONResponse(content={'detail': 'Internal server error'}, status_code=500)