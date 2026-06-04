from .any_type import any_type


class ConvertToInteger:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type,),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("output",)
    FUNCTION = "convert"
    CATEGORY = "zfr-nodes"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def _convert_str_to_int(self, value):
        text = str(value).strip()
        if text.lower() in ("true", "yes", "y", "on"):
            return 1
        if text.lower() in ("false", "no", "n", "off"):
            return 0
        try:
            return int(text)
        except Exception:
            try:
                return int(float(text))
            except Exception:
                return 0

    def convert(self, input):
        try:
            return (int(input),)
        except Exception:
            try:
                return (int(float(input)),)
            except Exception:
                return (self._convert_str_to_int(input),)
