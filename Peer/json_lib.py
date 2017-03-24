import json

def validateAndStringifyJson(data):
    """
    data: dict/JSON object
    return: json string of data
    """
    try:
        return json.dumps(data, indent=4)
    except NameError as err:
        return None

def validateAndCreateJson(data):
    """Validates the data argument sent against JSON format
        data: json data in string format
        returns: JSON object
    """
    try:
        return json.loads(data)
    except ValueError as err:
        print "Error creating the json, skipping."
