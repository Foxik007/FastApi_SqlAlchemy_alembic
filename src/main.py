
from fastapi import FastAPI, Depends
from starlette.staticfiles import StaticFiles

from pages.router import router as router_pages
from book.router import router as router_book

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)
app.include_router(router_book)
