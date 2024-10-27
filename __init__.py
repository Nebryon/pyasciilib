"""
https://github.com/Slinky802/pyimage2ascii

pyimage2ascii is a library created by Alexandre Poggioli
    https://slinky-presentation.netlify.app

This library allows converting an image into ASCII using different methods.
It supports multiple languages and offers various customization options.

The supported languages are English, French, Spanish, German, Italian, Portuguese, Russian, Chinese, Japanese, Korean, and Arabic.

Use pyimage2ascii.ascii_help(language) to display the library's usage instructions in the selected language ("en" by default).


⊂(◉‿◉)つ
"""

import inspect
from PIL import Image
from .to_ascii import *

__all__ = [name for name, obj in inspect.getmembers(to_ascii) if inspect.isfunction(obj)]
#__all__ += [name for name, obj in inspect.getmembers(to_image) if inspect.isfunction(obj)]

print("\nWelcome to pyimage2ascii by Alexandre Poggioli !")
print("pyimage2ascii.pyimage2ascii_help() to get some help")
#print("Fonctions disponibles :", __all__)
print()