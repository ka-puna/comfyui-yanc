"""
This node saves images in the WEBP format. It includes options for file name, location, and quality.
Depends On:
    json, random, numpy, os, PIL, random, comfy, folder_paths
Input:
    images: A batch of images.
    output_type: The output type selects which base directory is used.
    filename_prefix: The filename/filepath, relative to the base directory.
    lossless: If True, then the desired image format is lossless.
    quality: This value in [0, 100] sets the lossy image quality.
Modified from Sources:
https://github.com/comfyanonymous/ComfyUI/blob/391c1046cff8a3877a2ba343057579ab4278c5b1/nodes.py
https://github.com/Kaharos94/ComfyUI-Saveaswebp/blob/68d5c29192450d5b2f5a4e04fdd05808902190d3/Save_as_webp.py
https://github.com/audioscavenger/save-image-extended-comfyui/blob/bf9177927177f6c5649db11d5043cd34cd98de05/save_image_extended.py
"""
import json
import numpy as np
import os
from PIL import Image
import random

from comfy.cli_args import args
import folder_paths


class SaveImageWEBP:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", ),
                "output_type": (["output", "temp"], {"default": "output"}),
                "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                "lossless": ("BOOLEAN", {"default": False}),
                "quality": ("INT", {"default": 90, "min": 0, "max": 100}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
    }

    RETURN_TYPES = ()
    FUNCTION = "save_images"
    OUTPUT_NODE = True
    CATEGORY = "image"

    def save_images(self, images, output_type, filename_prefix, lossless, quality, prompt=None, extra_pnginfo=None):
        results = list()
        kwargs = dict()
        output_dir = folder_paths.get_output_directory() if output_type == "output" else folder_paths.get_temp_directory()
        full_output_folder, filename, counter, subfolder = folder_paths.get_save_image_path(filename_prefix, output_dir, images[0].shape[1], images[0].shape[0])[0:4]

        # Save batch arguments.
        kwargs["lossless"] = lossless
        kwargs["quality"] = quality

        for (batch_number, image) in enumerate(images):
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            filename_with_batch_num = filename.replace("%batch_num%", str(batch_number))
            file = f"{filename_with_batch_num}_{counter:05}.webp"
            while os.path.exists(os.path.join(full_output_folder, file)):
                file = f"{filename_with_batch_num}_{counter:05}_%s.webp" % ''.join(random.choice("abcdefghijklmnopqrstupvxyz") for x in range(5))

            if not args.disable_metadata:
                exif = img.getexif()
                if prompt is not None:
                    # Add prompt to EXIF tag "Make".
                    exif[0x010f] = "Prompt:" + json.dumps(prompt)
                if extra_pnginfo is not None:
                    # Add workflow to EXIF tag "ImageDescription".
                    exif[0x010e] = "Workflow:" + json.dumps(extra_pnginfo["workflow"])
                kwargs["exif"] = exif.tobytes()

            img.save(os.path.join(full_output_folder, file), **kwargs)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": output_type,
            })
            counter += 1

        return { "ui": { "images": results } }


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "YANC.SaveImageWEBP": SaveImageWEBP,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "YANC.SaveImageWEBP": "Save Image as WEBP",
}
