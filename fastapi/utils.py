def generate_markdown_report(sector: str, data: dict) -> str:
    md = f"# Market Analysis Report: {sector.capitalize()}\n\n"
    md += f"## Summary\n{data['summary']}\n\n"
    md += "## Key Insights\n"
    for insight in data["insights"]:
        md += f"- {insight}\n"
    md += "\n## Trade Opportunities\n"
    for opp in data["opportunities"]:
        md += f"- **{opp['title']}**: Gain = {opp['gain']}, Risk = {opp['risk']}\n"
    return md
