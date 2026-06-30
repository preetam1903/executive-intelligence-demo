"""
=========================================================
Executive Intelligence Copilot
Chart Layout Studio
=========================================================

Responsibility
--------------
Display the layout editor and return crop coordinates.

No cropping.
No AI.
"""

import streamlit as st


class ChartLayoutStudio:

    def __init__(self):
        pass

    def show(self, selected_chart):

        st.divider()

        st.subheader("🟧 Chart Layout Studio")

        col1, col2 = st.columns(2)

        with col1:

            top = st.number_input(
                "Top",
                min_value=0,
                value=100,
                step=5
            )

            left = st.number_input(
                "Left",
                min_value=0,
                value=100,
                step=5
            )

        with col2:

            bottom = st.number_input(
                "Bottom",
                min_value=0,
                value=800,
                step=5
            )

            right = st.number_input(
                "Right",
                min_value=0,
                value=1000,
                step=5
            )

        st.button(
            "Preview Crop",
            type="primary"
        )

        return {

            "top": top,
            "bottom": bottom,
            "left": left,
            "right": right

        }
