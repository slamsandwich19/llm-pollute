# third party
from docx import Document


class Reader:
    def read_document(self, path: str) -> str:
        """
        Reads the raw text from a .docx file and returns the contents as a string

        Args:
            path (str): This represents the path to the file.

        Returns:
            str: This represents the raw contents of the file.
        """
        document = Document(path)
        return "\n".join(paragraph.text for paragraph in document.paragraphs)
