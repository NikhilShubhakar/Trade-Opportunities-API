from fastapi import FastAPI, HTTPException, Path
from fastapi.security import HTTPBearer
from limiter import RateLimitMiddleware
from collector import fetch_sector_news
from analyzer import analyze_with_llm
from models import MarkdownReport

app = FastAPI()
app.add_middleware(RateLimitMiddleware)
auth_scheme = HTTPBearer()

@app.get("/analyze/{sector}", response_model=MarkdownReport)
async def analyze_sector(
    sector: str = Path(..., min_length=3),
    # user=Depends(verify_token),
):
    try:
        news_data = await fetch_sector_news(sector)
        analysis = await analyze_with_llm(sector, news_data)

        # ✅ Directly return the markdown from Gemini response
        return {
            "sector": sector,
            "report": analysis["report"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
