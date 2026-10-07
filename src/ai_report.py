import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()


def generate_ai_report(business_report):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found. "
            "Please check your .env file."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a professional business data analyst.

Analyze the sales analytics report below.

Create a concise executive business report containing:

1. Executive Summary
2. Key Findings
3. Product Performance
4. Regional Performance
5. Monthly Performance
6. Business Recommendations

Rules:
- Use only the information provided.
- Do not invent numbers or facts.
- Do not interpret an incomplete current month as a full-month performance.
- If the latest month is incomplete, explicitly mention that its revenue is partial.
- Do not claim seasonality unless the provided data supports a seasonal pattern.
- Distinguish between observed facts and business recommendations.
- Avoid unsupported causal explanations.
- Mention important figures when relevant.
- Make practical business recommendations.
- Write in professional English.
- Focus on actionable insights.
- Do not treat an incomplete current month as a completed month.
- If the latest month is partial, explicitly state that it contains partial data.
- Do not describe the latest partial month as the worst-performing month.
- Do not claim seasonality unless the provided data clearly supports a seasonal pattern.
- Do not invent causes for increases or decreases.
- Clearly distinguish observed facts from recommendations.

SALES ANALYTICS REPORT
======================

{business_report}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as error:
            if "503" in str(error) and attempt < 2:
                print(
                    f"Gemini server is temporarily unavailable. "
                    f"Retrying... ({attempt + 1}/2)"
                )
                time.sleep(5)
            else:
                raise