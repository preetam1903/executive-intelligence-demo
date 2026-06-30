"""
=========================================================
Executive Intelligence Copilot
Chart Inventory Agent
=========================================================

Responsibility:
- Build Executive Chart Inventory
- Assign Chart IDs
- Return chart metadata

This version is a placeholder.

Later it will use grid detection to locate charts.
"""


class ChartInventoryAgent:

    def __init__(self):
        pass

    def process(self, page_info):
        """
        Build Executive Chart Inventory.

        Parameters
        ----------
        page_info : dict

        Returns
        -------
        list
        """

        charts = []

        chart_number = 1

        for page in page_info["pages"]:

            #
            # Temporary:
            # Assume 2 executive charts per page.
            #

            for position in range(2):

                charts.append(

                    {

                        "chart_id": f"CH{chart_number:03}",

                        "page_number": page["page_number"],

                        "position": position + 1,

                        "status": "Detected"

                    }

                )

                chart_number += 1

        return charts
