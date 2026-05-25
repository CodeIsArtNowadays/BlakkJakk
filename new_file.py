from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
	title: str


items = []

@app.get('/')
async def index():
	return {'ok': True}

@app.post('/')
async def create_item(item_data: Item):
	items.append(item_data)
	return item_data
	
@app.put('/{item_id}'}
async def update_item(item_id: int, new_item: Item):
	items[item_id-1] = new_item


@app.delete('/{item_id}'}
async def delete_item(item_id: int):
	items.remove(item_id-1)
	return {'status': 'deleted'}

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

@app.get('/factorial')
async def fact_handler(n: Path):
	return fact(n)


@app.get('/multiply')
async def miltiply(a: int, b: int):
	return {'result': a * b}

INFO = 'LONG LONG INFO'

@app.get('/info')
async def index():
	return {'info': INFO}


