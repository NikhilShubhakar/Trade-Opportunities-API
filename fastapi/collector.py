import httpx

async def fetch_sector_news(sector: str) -> str:
    url = "https://api.duckduckgo.com/"
    params = {
        "q": f"{sector} sector India news",
        "format": "json",
        "no_html": 1,
        "skip_disambig": 1,
    }

    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        data = r.json()
        return data.get("AbstractText", "No relevant data found.")
