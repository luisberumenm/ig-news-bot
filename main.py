from fastapi import FastAPI
from app.scraper import get_top_posts

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from ig-news-bot!"}

@app.get("/scrape/{subreddit}")
def scrape(subreddit: str):
    posts = get_top_posts()
    return {"subreddit": subreddit, "posts": posts}