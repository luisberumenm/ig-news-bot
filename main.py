from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.scraper import get_top_posts
from app.caption_writer import generate_caption
from app.image_generator import generate_image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from ig-news-bot!"}

@app.get("/scrape/{subreddit}")
def scrape(subreddit: str):
    posts = get_top_posts()
    return {"subreddit": subreddit, "posts": posts}

@app.get("/generate-caption")
def caption():
    posts = get_top_posts()
    post = posts[0]
    caption = generate_caption(post)
    return {
        "post_title": post["title"],
        "caption": caption
    }

@app.get("/generate-image")
def image():
    posts = get_top_posts()
    post = posts[0]
    image_path = generate_image(post)
    return FileResponse(image_path, media_type="image/png")