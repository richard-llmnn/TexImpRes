import Semantic.AbstractSemantic as AbstractSemantic
import re

class VariableSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'\$\w+'

    def __init__(self, file_content):
        self.file_content = file_content
    def get_first(self):
        return re.search(VariableSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(VariableSemantic.regex, self.file_content)
