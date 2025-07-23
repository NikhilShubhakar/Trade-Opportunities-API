from pydantic import BaseModel

class MarkdownReport(BaseModel):
    sector: str
    report: str
