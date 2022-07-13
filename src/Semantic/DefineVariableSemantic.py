import Semantic.AbstractSemantic as AbstractSemantic
import re

class DefineVariableSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@var \w* = "[^"]*"[\n\t\r\s]*'

    def __init__(self, file_content):
        self.file_content = file_content
    def get_first(self):
        return re.search(DefineVariableSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(DefineVariableSemantic.regex, self.file_content)
