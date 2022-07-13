import Semantic.AbstractSemantic as AbstractSemantic
import re

class VariableSemantic(AbstractSemantic.Semantic):

    def __init__(self, file_content, name):
        self.file_content = file_content
        self.regex = f"\${name}"
    def get_first(self):
        return re.search(self.regex, self.file_content)

    def get_all(self):
        return re.finditer(self.regex, self.file_content)
