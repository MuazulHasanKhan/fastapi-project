from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


# to register the exceptions, they needs to be linked to the app instance, so we can create a function to register them
def register_exception_handlers(app: FastAPI):
    @app.add_exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500, content = {'detail': str(exc)}
        )