"""
=========================================================
Executive Intelligence Copilot
Repository Agent
=========================================================

Responsibility
--------------
Build the Executive Repository.

This agent does NOT:
- Save files
- Query AI
- Display UI

It only builds the repository object.
"""


class RepositoryAgent:

    def __init__(self):
        pass

    def process(self, charts):
        """
        Build Executive Repository.

        Parameters
        ----------
        charts : list

        Returns
        -------
        dict
        """

        repository = {

            "repository_name": "Executive Intelligence Repository",

            "version": "1.0",

            "total_charts": len(charts),

            "charts": []

        }

        for chart in charts:

            repository["charts"].append({

                "chart_id": chart["chart_id"],

                "page_number": chart["page_number"],

                "position": chart["position"],

                "image": chart.get("image"),

                "chart_title": chart["chart_title"],

                "chart_type": chart["chart_type"],

                "business_area": chart["business_area"],

                "metric": chart["metric"],

                "summary": chart["summary"],

                "confidence": chart["confidence"]

            })

        return repository
