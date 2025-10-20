from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.models import Post, PostId, Comment, CommentId, PostWithComments


origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

post_db = {
    0: {"id": 0, "content": "Hello, world!"},
    1: {"id": 1, "content": "My second post."},
    2: {"id": 2, "content": "FastAPI is awesome!"},
}


def find_post(post_id: int):
    if post_id not in post_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_db[post_id]


@app.post("/post", response_model=PostId)
async def create_post(post: Post):
    body = post.dict()
    if body["content"] == "":
        raise HTTPException(status_code=400, detail="Content cannot be empty")

    post_id = len(post_db)
    post_db[post_id] = {**body, "id": post_id}
    return post_db[post_id]


@app.get("/posts", response_model=list[PostId])
async def get_posts():
    return list(post_db.values())


@app.get("/post/{post_id}", response_model=PostId)
async def get_one_post(post_id: int):
    if post_id not in post_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_db[post_id]


@app.delete("/post/{post_id}", response_model=PostId)
async def delete_post(post_id: int):
    if post_id not in post_db:
        raise HTTPException(status_code=404, detail="Post not found")

    post = post_db.pop(post_id)
    return post


@app.put("/post/{post_id}", response_model=PostId)
async def update_post(post_id: int, post: Post):
    if post_id not in post_db:
        raise HTTPException(status_code=404, detail="Post not found")

    body = post.dict()
    if body["content"] == "":
        raise HTTPException(status_code=400, detail="Content cannot be empty")

    # post_db[post_id] = {**body, "id": post_id} # alternative way
    post_db[post_id].update(body)
    return post_db[post_id]


@app.post("/post/{post_id}/comment", response_model=CommentId)
async def create_comment_for_post(post_id: int, comment: Comment):
    body = comment.dict()
    if body["comment"] == "":
        raise HTTPException(status_code=400, detail="Content cannot be empty")

    post = find_post(post_id)
    post_comments = post.get("comments", [])
    comment_id = len(post_comments)
    post_comments.append({**body, "id": comment_id})
    post["comments"] = post_comments
    return {"id": comment_id, **body}

@app.get("/post/{post_id}/comment", response_model=list[CommentId])
async def get_comments_for_post(post_id: int):
    post = find_post(post_id)
    return post.get("comments", [])


@app.get("/post/{post_id}/comments", response_model=PostWithComments)
async def get_comments_with_post(post_id: int):
    post = find_post(post_id)    
    comments = await get_comments_for_post(post_id)
    
    return {"post": post, "comments": comments}

