
from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import Book
from schemas import Book_schema


router = APIRouter(
    prefix='/book',
    tags=['book']
)

#=======CRUD=======

#Добавление книги
@router.post('/')
async def post_book(Book_schem:Book_schema,session:AsyncSession = Depends(get_async_session)):
    stmt = insert(Book).values(**Book_schem.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status":'success'}


#Вывести книги где цена больше указанной
@router.get('/')
async def get_book(name_book:str,session:AsyncSession = Depends(get_async_session)):
    query = select(Book).where(Book.name_book == name_book )
    result = await session.execute(query)
    return result.scalars().all()


#Удаление товара по ID
@router.delete('/book/{book_id}')
async def delete_book(book_id:int,session:AsyncSession = Depends(get_async_session)):
    query = delete(Book).where(Book.id == book_id)
    await session.execute(query)
    await session.commit()
    return {'status':'Book deleted'}



#Изменяет название книги
@router.put('/book/{book_name}')
async def put_book(book_name:str,new_book_name:str,session:AsyncSession = Depends(get_async_session)):
    if Book.name_book == book_name:
        stmt = update(Book).where(Book.name_book == book_name).values(name_book=new_book_name)
        await session.execute(stmt)
        await session.commit()
        return {'status':'Book update',
                'new name book':new_book_name}
    else:
        return 'Название книги не найдено'
