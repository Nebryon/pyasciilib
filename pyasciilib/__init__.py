"""
https://github.com/Slinky802/pyasciilib

pyasciilib is a library created by Alexandre Poggioli
    https://slinky-presentation.netlify.app

This library allows converting an image into ASCII using different methods.
It supports multiple languages and offers various customization options.

The supported languages are English, French, Spanish, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean, and Arabic.

Use pyasciilib.ascii_help(language) to display the library's usage instructions in the selected language ("en" by default).


⊂(◉‿◉)つ
"""

import inspect
from PIL import Image
from .to_ascii import *

__all__ = [name for name, obj in inspect.getmembers(to_ascii) if inspect.isfunction(obj)]
#__all__ += [name for name, obj in inspect.getmembers(to_image) if inspect.isfunction(obj)]

print("\nWelcome to pyasciilib by Alexandre Poggioli !")
print("pyasciilib.pyasciilib_help() to get some help")
#print("Fonctions disponibles :", __all__)
print()