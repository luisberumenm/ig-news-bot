import openai
import requests
import os
from app.config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_image(post: dict) -> str:
    prompt = f"""A vibrant, exciting LEGO promotional image for this news:
{post['title']}

Style: Bright, colorful LEGO aesthetic. Dramatic lighting.
Collector/fan appeal. No text overlays. Square format."""

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = response.data[0].url

    os.makedirs("generated_images", exist_ok=True)
    image_path = "generated_images/latest_post.png"

    image_data = requests.get(image_url).content
    with open(image_path, "wb") as f:
        f.write(image_data)

    return image_path