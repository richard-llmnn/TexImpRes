import Semantic.AbstractSemantic as AbstractSemantic


class ImportNewlineSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+" *(\r\n|\r|\n){1}'
