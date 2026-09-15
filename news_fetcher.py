import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise ValueError("NEWS_API_KEY not found in .env file")

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def get_news(query, page_size=5):

    # Fetch more articles first
    response = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="publishedAt",
        page_size=20
    )

    articles = response.get("articles", [])

    # Convert search topic into keywords
    keywords = query.lower().split()

    relevant_articles = []

    for article in articles:

        title = article.get("title") or ""
        description = article.get("description") or ""

        text = (title + " " + description).lower()

        # Count how many keywords are present
        match_count = sum(
            1 for keyword in keywords
            if keyword in text
        )

        if match_count > 0:
            article["relevance_score"] = match_count
            relevant_articles.append(article)

    # Sort by relevance first, then latest articles
    relevant_articles.sort(
        key=lambda x: (
            x.get("relevance_score", 0),
            x.get("publishedAt", "")
        ),
        reverse=True
    )

    # Return only requested number
    return relevant_articles[:page_size]


if __name__ == "__main__":

    query = "Artificial Intelligence"

    articles = get_news(query)

    print(f"\nFound {len(articles)} relevant articles:\n")

    for i, article in enumerate(articles, start=1):

        print(f"{i}. {article.get('title', 'No Title')}")
        print(f"   Source: {article.get('source', {}).get('name', 'Unknown')}")
        print(f"   URL: {article.get('url', '')}")
        print()