import Semantic.AbstractSemantic as AbstractSemantic


class ImportNewlineSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+"[\s]*(\r\n|\r|\n)'
