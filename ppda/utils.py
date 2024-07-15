import pandas as pd
import re


def read_excel(file_path, header=0, sheet_name=None):
    return pd.read_excel(
        file_path, engine="openpyxl", header=header, sheet_name=sheet_name
    )


def to_camel_case(snake_str, joining="_"):
    """
    Translate from Python Code to JavaScript
    Parameter:
        snake_str: Python name convention
        joining: sign joinig string in python name
    Return: JavaScript name convention
    """
    if snake_str == "_id":
        return snake_str
    components = snake_str.split(joining)
    return components[0] + "".join(x.title() for x in components[1:])


def to_snake_case(camel_str):
    """
    Translate from JavaScript to Python
    Parameter:
        camel_str: JavaScript name convention
    Return: Python name convention
    """
    if camel_str == "_id":
        return camel_str
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()


def output_form(class_, data_list, output):
    """
    Transform a data to standardised format, default DataFrame
    Parameter:
        class_: format class to transform (list, set, tuple, numpy, etc.)
        data_list: data to transform
        output: name of the format in string so that don't need to pass a class object in class_
        (currently support only 'DataFrame')
    Return: corresponding data in chosen format
    """
    if not data_list:
        return []
    if output == "DataFrame":
        return pd.DataFrame(data_list) if data_list else []
    else:
        return [class_(instance) for instance in data_list]


def concatenate_output(lst_1, lst_2):
    if type(lst_1) != type(lst_2):
        print("ERROR in concatenate_output(): Not the same type")
        return []
    if isinstance(lst_1, list):
        return lst_1 + lst_2
    if isinstance(lst_1, pd.DataFrame):
        return pd.concat([lst_1, lst_2], ignore_index=True)
    if not lst_1 and not lst_2:
        return []
