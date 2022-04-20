# google-tts
**google-tts** (*Google Text-to-Speech*), a Python library with Google text-to-speech API. 
Write spoken audio data to a file, or get Base64 encoding audio data 

[![PyPI version](https://img.shields.io/pypi/v/google-tts)](https://pypi.org/project/google-tts/)
[![Python versions](https://img.shields.io/pypi/pyversions/google-tts)](https://pypi.org/project/google-tts/)
[![Commits Since](https://img.shields.io/github/commits-since/ykutaykuta/google-tts/latest.svg)](https://github.com/ykutaykuta/google-tts/commits/)

## Features
-   Text length up to 5000 characters
-   Customizable speak-rate (0.25 - 4.0) and sample-rate
-   Audio encoding: LINEAR16, MP3, OGG-OPUS, MULAW, ALAW
-   MALE and FEMALE voice

### Installation
    $ pip install google-tts

### Quickstart
    from GoogleTTS import GoogleTTS
    tts = GoogleTTS()
    ret = tts.tts('Xin chào!', 'output.mp3')
    if 'audioContent' in ret:
        b64 = ret['audioContent']
    else:
        error = ret['error']
        code = error['code']
        message = error['message']
        status = error['status']

### Licence
[The MIT License (MIT)](LICENSE) Copyright © 2022 ykuta