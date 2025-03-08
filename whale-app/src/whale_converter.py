class WhaleConverter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def convert(self, text: str) -> str:
        return ''.join(char for char in text if char not in self.vowels)
