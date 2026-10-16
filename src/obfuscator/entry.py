

class Entry:
    ORIGINAL = 0
    GARBAGE = 1
    def __init__(self, content: str, flag: int) -> None:
        self.content = content
        self.flag = flag