# stlib
from collections import deque

# third party
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

# project
from src.obfuscator import Entry


class Writer:
    def write(self, contents: deque[Entry]) -> None:
        style = ParagraphStyle(
            "Body", fontName = "Times-Roman", fontSize = 12, leading = 28,
            firstLineIndent = 36
        )

        lines = [""]
        for entry in contents:
            if entry.flag == Entry.ORIGINAL:
                first, *other = entry.content.split("\n")
                lines[-1] += first
                lines.extend(other)
            else:
                lines[-1] += f'<font name="Courier" size="0.25" color="white">{entry.content}</font>'

        story = [
            Paragraph(line, style) if line else Spacer(1, style.leading)
            for line in lines
        ]

        SimpleDocTemplate("src/assets/output.pdf", pagesize = letter).build(story)