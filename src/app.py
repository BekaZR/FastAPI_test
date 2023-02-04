from fastapi import FastAPI, Depends
from fastapi.responses import Response

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.dependencies import get_async_session
from src.routers.users import router

def create_app():
    app = FastAPI()
    
    @app.get("/helt_check")
    async def helth_check(session: AsyncSession = Depends(get_async_session)):
        return Response(status_code=200)
    
    app.include_router(router=router)
    return app