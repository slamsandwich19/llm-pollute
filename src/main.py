# stlib
import argparse
from pathlib import Path

# project
from src.obfuscator import Obfuscator
from src.reader import Reader
from src.writer import Writer

class App:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "-p", "--path",
            type = Path,
            help = "Path to the input file"
        )
        self.args = self.parser.parse_args()

        self.obfuscator = Obfuscator()
        self.reader = Reader()
        self.writer = Writer()

    def run(self) -> None:
        raw = self.reader.read_document(self.args.path)
        polluted = self.obfuscator.obfuscate(raw)
        self.writer.write(polluted)

if __name__ == "__main__":
    app = App()
    app.run()