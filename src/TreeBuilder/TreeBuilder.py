import TreeBuilder.resolve as resolve
import os.path
import Exceptions.File as FileExceptions
import Semantic.Import as ImportSemantic

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
            import_resolver = ImportSemantic.ImportSemantic(file_content)
            for found_import in import_resolver.get_all():
                if file_content[found_import.start() - 1] == "\\" and file_content[found_import.start() - 2] != "\\":
                    continue

                import_file_path = found_import.group().split('"')[-2]
                import_file_path = os.path.join(os.path.dirname(file_path), import_file_path)
                import_file_path = os.path.abspath(import_file_path)
                print(f"File '{import_file_path}' added to file tree!")
                self.file_tree[file_path].append(import_file_path)

                if import_file_path not in self.file_tree:
                    if not os.path.exists(import_file_path):
                        raise FileExceptions.FileNotFound(f"File \"{import_file_path}\" was not found in \"{file_path}\"")
                    self.file_tree[import_file_path] = []

                try:
                    resolve.resolve_handler(self.file_tree, self.start_file_path)
                except Exception as e:
                    print(str(e))
                    exit()


                self.resolve_imports(import_file_path)
