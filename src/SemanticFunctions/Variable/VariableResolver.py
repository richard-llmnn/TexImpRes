import Semantic.DefineVariableSemantic as DefineVariableSemantic
import Semantic.VariableSemantic as VariableSemantic

class VariableResolver():
    def replace(self, file_content):
        variables = []
        semantics = DefineVariableSemantic.DefineVariableSemantic(file_content)
        for found_variable in semantics.get_all():
            if file_content[found_variable.start() - 1] == "\\" and file_content[found_variable.start() - 2] != "\\":
                continue
            variables.append({
                "key": found_variable.group().split()[1],
                "value": found_variable.group().split('"')[1],
                "start": found_variable.start(),
                "end": found_variable.end()
            })
        variables.sort(key=lambda v: v["start"], reverse=True)
        for variable in variables:
            start_from = variable["end"]
            matches = list(VariableSemantic.VariableSemantic(file_content[start_from:], variable["key"]).get_all())
            matches.reverse()
            temp_file_content = file_content[start_from:]
            for found_variable in matches:
                if temp_file_content[found_variable.start() - 1] == "\\" and temp_file_content[found_variable.start() - 2] != "\\":
                    skipped=True
                    continue
                skipped=False
                file_content = file_content[:found_variable.start()+start_from] + \
                    variable["value"] + \
                    file_content[found_variable.end()+start_from:]
                if temp_file_content[found_variable.start() - 2:found_variable.start()] == r"\\":
                    file_content = file_content[:found_variable.start()+start_from - 1] + \
                        file_content[found_variable.start()+start_from:]
            if not skipped:
                if file_content[variable["start"]-2:variable["start"]] == r"\\":
                    file_content = file_content[:variable["start"] - 1] + \
                        file_content[variable["start"]:]
                else:
                    file_content = file_content[:variable["start"]] + \
                        file_content[variable["end"]:]

        semantics = DefineVariableSemantic.DefineVariableSemantic(file_content)
        for found_variable in semantics.get_all():
            if file_content[found_variable.start() - 1] == "\\" and file_content[found_variable.start() - 2] != "\\":
                file_content = file_content[:found_variable.start() - 1] + \
                    file_content[found_variable.start():]
                continue

        for variable in variables:
            start_from = variable["end"]
            matches = list(VariableSemantic.VariableSemantic(file_content[start_from:], variable["key"]).get_all())
            matches.reverse()
            temp_file_content = file_content[start_from:]
            for found_variable in matches:
                if temp_file_content[found_variable.start() - 1] == "\\" and temp_file_content[found_variable.start() - 2] != "\\":
                    file_content = file_content[:found_variable.start()+start_from-1] + \
                        file_content[found_variable.start()+start_from:]

        return file_content
