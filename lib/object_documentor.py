import json


def get_prop_name(key, parents=None, complex_object=False):
    prop = ""
    if parents is not None:
        for parent in parents:
            prop += f"{parent}."
        if complex_object is False:
            prop += key
        else:
            prop = prop.removesuffix(".")
    else:
        prop = key
    return prop


def documentize_prop(key, value, parents=None):
    data_type = None
    prop = get_prop_name(key, parents)
    if isinstance(value, str):
        data_type = "String"
    if isinstance(value, int):
        data_type = "Integer"
    if isinstance(value, float):
        data_type = "Float"
    description = input("Describe prop " + prop + ": ")
    line = f"`{prop}` | {data_type} | {description} | {str(value)}"
    return [line + "\n"]


def documentize_object(key, data, parents=None):
    prop = get_prop_name(key, parents, True)
    description = input("Describe prop " + prop + ": ")
    lines = [f"`{prop}` | Object | {description} |\n"]
    for i in data:
        if isinstance(data[i], dict):
            lines = lines + documentize_object(i, data[i], parents + (i,))
        elif isinstance(data[i], list):
            print("Array")
        else:
            lines = lines + documentize_prop(i, data[i], parents)
    return lines


def documentize_array(key, data, parents=None):
    prop = get_prop_name(key, parents, True)
    lines = [f"`{prop}` | Array | |\n"]
    for item in data:
        if isinstance(item, dict):
            lines = lines + documentize_object(
                "ArrayItem", item, parents + ("ArrayItem",)
            )

        elif isinstance(item, list):
            print("Array")
        else:
            lines = lines + documentize_prop("ArrayItem", item, parents)
    return lines
