import Arguments.Arguments as Arguments
import TreeBuilder.TreeBuilder as TreeBuilder
import prettyprint.pprint as pprint

class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()

    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()