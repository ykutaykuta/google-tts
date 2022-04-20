import site
from codecs import open

from setuptools import setup

# PEP517
site.ENABLE_USER_SITE = True

exec(open('GoogleTTS/version.py').read())

setup(
    version=__version__  # type: ignore # noqa: F821
)
