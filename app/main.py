from fastapi import FastAPI
from .routers import business, crypto, users

app = FastAPI()

#app.include_router(business.router)
#app.include_router(crypto.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Connecting crypto friendly businesses with crypto fanatic people"}