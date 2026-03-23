from fastapi import FastAPI
from app.scraper import get_top_posts
from app.caption_writer import generate_caption

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