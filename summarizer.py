
from news_fetcher import get_news

# Try to load LangChain configuration
try:
    from langchain_config import llm
    LANGCHAIN_AVAILABLE = True
except Exception:
    llm = None
    LANGCHAIN_AVAILABLE = False


def fallback_summary(article):
    """
    Creates a simple summary using the article title
    and description from NewsAPI.
    This works without OpenAI credits.
    """

    title = article.get("title", "")
    description = article.get("description", "")

    title = title.strip() if title else ""
    description = description.strip() if description else ""

    # Remove incomplete ending from NewsAPI description
    if description.endswith("..."):
        description = description[:-3].strip()

    if title and description:
        return (
            f"The article discusses {title}. "
            f"{description}"
        )

    elif description:
        return description

    elif title:
        return f"The article discusses {title}."

    return "No summary available for this article."


def summarize_article(article):
    """
    Generates a summary.

    If OpenAI/LangChain is available, it attempts to use it.
    If the API has no credits or any API error occurs,
    it automatically uses the free fallback summary.
    """

    title = article.get("title", "")
    description = article.get("description", "")

    title = title.strip() if title else ""
    description = description.strip() if description else ""

    # Try LangChain + OpenAI first
    if LANGCHAIN_AVAILABLE and title and description:

        try:
            prompt = f"""
Summarize the following news article in 2 short and simple sentences.

Title:
{title}

Article:
{description}

Give only the summary.
"""

            response = llm.invoke(prompt)

            summary = response.content.strip()

            if summary:
                return summary

        except Exception:
            # OpenAI credits/API unavailable.
            # Use free fallback instead.
            pass

    # Free fallback
    return fallback_summary(article)


def main():

    query = input("Enter your news topic: ")

    if not query.strip():
        print("Please enter a valid topic.")
        return

    articles = get_news(query)

    print(f"\nFound {len(articles)} articles.\n")
    print("=" * 70)

    for i, article in enumerate(articles, start=1):

        print(f"\n{i}. {article.get('title', 'No title')}")

        summary = summarize_article(article)

        print("\nSummary:")
        print(summary)

        print(
            "\nSource:",
            article.get("source", {}).get("name", "Unknown")
        )

        print("URL:", article.get("url", ""))

        print("-" * 70)


if __name__ == "__main__":
    main()

