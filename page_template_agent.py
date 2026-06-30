"""
=========================================================
Executive Intelligence Copilot
Page Template Agent
=========================================================

Responsibility:
- Read uploaded PDF
- Count pages
- Return page information

This agent does NOT detect charts.
This agent does NOT use AI.
"""

import fitz


class PageTemplateAgent:
    """
    Reads the uploaded PDF and returns basic page information.
    """

    def __init__(self):
        pass

    def process(self, uploaded_pdf):
        """
        Process uploaded PDF.

        Parameters
        ----------
        uploaded_pdf : Streamlit UploadedFile

        Returns
        -------
        dict
        """

        # Read uploaded PDF bytes
        pdf_bytes = uploaded_pdf.read()

        # Open PDF
        document = fitz.open(stream=pdf_bytes, filetype="pdf")

        total_pages = document.page_count

        pages = []

        for page_no in range(total_pages):

            page = document.load_page(page_no)

            rect = page.rect

            pages.append(
                {
                    "page_number": page_no + 1,
                    "width": round(rect.width, 2),
                    "height": round(rect.height, 2)
                }
            )

        document.close()

        return {

            "filename": uploaded_pdf.name,

            "total_pages": total_pages,

            "pages": pages

        }
