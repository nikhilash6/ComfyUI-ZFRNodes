from .any_type import any_type


class ConvertToBoolean:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_type,),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("output",)
    FUNCTION = "convert"
    CATEGORY = "zfr-nodes"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def convert(self, input):
        if isinstance(input, bool):
            return (input,)

        if isinstance(input, (int, float)):
            return (bool(input),)

        text = str(input).strip().lower()
        if text in ("true", "1", "yes", "y", "on"):
            return (True,)
        if text in ("false", "0", "no", "n", "off"):
            return (False,)

        return (False,)
