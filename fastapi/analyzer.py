import google.generativeai as genai

genai.configure(api_key="AIzaSyD5uAx8bNuZR067PyDqRLVIQCAnhfCee8M")

async def analyze_with_llm(sector: str, news: str) -> dict:
    prompt = f"""
You are a market expert. Based on this recent news about the {sector} sector in India, write a markdown-formatted trade opportunity report.

### Format:

# Market Analysis Report: {sector}
## Summary
(Summary paragraph)

## Key Insights
- (3 bullet points)

## Trade Opportunities
- (2 bullet points with title, gain %, risk level)

News:
{news}
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return {
        "report": response.text  # ✅ This key must exist
    }
