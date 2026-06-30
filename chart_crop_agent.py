"""
=========================================================
Executive Intelligence Copilot
Chart Crop Agent
=========================================================

Responsibility
--------------
Create chart images from the PDF.

Current Version
---------------
Saves the entire page as an image.

Future Version
--------------
Crop individual charts using grid/layout information.
"""

import os
import fitz


class ChartCropAgent:

    def __init__(self, output_folder="output"):

        self.output_folder = output_folder

        os.makedirs(self.output_folder, exist_ok=True)

    def process(self, uploaded_pdf, charts):
        """
        Generate chart images.

        Parameters
        ----------
        uploaded_pdf : Streamlit UploadedFile

        charts : list

        Returns
        -------
        list
        """

        uploaded_pdf.seek(0)
        pdf_bytes = uploaded_pdf.read()

        document = fitz.open(stream=pdf_bytes, filetype="pdf")

        for chart in charts:

            page_number = chart["page_number"] - 1

            page = document.load_page(page_number)

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            image_path = os.path.join(
                self.output_folder,
                f"{chart['chart_id']}.png"
            )

            pix.save(image_path)

            chart["image"] = image_path

        document.close()

        return charts
