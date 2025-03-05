from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from app.api.v1 import ChatRouter, UsersRouter
from app.auth import AuthRouter, get_current_user
from app.core.database import init_db

init_db()

app = FastAPI(
        title="TravelSynk API",
        description="Personalized AI Chat-bot",
        version="1.0.0"
    )


app.include_router(AuthRouter,prefix="/auth", tags=["Authentication"])
app.include_router(ChatRouter, tags=["Chat"], dependencies=[Depends(get_current_user)])
app.include_router(UsersRouter, tags=["Users"])



@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
