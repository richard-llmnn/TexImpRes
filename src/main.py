import argparse
import os.path
import re

class Arguments():
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

class TreeBuilder():
    @staticmethod
    def resolve_imports(text):
        for found_import in re.finditer(r'[.]*@import "[^"]+"', text):
            if text[found_import.start() - 1] == "\\" and text[found_import.start() - 2] != "\\" :
                continue
            print(found_import)
            file_path = found_import.group().split('"')[-2]
            with open(file_path, 'r') as imported_file:
                TreeBuilder.resolve_imports(imported_file.read())

class App():
    def __init__(self):
        args = Arguments()
        with open(args.input_file, 'r') as input_file:
            TreeBuilder.resolve_imports(input_file.read())



def main():
    App()

if __name__ == "__main__":
    main()