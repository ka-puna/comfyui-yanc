"""
This node outputs a string representation of a widget value.
INPUT:
    node_name_for_sr:
        The target node's "Node name for S&R" property. The target node should
                have a unique value for this property.
    widget_name
OUTPUT:
    STRING: A string representation of node_name.widget_name.
Modified from Source:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/8cc071e40d0270d42e00028926688c68f069fde7/py/math_expression.py
"""


class GetWidgetValueString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "node_name_for_sr": ("STRING", {
                    "multiline": False,
                    "default": "",
                }),
                "widget_name": ("STRING", {
                    "multiline": False,
                    "default": "",
                }),
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO",
                "prompt": "PROMPT",
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "get_widget_value_string"
    OUTPUT_NODE = True
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(s, **kwargs):
        return float("NaN")

    def get_widget_value_string(self, node_name_for_sr, widget_name, extra_pnginfo, prompt):
        workflow = extra_pnginfo["workflow"]
        # Get node id.
        node_id = None
        for node in workflow["nodes"]:
            name = node["type"]
            if "properties" in node:
                if "Node name for S&R" in node["properties"]:
                    name = node["properties"]["Node name for S&R"]
                if name == node_name_for_sr:
                    node_id = node["id"]
        # Get widget value string from node.
        string = "%unknown_error%"
        if node_id is not None:
            values = prompt[str(node_id)]
            if "inputs" in values and widget_name in values["inputs"]:
                   value = values["inputs"][widget_name]
                   string = str(value)
            else:
                raise NameError(f"Widget not found: {node_name_for_sr}.{widget_name}")
        else:
            raise NameError(f"Node not found: {node_name_for_sr}.{widget_name}")
        return (string,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.GetWidgetValueString": GetWidgetValueString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.GetWidgetValueString": "Get Widget Value String",
}