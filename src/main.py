import argparse
import os.path
import re
import Exceptions.TreeResolver as TreeResolverExceptions

def pprint(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pprint(value, indent+1)
        elif isinstance(value, list):
            for item in value:
                print('\t' * (indent+1) + str(item))
            print()
        else:
            print('\t' * (indent+1) + str(value))


def resolve(importTree, startKey, forbiddenFiles=[]):
    forbiddenFiles = forbiddenFiles.copy()  # because the array list referenced -> create a copy

    # check if file is already in forbiddenFiles
    if startKey in forbiddenFiles:
        forbiddenFiles.append(startKey)  # add the file twice for better traceback design
        return False, forbiddenFiles
    # if not -> add the file
    forbiddenFiles.append(startKey)

    if startKey not in importTree:
        raise TreeResolverExceptions.MissingFile(f"File \"{startKey}\" was not found in file tree!")

    for fileImport in importTree[startKey]:
        code, callstack = resolve(importTree, fileImport, forbiddenFiles)
        if code == False:
            return False, callstack

    return True, []


def resolveHandler(importTree, startKey):
    cleanedTree = {}
    for key, value in importTree.items():
        cleanedTree[key] = list(set(value))

    del importTree

    code, callstack = resolve(cleanedTree, startKey)
    if code == False:
        raise TreeResolverExceptions.CycleDetected("Import cycle detected:\n" + " -> ".join(map(str, callstack)))
    else:
        return True

class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('<input>', help='input file path', type=str)
        parser.add_argument('<output>', help='place the output into <output>', type=str)
        args = parser.parse_args().__dict__
        self.__input_file = args["<input>"]
        self.__output_file = args["<output>"]
        print(self.__dict__)

    @property
    def input_file(self):
        return os.path.abspath(self.__input_file)

    @property
    def output_file(self):
        return os.path.abspath(self.__output_file)


class Semantic:
    regex = None # Override!

class ImportSemantic(Semantic):
    # static variables
    regex = r'[.]*@import "[^"]+"'

    def __init__(self, file_content):
        self.file_content = file_content
    def get_first(self):
        return re.search(ImportSemantic.regex, self.file_content)

    def get_all(self):
        return re.finditer(ImportSemantic.regex, self.file_content)



class TreeBuilder:

    def __init__(self, file_path):
        self.start_file_path = file_path
        self.file_tree = {}

    def resolve_imports(self, file_path = None):
        if file_path is None:
            file_path = self.start_file_path

        self.file_tree[file_path] = []

        with open(file_path, "r") as imported_file:
            file_content = imported_file.read()
            import_resolver = ImportSemantic(file_content)
            for found_import in import_resolver.get_all():
                if file_content[found_import.start() - 1] == "\\" and file_content[found_import.start() - 2] != "\\":
                    continue

                import_file_path = found_import.group().split('"')[-2]
                import_file_path = os.path.join(os.path.dirname(file_path), import_file_path)
                print(f"File '{import_file_path}' added to file tree!")
                self.file_tree[file_path].append(import_file_path)

                if import_file_path not in self.file_tree:
                    self.file_tree[import_file_path] = []

                try:
                    resolveHandler(self.file_tree, self.start_file_path)
                except Exception as e:
                    print(str(e))
                    exit()


                self.resolve_imports(import_file_path)

class App:
    def __init__(self):
        args = Arguments()
        tree_bulder = TreeBuilder(args.input_file)
        tree_bulder.resolve_imports()
        pprint(tree_bulder.file_tree)


def main():
    App()

if __name__ == "__main__":
    main()