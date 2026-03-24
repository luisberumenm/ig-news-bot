from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.scraper import get_top_posts
from app.caption_writer import generate_caption
from app.image_generator import generate_image

app = FastAPI()
templates = Jinja2Templates(directory="templates")

current_post = {}

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
    return {"post_title": post["title"], "caption": caption}

@app.get("/generate-image")
def image():
    posts = get_top_posts()
    post = posts[0]
    image_path = generate_image(post)
    return FileResponse(image_path, media_type="image/png")

@app.get("/image")
def serve_image():
    return FileResponse("generated_images/latest_post.png", media_type="image/png")

@app.get("/approval", response_class=HTMLResponse)
def approval(request: Request):
    global current_post
    posts = get_top_posts()
    post = posts[0]
    caption = generate_caption(post)
    generate_image(post)
    current_post = {"title": post["title"], "caption": caption}
    return templates.TemplateResponse("approval.html", {
        "request": request,
        "post_title": post["title"],
        "caption": caption
    })

@app.post("/approve")
async def approve(request: Request):
    data = await request.json()
    caption = data.get("caption")
    print(f"✅ APPROVED POST")
    print(f"Caption: {caption}")
    return {"message": "Post approved! Ready for Instagram publishing in Phase 6."}

@app.post("/reject")
def reject():
    print("❌ Post rejected")
    return {"message": "Post rejected. Generate a new one by visiting /approval again."}