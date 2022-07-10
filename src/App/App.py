import Arguments.Arguments as Arguments
from SemanticFunctions.Import import TreeBuilder

class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()

    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()

    def resolve_all_imports(self):
        pass