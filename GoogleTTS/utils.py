import base64
from enum import Enum


def b64_to_audio(b64: str) -> bytes:
    audio_bytes = base64.b64decode(s=b64)
    return audio_bytes


class SsmlGender(str, Enum):
    UNSPECIFIED = "SSML_VOICE_GENDER_UNSPECIFIED"
    MALE = "MALE"
    FEMALE = "FEMALE"


class AudioEncoding(str, Enum):
    UNSPECIFIED = "AUDIO_ENCODING_UNSPECIFIED"
    LINEAR16 = "LINEAR16"
    MP3 = "MP3"
    OGG_OPUS = "OGG_OPUS"
    MULAW = "MULAW"
    ALAW = "ALAW"


extensions: dict = {
    AudioEncoding.LINEAR16: ".wav",
    AudioEncoding.MP3: ".mp3",
    AudioEncoding.OGG_OPUS: ".ogg",
    AudioEncoding.MULAW: ".wav",
    AudioEncoding.ALAW: "wav"
}
