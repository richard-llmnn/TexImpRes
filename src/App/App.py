import Arguments.Arguments as Arguments
from SemanticFunctions.Import import TreeBuilder, ImportResolver
from SemanticFunctions.Variable import VariableResolver
from SemanticFunctions.Comment import CommentRemover


class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()
        with open(self.args.output_file, "w") as f:  # replace comments
            text = self.resolve_all_imports()
            comment_remover = CommentRemover.CommentRemover(text)
            text = comment_remover.run()
            text = self.resolve_all_variables(text)
            f.write(text)

    # check for import cycles
    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()

    def resolve_all_imports(self):
        return (
            ImportResolver.ImportResolver(self.args.input_file, self.args.output_file)
        ).run()

    def resolve_all_variables(self, text):
        return VariableResolver.VariableResolver().replace(text)
