from fastapi import APIRouter, Request, Depends
from starlette.templating import Jinja2Templates

from book.router import get_book

router = APIRouter(
    prefix='/pages',
    tags=['pages']
)

templates = Jinja2Templates(directory='templates')


@router.get('/index')
def get_base_page(request:Request):
    return templates.TemplateResponse('base.html',{'request':request})


@router.get('/search/{name_book}')
def get_search_page(request:Request,records=Depends(get_book)):
    return templates.TemplateResponse('search.html',{'request': request,'books':records})