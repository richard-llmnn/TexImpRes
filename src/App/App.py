import Arguments.Arguments as Arguments
from SemanticFunctions.Import import TreeBuilder, ImportResolver
from SemanticFunctions.Variable import VariableResolver
from SemanticFunctions.Comment import CommentRemover


class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()

        file_content = self.resolve_all_imports()
        file_content = self.remove_comments(file_content)
        file_content = self.resolve_all_variables(file_content)

        with open(self.args.output_file, "w") as output_pointer:
            output_pointer.write(file_content)

        print(f"Compiled file was saved to {self.args.output_file}.")

    # check for import cycles
    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()

    def resolve_all_imports(self):
        return ImportResolver.ImportResolver(self.args.input_file).run()

    def resolve_all_variables(self, text):
        return VariableResolver.VariableResolver().replace(text)

    def remove_comments(self, text):
        return CommentRemover.CommentRemover(text).run()