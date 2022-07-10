import Exceptions.TreeResolver as TreeResolverExceptions

def resolve(importTree, startKey, forbiddenFiles=[]):
    forbiddenFiles = forbiddenFiles.copy()  # because the array list referenced -> create a copy

    # check if file is already in forbiddenFiles
    if startKey in forbiddenFiles:
        forbiddenFiles.append(startKey)  # add the file twice for better traceback design
        return False, forbiddenFiles
    # if not -> add the file
    forbiddenFiles.append(startKey)

    if startKey not in importTree:
        raise TreeResolverExceptions.MissingFile(f"File \"{startKey}\" was not found in file tree")

    for fileImport in importTree[startKey]:
        code, callstack = resolve(importTree, fileImport, forbiddenFiles)
        if code == False:
            return False, callstack

    return True, []

def resolve_handler(importTree, startKey):
    cleanedTree = {}
    for key, value in importTree.items():
        cleanedTree[key] = list(set(value))

    del importTree

    code, callstack = resolve(cleanedTree, startKey)
    if code == False:
        raise TreeResolverExceptions.CycleDetected("Import cycle detected:\n" + " -> ".join(map(str, callstack)))
    else:
        return True
