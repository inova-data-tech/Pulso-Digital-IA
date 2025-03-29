from fastapi import FastAPI

app = FastAPI()
app.include_router(string_proc_router)