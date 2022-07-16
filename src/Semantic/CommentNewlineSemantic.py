import Semantic.AbstractSemantic as AbstractSemantic
import re


class CommentNewlineSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r"^@comment.*\n"

    def __init__(self, file_content):
        self.file_content = file_content

    def get_first(self):
        return re.search(CommentNewlineSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(CommentNewlineSemantic.regex, self.file_content)
