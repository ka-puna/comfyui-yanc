"""
This node concatenates multiple strings.
Input:
    Let Strings = [a_optional, separator, b_optional].
Output:
    A concatenation of each strings by order in 'Strings'.
"""
class ConcatStrings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "separator": ("STRING", {
                    "multiline": False,
                    "default": "",
                }),
            },
            "optional": {
                "a_optional": ("STRING", {
                    "multiline": False,
                    "forceInput": True,
                }),
                "b_optional": ("STRING", {
                    "multiline": False,
                    "forceInput": True,
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "concat_strings"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def concat_strings(self, separator, a_optional = "", b_optional = ""):
        return (a_optional + separator + b_optional,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.ConcatStrings": ConcatStrings,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.ConcatStrings": "Concatenate Strings",
}
