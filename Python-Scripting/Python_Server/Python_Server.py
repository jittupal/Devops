from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def root():
    return {"Message " : "Hello! From FastAPI!!!"}

@app.get("/sum")
async def sums():
    return {"Sum " : f"{2+2}"}


@app.get("/blogs/comments")
async def read_comments():
    return {"message " : "12345"}


@app.get("/blogs/{blog_id}")
async def read_blogs(blog_id : int, q: int = 0, name: str = ""):
    print(q, name)
    return {"Blog ID :" : blog_id}