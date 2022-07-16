import Semantic.AbstractSemantic as AbstractSemantic
import re


class CommentInlineSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r"@comment.*"

    def __init__(self, file_content):
        self.file_content = file_content

    def get_first(self):
        return re.search(CommentInlineSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(CommentInlineSemantic.regex, self.file_content)
