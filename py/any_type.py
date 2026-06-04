class AnyType(str):
    """ComfyUI'da her tipi kabul eden / her tiple eşleşen özel string tipi."""

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    def __hash__(self):
        return hash(str(self))


any_type = AnyType("*")
