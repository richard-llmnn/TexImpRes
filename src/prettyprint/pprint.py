def pprint(d, indent=0):
    for key, value in d.items():
        print("\t" * indent + str(key))
        if isinstance(value, dict):
            pprint(value, indent + 1)
        elif isinstance(value, list):
            for item in value:
                print("\t" * (indent + 1) + str(item))
            print()
        else:
            print("\t" * (indent + 1) + str(value))
