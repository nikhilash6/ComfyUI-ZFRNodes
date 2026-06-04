from .any_type import any_type


class ConvertToFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type,),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("output",)
    FUNCTION = "convert"
    CATEGORY = "zfr-nodes"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def _convert_str_to_float(self, value):
        text = str(value).strip()
        if text.lower() in ("true", "yes", "y", "on"):
            return 1.0
        if text.lower() in ("false", "no", "n", "off"):
            return 0.0
        try:
            return float(text)
        except Exception:
            return 0.0

    def convert(self, input):
        try:
            return (float(input),)
        except Exception:
            return (self._convert_str_to_float(input),)
