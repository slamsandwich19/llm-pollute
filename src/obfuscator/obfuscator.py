# stlib
import random
from collections import deque

# project
from src.obfuscator.entry import Entry
from src.obfuscator.word_dict import WordDictionary


class Obfuscator:
    def __init__(self, buffer_size: int) -> None:
        self.word_dict = WordDictionary(buffer_size)

    def generate_garbage(self, length: int) -> str:
        """
        Generates random words separated by spaces within the size limits provided.

        NOTE - Words near the end are more likely to be shorter and punctuation is less
            likely to appear given the nature of the implementation.

        Args:
            length (int): Represents the desired length of the output.

        Returns:
            str: Represents the output string.
        
        >>> obfuscator.generate_garbage(10)
        ' or has a '
        >>> obfuscator.generate_garbage(20)
        ' at a that how here '
        >>> obfuscator.generate_garbage(50)
        '. After I us, right should place day. All course not '
        """
        output = ""
        available_space = length - 2 # subtract 2 for spaces at the front and back

        while available_space > 0:
            #print(f"{available_space}, {len(output)}: {repr(output)}")

            # clamp the word length between the available space and the max word length
            word_length = random.randint(1, min(available_space, self.word_dict.MAX_LENGTH))
            modifier_roll = random.randint(1, 100)

            # if the word is one character short then extend it to prevent double spaces unless the max length is reached
            if available_space - word_length == 1:
                word_length = word_length + 1 if word_length != self.word_dict.MAX_LENGTH else word_length - 1

            available_space -= word_length

            # add commas 7% of the time
            if available_space > 2 and modifier_roll < 8:
                output += ", " + self.word_dict.get_random(word_length)
                available_space -= 2

            # add periods 7% of the time
            elif available_space > 2 and modifier_roll < 14:
                output += ". " + self.word_dict.get_random(word_length).title()
                available_space -= 2

            # add quotations 1% of the time
            elif available_space > 2 and modifier_roll < 15:
                output += "\" " + self.word_dict.get_random(word_length)
                available_space -= 2

            else:
                output += " " + self.word_dict.get_random(word_length)
                available_space -= 1

        output += " "
        return output

    def obfuscate(self, raw: str) -> deque[Entry]:
        """
        Takes a string and replaces all spaces with random words and punctuation.
        Then returns a stack containing each word followed by noise
        ```
        >>> for entry in obfuscator.obfuscate("Hello World"):
        ...     print(repr(entry.content))
        'Hello'
        ' other meaning that '
        'World'
        ' company meaning it '
        ```
        """
        words = raw.split(" ")
        output = deque()
        for word in words:
            self.word_dict.write(word.lower())
            output.append(Entry(word, Entry.ORIGINAL))
            output.append(Entry(self.generate_garbage(20), Entry.GARBAGE))
        return output