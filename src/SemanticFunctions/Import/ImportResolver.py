import Semantic.ImportSemantic as ImportSemantic
import os.path

class ImportResolver:
    def __init__(self, entry_file_path, output_file_path):
        self.entry_file_path = entry_file_path
        self.output_file_path = output_file_path

    def run(self):

        before_file_path = self.entry_file_path

        with open(self.entry_file_path, "r") as entry_file:
            file_content = entry_file.read()

            while True:
                found_import = ImportSemantic.ImportSemantic(file_content).get_first()
                if found_import is None:
                    break

                print(f"---Found import: {found_import.group()}---")
                if file_content[found_import.start() - 1] == "\\" and file_content[found_import.start() - 2] != "\\":
                    continue

                import_rel_path = found_import.group().split('"')[-2]
                import_abs_path = self.create_rel_path(before_file_path, import_rel_path)
                before_file_path = import_abs_path

                if not os.path.exists(import_abs_path):
                    import_abs_path = self.create_rel_path(self.entry_file_path, import_rel_path)
                    before_file_path = import_abs_path

                file = open(import_abs_path, "r")
                import_file_content = file.read()
                file.close()

                file_content = file_content[0:found_import.start()] + import_file_content + file_content[found_import.end():]

        with open(self.output_file_path, "w") as output_file:
            output_file.write(file_content)

    def create_rel_path(self, root_path, file_path):
        return os.path.abspath(os.path.join(os.path.dirname(root_path), file_path))