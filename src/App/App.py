import Arguments.Arguments as Arguments
from SemanticFunctions.Import import TreeBuilder, ImportResolver
from SemanticFunctions.Variable import VariableResolver
import re

class App:
    def __init__(self):
        self.args = Arguments.Arguments()

    def run(self):
        self.check_import_tree()
        self.resolve_all_imports()
        with open(self.args.output_file, "r+") as f: # replace comments
            text = f.read()
            text = re.sub(r"^@comment.*\n", "", text, flags=re.M)
            text = re.sub(r"@comment.*", "", text)
            print(text)
            text = self.resolve_all_variables(text)
            print(text)
            # print(text)


    def check_import_tree(self):
        tree_builder = TreeBuilder.TreeBuilder(self.args.input_file)
        tree_builder.resolve_imports()



    def resolve_all_imports(self):
        (ImportResolver.ImportResolver(self.args.input_file, self.args.output_file)).run()

    def resolve_all_variables(self, text):
        return (VariableResolver.VariableResolver().replace(text))
