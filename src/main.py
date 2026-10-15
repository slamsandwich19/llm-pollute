# stlib
import argparse
from pathlib import Path

# project
from obfuscator import Obfuscator
from src.reader import Reader


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

    def run(self) -> None:
        print(self.args.path)
        raw = self.reader.read_document(self.args.path)
        print(raw)

        polluted = self.obfuscator.obfuscate(raw)
        print(polluted)

if __name__ == "__main__":
    app = App()
    app.run()