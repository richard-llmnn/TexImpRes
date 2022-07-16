import Semantic.AbstractSemantic as AbstractSemantic


class DefineVariableSemantic(AbstractSemantic.Semantic):
    # static variables
    regex = r'[.]*@var \w* = "[^"]*"[\n\t\r\s]*'
