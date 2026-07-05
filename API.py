import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_listings(product_details):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert Daraz seller who specializes in writing optimized product listings and SEO for the Pakistani market. You understand Daraz search algorithms and what Pakistani buyers search for. Your task is to write an optimized product title for a given product description. The title should be concise, include relevant keywords, and be appealing to Pakistani buyers. Return only the product titles as a numbered list. No explanations, no bullet breakdowns, just the titles."},
            {"role": "user", "content": product_details}
        ]
    )
    return response.choices[0].message.content

