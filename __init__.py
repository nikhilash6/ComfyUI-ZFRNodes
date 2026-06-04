from .py.convert_to_integer import ConvertToInteger
from .py.convert_to_float import ConvertToFloat
from .py.convert_to_string import ConvertToString
from .py.convert_to_boolean import ConvertToBoolean
from .py.json_frame_extractor import JsonFrameExtractor
from .py.story_frame_generator import StoryFrameGenerator
from .py.simple_image_generator import SimpleImageGenerator


NODE_CLASS_MAPPINGS = {
    "Convert To Integer": ConvertToInteger,
    "Convert To Float": ConvertToFloat,
    "Convert To String": ConvertToString,
    "Convert To Boolean": ConvertToBoolean,
    "JSON Frame Extractor": JsonFrameExtractor,
    "Story Frame Generator": StoryFrameGenerator,
    "Simple Image Generator": SimpleImageGenerator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Convert To Integer": "Convert To Integer",
    "Convert To Float": "Convert To Float",
    "Convert To String": "Convert To String",
    "Convert To Boolean": "Convert To Boolean",
    "JSON Frame Extractor": "JSON Frame Extractor",
    "Story Frame Generator": "Story Frame Generator",
    "Simple Image Generator": "Simple Image Generator",
}

__version__ = "1.0.0"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "__version__"]
