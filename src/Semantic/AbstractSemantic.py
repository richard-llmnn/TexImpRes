import re

class Semantic:
    regex = None  # Override!

    def __init__(self, file_content):
        self.file_content = file_content

    def get_first(self):
        return re.search(self.regex, self.file_content)

    def get_all(self):
        return re.finditer(self.regex, self.file_content)
