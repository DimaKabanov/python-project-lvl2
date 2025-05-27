def flatten(coll):
    result = []
    for item in coll:
        if isinstance(item, list):
            for sub_item in item:
                result.append(sub_item)
        else:
            result.append(item)
    return result