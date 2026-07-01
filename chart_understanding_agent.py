
"""
=========================================================
Executive Intelligence Copilot
Chart Understanding Agent
=========================================================

Responsibility
--------------
Understand the business meaning of each chart.

Current Version:
- Placeholder implementation.

Future Version:
- GPT Vision
- Chart reasoning
- Executive summary generation
"""
import json
import base64
from openai import OpenAI
import streamlit as st

class ChartUnderstandingAgent:

    def __init__(self):

        self.client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

    def encode_image(self, image_path):
        """
        Convert image to Base64 for GPT Vision.
        """

        with open(image_path, "rb") as image_file:

            return base64.b64encode(
                image_file.read()
            ).decode("utf-8")

    def understand_page(self, image_path):

        base64_image = self.encode_image(image_path)

        prompt = """
    You are an Executive Manufacturing Intelligence Agent.

    The image contains an executive dashboard page with multiple charts.

    Identify every chart on the page.

    Return ONLY valid JSON.

    {
        "charts":[
            {
                "chart_id":"",
                "chart_title":"",
                "chart_type":"",
                "business_area":"",
                "metric":"",
                "summary":"",
                "confidence":0.0
            }
        ]
    }

    Rules

    - One object per chart.
    - Do not analyse numerical values.
    - Do not analyse X axis.
    - Do not analyse legends.
    - Do not guess.
    - Return JSON only.
    """

        response = self.client.chat.completions.create(

            model="gpt-4.1",

            response_format={"type":"json_object"},

            messages=[

                {

                    "role":"user",

                    "content":[

                        {
                            "type":"text",
                            "text":prompt
                        },

                        {

                            "type":"image_url",

                            "image_url":{

                                "url":f"data:image/png;base64,{base64_image}"

                            }

                        }

                    ]

                }

            ]

        )

        return json.loads(
            response.choices[0].message.content
        )

    def understand_chart(self, image_path):

        base64_image = self.encode_image(image_path)

        prompt = """
    You are an Executive Manufacturing Intelligence Agent.

    Analyse the chart image.

    Return ONLY valid JSON.

    {
        "chart_type":"",
        "chart_title":"",
        "business_area":"",
        "metric":"",
        "x_axis":"",
        "left_y_axis":"",
        "right_y_axis":"",
        "legend":[],
        "summary":"",
        "missing_information":[],
        "confidence":0.0
    }

    Rules:

    - Return JSON only.
    - No markdown.
    - No explanation.
    - Confidence must be between 0 and 1.
    - If information is unavailable, use empty string or empty array.
    """

        response = self.client.chat.completions.create(

            model="gpt-4.1",

            response_format={"type": "json_object"},

            messages=[

                {
                    "role": "user",

                    "content": [

                        {
                            "type": "text",
                            "text": prompt
                        },

                        {
                            "type": "image_url",

                            "image_url": {

                                "url": f"data:image/png;base64,{base64_image}"

                            }

                        }

                    ]

                }

            ]

        )

        return json.loads(
            response.choices[0].message.content
        )

    #############

    def process(self, charts):

        if len(charts) == 0:
            return charts

    # ----------------------------------------
    # Analyse the PAGE only once
    # ----------------------------------------

        page_understanding = self.understand_page(
            charts[0]["image"]
        )

        ai_charts = page_understanding.get("charts", [])

    # ----------------------------------------
    # Copy AI results into inventory
    # by position (CH001 = first chart, etc.)
    # ----------------------------------------

        for chart, ai_chart in zip(charts, ai_charts):

            chart["chart_type"] = ai_chart.get(
                "chart_type",
                ""
            )

            chart["chart_title"] = ai_chart.get(
                "chart_title",
                ""
            )

            chart["business_area"] = ai_chart.get(
                "business_area",
                ""
            )

            chart["metric"] = ai_chart.get(
                "metric",
                ""
            )

            chart["summary"] = ai_chart.get(
                "summary",
                ""
            )

            chart["confidence"] = ai_chart.get(
                "confidence",
                0.0
            )

        return charts
