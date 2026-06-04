import json

from .any_type import any_type


class JsonFrameExtractor:
    """
    Gelen JSON'u (title / total_frames / frames[]) ayrıştırır.

    Her frame'in "type" alanına göre promptları iki ayrı listeye böler:
      - text_to_image  -> prompt genelde bir dict (Subject/Location/Style...)
      - image_to_image -> prompt genelde bir string

    Prompt listeleri OUTPUT_IS_LIST ile işaretlidir; böylece ComfyUI'nın
    kendi batch mekanizması listedeki her prompt için downstream node'ları
    (KSampler vb.) sırayla bir kez çalıştırır.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": (any_type,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT", "INT", "STRING", "STRING")
    RETURN_NAMES = (
        "text_to_image_prompts",
        "image_to_image_prompts",
        "text_to_image_count",
        "image_to_image_count",
        "total_frames",
        "text_to_image_preview",
        "image_to_image_preview",
    )
    # İlk iki çıktı liste (batch için). Geri kalanlar tekil:
    # sayılar + insan-okur önizleme metinleri (Show Text'e bağlamak için).
    OUTPUT_IS_LIST = (True, True, False, False, False, False, False)
    FUNCTION = "extract"
    CATEGORY = "zfr-nodes"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("nan")

    def _parse_input(self, json_input):
        if isinstance(json_input, str):
            try:
                return json.loads(json_input)
            except Exception:
                return {}
        if isinstance(json_input, dict):
            return json_input
        return {}

    def _prompt_to_text(self, prompt):
        if isinstance(prompt, dict):
            lines = []
            for key, value in prompt.items():
                lines.append(f"{key}: {value}")
            return "\n".join(lines)
        if isinstance(prompt, list):
            return "\n".join(self._prompt_to_text(item) for item in prompt)
        return str(prompt)

    def extract(self, json_input):
        data = self._parse_input(json_input)

        frames = data.get("frames", [])
        if not isinstance(frames, list):
            frames = []

        text_to_image_prompts = []
        image_to_image_prompts = []

        for frame in frames:
            if not isinstance(frame, dict):
                continue

            prompt = frame.get("prompt")
            frame_type = frame.get("type")

            if frame_type == "text_to_image":
                text_to_image_prompts.append(self._prompt_to_text(prompt))
            elif frame_type == "image_to_image":
                image_to_image_prompts.append(self._prompt_to_text(prompt))

        text_to_image_count = len(text_to_image_prompts)
        image_to_image_count = len(image_to_image_prompts)

        total_frames = data.get("total_frames")
        if total_frames is None:
            total_frames = len(frames)
        try:
            total_frames = int(total_frames)
        except Exception:
            total_frames = len(frames)

        # Debug/önizleme: tüm promptları tek metinde numaralandırılmış göster.
        t2i_preview = self._build_preview("text_to_image", text_to_image_prompts)
        i2i_preview = self._build_preview("image_to_image", image_to_image_prompts)

        # OUTPUT_IS_LIST nedeniyle liste çıktılar liste KALMALI (tek elemanlı olsa bile).
        # Tekil çıktılar batch ile çoğalmasın diye tek elemanlı listeye sarılır.
        return (
            text_to_image_prompts,
            image_to_image_prompts,
            [text_to_image_count],
            [image_to_image_count],
            [total_frames],
            [t2i_preview],
            [i2i_preview],
        )

    def _build_preview(self, label, prompts):
        header = f"=== {label} | {len(prompts)} adet ==="
        if not prompts:
            return header + "\n(yok)"
        body = "\n\n".join(
            f"[{i}/{len(prompts)}] {p}" for i, p in enumerate(prompts, 1)
        )
        return f"{header}\n\n{body}"
