import Semantic.AbstractSemantic as AbstractSemantic


class ImportInlineSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+"'
