import Semantic.AbstractSemantic as AbstractSemantic


class ImportSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+"'
