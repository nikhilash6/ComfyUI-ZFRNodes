from .any_type import any_type


class ConvertToString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type,),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "convert"
    CATEGORY = "zfr-nodes"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def convert(self, input):
        if input is None:
            return ("",)
        return (str(input),)
