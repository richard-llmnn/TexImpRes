import Arguments.Arguments as Arguments
import TreeBuilder.TreeBuilder as TreeBuilder
import prettyprint.pprint as pprint

class App:
    def __init__(self):
        args = Arguments.Arguments()
        tree_builder = TreeBuilder.TreeBuilder(args.input_file)

        try:
            tree_builder.resolve_imports()
        except Exception as e:
            print(str(e))
            exit()
        pprint.pprint(tree_builder.file_tree)
