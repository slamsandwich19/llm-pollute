# project
from src.obfuscator.word_list import WordList


class WordDictionary:
    COMMON_WORDS: dict[int, str]
    MAX_LENGTH = 8
    
    def __init__(self, buffer_size: int = 50) -> None:
        self.COMMON_WORDS = {
            1: ["a", "I"],
            2: ["to", "of", "in", "it", "is", "be", "as", "at", "so", "we", "he", "by", "or", "on", "do", "if", "my", "an", "no", "us"],
            3: ["the", "and", "for", "you", "are", "not", "all", "out", "day", "get", "has", "him", "his", "how", "man", "new", "now", "old", "see", "two"],
            4: ["that", "with", "have", "this", "will", "your", "from", "they", "know", "want", "been", "good", "much", "some", "time", "very", "when", "come", "here", "just"],
            5: ["their", "would", "about", "there", "which", "other", "could", "years", "first", "water", "after", "right", "three", "place", "where", "sound", "great", "house", "under", "group"],
            6: ["people", "before", "little", "should", "always", "system", "school", "public", "number", "course", "during", "second", "center", "family", "within", "though", "mother", "around", "states", "friend"],
            7: ["because", "through", "between", "another", "against", "country", "company", "program", "problem", "general", "however", "without", "nothing", "governs", "service", "history", "several", "present", "meaning", "process"],
            8: ["together", "children", "american", "business", "possible", "standard", "increase", "activity", "industry", "interest", "decision", "strength", "building", "practice", "national", "question", "movement", "material", "economic", "physical"]
        }

        self.buffer_size = buffer_size
        self.words = {
            length: WordList(self.buffer_size, self.COMMON_WORDS[length])
            for length in self.COMMON_WORDS
        }

    def get_random(self, length: int) -> str:
        """
        Returns a random entry from running_dictionary.

        Args:
            length (int): Represents the desired word size.

        Raises:
            IndexError: Raises this if no entries for a given length exist.

        Returns:
            str: Represents the output word.
        
        >>> my_dictionary
        {1: [...], 2: ['no', 'us', 'an'], 3: [...]}
        >>> my_dictionary.get_random(2)
        'us'
        >>> my_dictionary.get_random(2)
        'no'
        """
        if length in self.words:
            return self.words[length].get_random()
        else:
            raise IndexError(f"No word entries for length '{length}'")

    def write(self, word: str) -> None:
        """
        Writes a word to the buffer containing words of similar length.

        Args:
            word (str): Represents the word to write.
        
        >>> my_dictionary
        {1: [...], 2: ['no', 'us', 'an'], 3: [...]}
        >>> mydictionary.write("go")
        {1: [...], 2: ['no', 'us', 'go'], 3: [...]}
        """
        length = len(word)
        if length in self.words:
            self.words[length].write(word)
        else:
            self.words[length] = WordList(self.buffer_size)
            self.words[length].write(word)

if __name__ == "__main__":
    test = WordDictionary()
    print(test.words)
    test.write("go")
    print(test.words)
    print(test.get_random(2))