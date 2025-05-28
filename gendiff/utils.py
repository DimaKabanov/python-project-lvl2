def flatten(coll):
    result = []
    for item in coll:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result