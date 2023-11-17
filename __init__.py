"""
This script imports modules and updates the list of custom nodes.
Modified from Sources:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/8cc071e40d0270d42e00028926688c68f069fde7/pysssss.py
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/8cc071e40d0270d42e00028926688c68f069fde7/__init__.py
"""
import importlib.util
import glob
import os
import sys


NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Get a list of the files in the nodes directory.
dir = os.path.dirname(__file__)
dir = os.path.join(dir, "nodes")
dir = os.path.abspath(dir)
files = glob.glob(os.path.join(dir, "*.py"), recursive=False)

for file in files:
    # Import the module associated with the file.
    name = os.path.splitext(file)[0]
    spec = importlib.util.spec_from_file_location(name, file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)

    # Update the node lists.
    if hasattr(module, "NODE_CLASS_MAPPINGS") and getattr(module, "NODE_CLASS_MAPPINGS") is not None:
        NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
        if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS") and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None:
            NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS",]
