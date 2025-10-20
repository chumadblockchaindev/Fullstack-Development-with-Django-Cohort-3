from pydantic import BaseModel

class Post(BaseModel):
    content: str

class PostId(Post):
    id: int

class Comment(BaseModel):
    comment: str

class CommentId(Comment):
    id: int

class PostWithComments(BaseModel):
    post: PostId
    comments: list[CommentId]



