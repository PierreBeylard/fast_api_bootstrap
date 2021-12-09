from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .library.helpers import *
from .routers import twoforms, unsplash, accordion

app = FastAPI()

#les routers permettent de pointer vers différents fichiers
#https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(unsplash.router)
app.include_router(twoforms.router)
app.include_router(accordion.router)
#Import Jinja2Templates and set the template directory templates.
templates= Jinja2Templates(directory="templates")
#mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")
#Request as a parameter & as a returned value.
# Specify the response_class to HTMLResponse.
# Return templates.TemplateResponse() with the page HTML and data

@app.get("/", response_class= HTMLResponse)
async def home(request : Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html",{"request":request,"data": data})


@app.get("/page/{page_name}", response_class= HTMLResponse)
async def page(request : Request, page_name: str):
    data = openfile(page_name+".md")
    return templates.TemplateResponse("page.html", {"request": request,"data": data})
