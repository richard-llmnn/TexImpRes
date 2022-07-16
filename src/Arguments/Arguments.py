import argparse
import os.path


class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("<input>", help="input file path", type=str)
        parser.add_argument("<output>", help="place the output into <output>", type=str)
        args = parser.parse_args().__dict__
        self.__input_file = args["<input>"]
        self.__output_file = args["<output>"]

    @property
    def input_file(self):
        return os.path.abspath(self.__input_file)

    @property
    def output_file(self):
        return os.path.abspath(self.__output_file)
