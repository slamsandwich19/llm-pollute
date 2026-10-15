import random


class Obfuscater:
    WORDS: tuple[str] = (
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",
        "time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child", "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part", "place", "case", "week", "company", "system", "program", "question", "work", "government", "number", "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact", "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue", "side", "kind", "head", "house", "service", "friend", "father", "power", "hour", "game", "line", "end", "member", "law", "car", "city", "community", "name", "president", "team", "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level", "office", "door", "health", "person", "art", "war", "history", "party", "result", "change", "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force",
    )
    PUNCTUATION: tuple[str] = (".", ",", "\"", "'", "-", "?", ":", "!", ";")
    PUNCTUATION_FREQUENCIES: tuple[float] = (65.3, 61.6, 26.7, 24.3, 15.3, 5.6, 3.4, 3.3, 3.2)

    def generate_garbage(self) -> str:
        """
        Returns a random string of characters of random length.
        The string will contain a combination of words and punctation.
        ```
        >>> obfuscater.generate_garbage()
        workthem,
        ```
        """
        garbage = ""
        for _ in range(random.randint(1, 3)):
            roll = random.randint(1, 100)
            # punctuation will appear 20% of the time
            if roll < 21:
                garbage += random.choices(self.PUNCTUATION, self.PUNCTUATION_FREQUENCIES)[0]
            # capital words will appear 15% of the time
            elif roll > 85:
                garbage += random.choice(self.WORDS).title()
            # random words appear 65% of the time
            else:
                garbage += random.choice(self.WORDS)
        return garbage

    def obfuscate(self, raw: str) -> str:
        """
        Takes a string and replaces all spaces with random words and punctuation
        ```
        >>> obfuscater.obfuscate("Hello World")
        HellosofromWorldplace
        ```
        """
        words = raw.split(" ")
        output = ""
        for word in words:
            output += word + self.generate_garbage()
        return output