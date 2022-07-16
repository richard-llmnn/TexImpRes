import Semantic.ImportSemantic as ImportSemantic
import os.path


class ImportResolver:
    def __init__(self, entry_file_path):
        self.entry_file_path = entry_file_path

    def run(self):
        with open(self.entry_file_path, "r") as entry_file:
            file_content = entry_file.read()

        file_content = self.recursive_resolve_files(file_content, self.entry_file_path)

        return self.remove_escaped_imports(file_content)

    def remove_escaped_imports(self, file_content):
        found_imports = list(ImportSemantic.ImportSemantic(file_content).get_all())
        found_imports.reverse()

        for found_import in found_imports:
            if (
                file_content[found_import.start() - 1] == "\\"
                and file_content[found_import.start() - 2] != "\\"
            ):
                file_content = (
                    file_content[: found_import.start() - 1]
                    + file_content[found_import.start() :]
                )

        return file_content

    def recursive_resolve_files(self, file_content, current_abs_path):
        found_imports = list(ImportSemantic.ImportSemantic(file_content).get_all())
        found_imports.reverse()

        for found_import in found_imports:
            if (
                file_content[found_import.start() - 1] == "\\"
                and file_content[found_import.start() - 2] != "\\"
            ):
                continue
            import_rel_path = found_import.group().split('"')[-2]
            import_abs_path = self.create_rel_path(current_abs_path, import_rel_path)

            file = open(import_abs_path, "r")
            import_file_content = self.recursive_resolve_files(
                file.read(), import_abs_path
            )
            file.close()

            offset = 0
            if file_content[found_import.start() - 2 : found_import.start()] == "\\\\":
                offset = 1

            file_content = (
                file_content[0 : found_import.start() - offset]
                + import_file_content
                + file_content[found_import.end() :]
            )

        return file_content

    def create_rel_path(self, root_path, file_path):
        return os.path.abspath(os.path.join(os.path.dirname(root_path), file_path))
