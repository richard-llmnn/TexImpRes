import Arguments.Arguments as Arguments
from SemanticFunctions.Import import TreeBuilder, ImportResolver
from SemanticFunctions.Variable import replace

class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()
        self.resolve_all_imports()

    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()

        replace.replace(open(self.args.input_file).read())



    def resolve_all_imports(self):
        (ImportResolver.ImportResolver(self.args.input_file, self.args.output_file)).run()
