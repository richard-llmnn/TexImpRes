import Semantic.AbstractSemantic as AbstractSemantic
import re


class ImportSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+"'

    def __init__(self, file_content):
        self.file_content = file_content

    def get_first(self):
        return re.search(ImportSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(ImportSemantic.regex, self.file_content)
