import os
import requests

def web_search(query: str, num_results=3) -> str:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "❌ SerpAPI key is missing."

    params = {
        "q": query,
        "api_key": api_key,
        "num": num_results,
        "engine": "google"
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        if "organic_results" not in data:
            return "❌ No search results found."

        results = data["organic_results"]
        snippets = [r.get("snippet", "") for r in results if "snippet" in r]
        return "\n\n".join(snippets)

    except Exception as e:
        return f"❌ Web search error: {e}"
