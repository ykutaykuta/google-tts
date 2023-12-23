import logging
from typing import Optional

import requests

from GoogleTTS.utils import *

# Logger
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class GoogleTTS:
    def __init__(self):
        self.__url = "https://content-texttospeech.googleapis.com/v1/text:synthesize"
        self.__x_referer = "https://explorer.apis.google.com"
        self.__key: str = "AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM"
        self.__language_code: str = "vi-VN"
        self.__ssml_gender: SsmlGender = SsmlGender.FEMALE

        self.__audio_encoding: AudioEncoding = AudioEncoding.MP3
        self.__pitch: float = 0.0
        self.__volume_gain_db: float = 0.0
        self.__sample_rate_hertz: int = 48000
        self.__effects_profile_id: AudioProfileID | None = None
        self.__speaking_rate: float = 1.0

    def set_key(self, key: str):
        self.__key = key

    def set_language_code(self, lang_code: str):
        self.__language_code = lang_code

    def set_ssml_gender(self, gender: SsmlGender):
        self.__ssml_gender = gender

    def set_audio_encoding(self, encoding: AudioEncoding):
        self.__audio_encoding = encoding

    def set_sample_rate(self, rate: int):
        self.__sample_rate_hertz = rate

    def set_speaking_rate(self, rate: float):
        self.__speaking_rate = rate

    def set_pitch(self, pitch: float):
        self.__pitch = pitch

    def set_volume_gain_db(self, volume_gain_db: float):
        self.__volume_gain_db = volume_gain_db

    def set_effects_profile_id(self, effects_profile_id: AudioProfileID | None):
        self.__effects_profile_id = effects_profile_id

    def __prepare_body(self, text: str) -> dict:
        _input: dict = {"text": text}
        _voice: dict = {
            "languageCode": self.__language_code,
            "ssmlGender": self.__ssml_gender
        }
        _audioConfig: dict = {
            "audioEncoding": self.__audio_encoding,
            "speakingRate": self.__speaking_rate,
            "pitch": self.__pitch,
            "volumeGainDb": self.__volume_gain_db,
            "sampleRateHertz": self.__sample_rate_hertz,
            "effectsProfileId": [
                self.__effects_profile_id
            ]
        }
        body: dict = {
            "input": _input,
            "voice": _voice,
            "audioConfig": _audioConfig
        }
        return body

    def __prepare_params(self) -> dict:
        params: dict = {
            "alt": "json",
            "key": self.__key
        }
        return params

    def __prepare_headers(self) -> dict:
        headers: dict = {
            "x-referer": self.__x_referer
        }
        return headers

    def __save_to_file(self, save_file: str, data: bytes):
        index = save_file.rfind(".")
        if index != -1:
            extension = save_file[index:].lower()
            if self.__audio_encoding != AudioEncoding.UNSPECIFIED and extension != extensions[self.__audio_encoding]:
                log.warning(f"Recommend using the extension '{extensions[self.__audio_encoding]}' for encoding '{self.__audio_encoding}'")
        else:
            log.warning(f"Cannot find extension of file '{save_file}'!!!")
        with open(save_file, "wb") as f:
            f.write(data)

    def tts(self, text: str, save_file: Optional[str] = None) -> dict:
        """Do the TTS API request.

        Args:
            text (string): the text need to process text-to-speech.
            save_file (Optional[str]): The path and file name to save the ``audio`` to, default value is ``None``.

        Returns:
            dict: On success return dict contain base64 audio data with key ``audioContent``.
                On failed return dict error detail ``{"error": {"code": int, "message": str, "status": str}}
        """

        headers = self.__prepare_headers()
        body = self.__prepare_body(text=text)
        params = self.__prepare_params()
        r = requests.post(self.__url, json=body, params=params, headers=headers)
        if r.status_code == 200:
            res_body = r.json()
            audio_content = res_body["audioContent"]
            audio_bytes = b64_to_audio(b64=audio_content)
            if save_file is not None:
                self.__save_to_file(save_file=save_file, data=audio_bytes)
        return r.json()
