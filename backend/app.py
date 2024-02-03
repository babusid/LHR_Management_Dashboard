from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    '''test method'''
    #todo send the static html index file
    return {'message': 'Hello World from FastAPI!'}

