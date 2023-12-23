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


class AudioProfileID(str, Enum):
    WEARABLE_CLASS_DEVICE = "wearable-class-device"
    HANDSET_CLASS_DEVICE = "handset-class-device"
    HEADPHONE_CLASS_DEVICE = "headphone-class-device"
    SMALL_BLUETOOTH_SPEAKER_CLASS_DEVICE = "small-bluetooth-speaker-class-device"
    MEDIUM_BLUETOOTH_SPEAKER_CLASS_DEVICE = "medium-bluetooth-speaker-class-device"
    LARGE_BLUETOOTH_SPEAKER_CLASS_DEVICE = "large-home-entertainment-class-device"
    LARGE_AUTOMOTIVE_CLASS_DEVICE = "large-automotive-class-device"
    TELEPHONY_CLASS_DEVICE = "telephony-class-application"


class SynthesisType(str, Enum):
    TEXT = "text"
    SSML = "ssml"
