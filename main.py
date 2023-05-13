from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user import userRouter
from auth import authRouter
from task import taskRouter
# import uvicorn


# pipreqs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(authRouter , prefix="/auth", tags=["auth"])
app.include_router(taskRouter, prefix="/task", tags=["task"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host='0.0.0.0', port=8900, reload=True)