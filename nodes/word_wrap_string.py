"""
This node adds line breaks to a string according to a given width.
        See: https://docs.python.org/3/library/textwrap.html#textwrap.wrap.
Depends On:
    textwrap
Input:
    string
    width: The maximum character length of each line in the string, excluding
            the newline character.
    break_on_hyphens: If true, new lines can break a hyphenated word.
    keep_lines: If true, new lines in the original string are kept.
Ouput:
    STRING: A copy of 'string' broken by word such that lines fit 'width'.
"""
from textwrap import wrap


class WordWrapString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", { "forceInput": True,}),
                "width": ("INT", { "default": 70,}),
                "keep_lines": ("BOOLEAN", { "default": True, }),
                "break_on_hyphens": ("BOOLEAN", { "default": True, }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "word_wrap_string"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    def word_wrap_string(self, string, width, keep_lines, break_on_hyphens):
        strings = string.splitlines() if keep_lines else [string]
        for i in range(len(strings)):
            s_wrapped = wrap(strings[i], width=width, break_on_hyphens=break_on_hyphens)
            strings[i] = '\n'.join(s_wrapped)
        return ('\n'.join(strings),)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.WordWrapString": WordWrapString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.WordWrapString": "Word Wrap String",
}
