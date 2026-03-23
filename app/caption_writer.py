import anthropic
from app.config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_caption(post: dict) -> str:
    prompt = f"""You are a creative Instagram content writer for a Lego news and leaks page.

Based on this Reddit post about a Lego leak or news:
Title: {post['title']}
Details: {post['selftext']}

Write an engaging Instagram caption that includes:
- An exciting opening line
- 2-3 sentences summarizing the news
- A question to encourage engagement
- 10 relevant hashtags

Keep the tone enthusiastic and fun, aimed at Lego fans."""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text