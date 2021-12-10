# imports
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#instantiation of APIrouter
router = APIRouter()
#instantiation of jinja templates folder
templates = Jinja2Templates(directory="templates/")


@router.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    tag = "flower"
    result = "Type a number"
    return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result, 'tag': tag})


@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):
#indicate that we want a to use accordion.html as template response et send context information to it -request result and tag
    return templates.TemplateResponse('accordion.html', context={'request': request, 'tag': tag})
