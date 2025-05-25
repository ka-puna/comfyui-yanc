"""
This node shortens a string by word, then appends a trailing character to the
        when it is shortened.
        See: https://docs.python.org/3/library/textwrap.html#textwrap.shorten.
Depends On:
    textwrap
Input:
    string
    length: The maximum character length of the string.
    trail: The string suffixed to the output string when it is truncated.
Output:
    STRING: A copy of 'string' shortened by word to 'length', using 'trail'
            to suffix a shortened string.
"""
from textwrap import shorten


class TruncateString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", { "forceInput": True,}),
                "length": ("INT", { "default": 48, "min": 0}),
                "trail": ("STRING", { "default": "-",}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "truncate_string"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def truncate_string(self, string, length, trail):
        return (shorten(string, width=length, placeholder=trail),)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.TruncateString": TruncateString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.TruncateString": "Truncate String",
}
