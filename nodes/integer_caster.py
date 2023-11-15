"""
This node casts an integer to multiple types.
Input:
    n: The integer to be casted.
Output:
    INT: A copy of 'n'.
    FLOAT: A float representation of 'n'.
    STRING: A string representations of 'n'.
"""
class IntegerCaster:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "n": ("INT", { "default": 0,}),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING",)
    RETURN_NAMES = ("INT", "FLOAT", "STRING",)
    FUNCTION = "get_int"
    OUTPUT_NODE = True
    CATEGORY = "utils/primitives"

    def get_int(self, n):
        return (n, float(n), str(n),)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.IntegerCaster": IntegerCaster,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.IntegerCaster": "Integer Caster",
}
