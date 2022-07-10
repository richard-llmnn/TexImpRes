import Semantic.DefineVariableSemantic as DefineVariableSemantic
import Semantic.VariableSemantic as VariableSemantic

def replace(file_content):
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
        matches = list(VariableSemantic.VariableSemantic(file_content[start_from:]).get_all())
        matches.reverse()
        for found_variable in matches:
            if file_content[found_variable.start() - 1] == "\\" and file_content[found_variable.start() - 2] != "\\":
                skipped=True
                continue
            skipped=False
            file_content = file_content[:found_variable.start()+start_from] + \
                variable["value"] + \
                file_content[found_variable.end()+start_from:]
        if not skipped:
            file_content = file_content[:variable["start"]] + \
                file_content[variable["end"]:]
    
    print(file_content)

