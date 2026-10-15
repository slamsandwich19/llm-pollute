# stlib
import random
from collections import deque


class Entry:
    ORIGINAL = 0
    GARBAGE = 1
    def __init__(self, content: str, flag: int) -> None:
        self.content = content
        self.flag = flag

class Obfuscator:
    WORDS: tuple[str] = (
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",
        "time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child", "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part", "place", "case", "week", "company", "system", "program", "question", "work", "government", "number", "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact", "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue", "side", "kind", "head", "house", "service", "friend", "father", "power", "hour", "game", "line", "end", "member", "law", "car", "city", "community", "name", "president", "team", "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level", "office", "door", "health", "person", "art", "war", "history", "party", "result", "change", "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force",
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    )
    PUNCTUATION: tuple[str] = (".", ",", "\"", "'", "-", "?", ":", "!", ";")
    PUNCTUATION_FREQUENCIES: tuple[float] = (65.3, 61.6, 26.7, 24.3, 15.3, 5.6, 3.4, 3.3, 3.2)
    NUMBERS = "0123456789"

    def generate_garbage(self, target: int) -> str:
        """
        Returns a random string of characters of target length.
        The string will contain a combination of words, punctation, and sometimes numbers.
        ```
        >>> print(obfuscator.generate_garbage(20))
        want.studybookweek.4
        ```
                
        Args:
            target (int): Represents the desired size of the garbage text.

        Returns:
            str: Represents the output text.
        """
        garbage = ""
        character_count = 0

        while True:
            # generate new_item which may be a random word or punctuation
            roll = random.randint(1, 100)
            if roll < 21: # punctuation will appear 20% of the time
                new_item = random.choices(self.PUNCTUATION, self.PUNCTUATION_FREQUENCIES)[0]
            elif roll > 85: # capital words will appear 15% of the time
                new_item = " " + random.choice(self.WORDS).title()
            else: # random words appear 65% of the time
                new_item = " " + random.choice(self.WORDS)

            # escape if there are too many characters, this does not guarantee that the target is met
            character_count += len(new_item)
            if character_count > target - 1: # we need to inject a space at the end
                character_count -= len(new_item)
                break

            garbage += new_item

        # the while loop is not guaranteed to generate a string of length 'target'
        # therefore we fill the empty space with numbers
        garbage += "".join([random.choice(self.NUMBERS) for _ in range(target - character_count - 1)])
        garbage += " "
        return garbage

    def obfuscate(self, raw: str) -> deque[Entry]:
        """
        Takes a string and replaces all spaces with random words and punctuation.
        Then returns a stack containing each word followed by noise
        ```
        >>> for item in obfuscator.obfuscate("Hello World"):
        ...     print(item)
        Hello
        even
        World
        for
        ```
        """
        words = raw.split(" ")
        output = deque()
        for word in words:
            output.append(Entry(word, Entry.ORIGINAL))
            output.append(Entry(self.generate_garbage(20), Entry.GARBAGE))
        return output

if __name__ == "__main__":
    o = Obfuscator()
    for i in range(10):
        print(o.generate_garbage(20))