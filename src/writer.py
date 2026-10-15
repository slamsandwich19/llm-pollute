# stlib
from collections import deque

# third party
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate


class Writer:
    def write(self, contents: deque) -> None:
        style = ParagraphStyle("Body", fontName="Times-Roman", fontSize=12, leading=15)

        text = "\t"
        for i, item in enumerate(contents):
            if i % 2 == 0:
                text += item
            else:
                text += f'<font name="Courier" size="0.25" color="white">{item}</font>'

        SimpleDocTemplate("output.pdf", pagesize = letter).build(
            [
                Paragraph((text), style)
            ]
        )