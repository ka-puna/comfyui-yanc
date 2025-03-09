"""
This node returns a string containing the current datetime according to a
        formatted string.
        See https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
Depends On:
    datetime
Input:
    string_format: A string formatted for datetime.strftime().
Output:
    STRING: A copy of 'string_format' with replacements from datetime.datetime.
"""
from datetime import datetime


class FormatDatetimeString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_format": ("STRING", {
                    "multiline": False,
                    "default": "%Y-%m-%d",
                }),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "get_datetime_string"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(s, string_format):
        now_standard = datetime.now(datetime.timezone.utc).isoformat()
        return [string_format, now_standard]

    def get_datetime_string(self, string_format):
        now = datetime.now()
        return (now.strftime(string_format),)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.FormatDatetimeString": FormatDatetimeString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.FormatDatetimeString": "Format Datetime String",
}