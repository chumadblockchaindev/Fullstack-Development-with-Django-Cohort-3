from pydantic import BaseModel

class Post(BaseModel):
    content: str

class PostId(Post):
    id: int
