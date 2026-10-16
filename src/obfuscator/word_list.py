# stlib
import random


class WordList(list):
    def __init__(self, size: int, initial_data: list[str] | None = None) -> None:
        self.size = size
        self.write_index = 0
        self.num_writes = 0

        super().__init__([0] * self.size)

        if not initial_data:
            return
        
        for word in initial_data:
            self.write(word)

    def get_random(self) -> str:
        """
        Returns a random entry from the buffer.

        Returns:
            str: Represents the selected entry.
        
        >>> mylist
        ['watermelon', 'apple', 'pear']
        >>> mylist.get_random()
        'watermelon'
        >>> mylist.get_random()
        'apple'
        >>> mylist.get_random()
        'watermelon'
        """
        return random.choice(self[0 : min(self.num_writes, self.size - 1)])

    def write(self, word: str) -> None:
        """
        Writes a word to the buffer. Overwrites the oldest entry.

        Args:
            word (str): Represents the word to add to the buffer.

        >>> mylist = WordList(3)
        [0, 0, 0]
        >>> mylist.write("banana")
        ['banana', 0, 0]
        >>> mylist.write("apple"); test.write("pear"); test.write("watermelon");
        ['watermelon', 'apple', 'pear']
        """
        self[self.write_index] = word
        self.write_index = (self.write_index + 1) % self.size
        self.num_writes += 1