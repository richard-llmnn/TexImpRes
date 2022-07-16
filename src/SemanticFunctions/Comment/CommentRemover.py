import Semantic.CommentNewlineSemantic as CommentNewlineSemantic
import Semantic.CommentInlineSemantic as CommentInlineSemantic
import re


class CommentRemover:
    def __init__(self, file_content):
        self.file_content = file_content

    def run(self):
        self.remove_newline_comments()
        self.remove_inline_comments()

        return self.file_content

    def remove_inline_comments(self):
        self.file_content = re.sub(CommentInlineSemantic.CommentInlineSemantic.regex, "", self.file_content)

    def remove_newline_comments(self):
        self.file_content = re.sub(CommentNewlineSemantic.CommentNewlineSemantic.regex, "", self.file_content, flags=re.M)
