# pyascii

**pyascii** is a Python library for converting images into ASCII art, using various methods and supporting several languages. It offers customization options, such as output size, ASCII characters used, and output format (text or list of lists).

## Contents
- [Installation](#installation)
- [Use](#use)
- [Features](#features)
- [Customization options](#customization-options)
- [Supported languages](#supported-languages)
- [License](#license)

---

## Installation

To install the library, use pip :

``` bash
pip install pyascii
```

---

## Usage
Basic example of converting an image to ASCII:

```python
import pyascii

# Converts an image to ASCII with default parameters
ascii_art = pyascii.image_to_ascii(
    image_link=“path/to/image.jpg”,
    method=“text”,
    size=(100, 100),
    charset=None
)

print(ascii_art)
```

---

## Features


**Flexible Output Format:** Returns the result either as printable ASCII text, or as a list of character lists.

**Output Size:** Defines the dimensions (width, height) of the output ASCII image.

**ASCII characters:** Modifies the list of ASCII characters used, from more to less dense, to obtain the desired output.

**Return Method:** Choice between “list” (list of lists) or “text” (printable text) for output format.

**Supported languages:**

 - en : English

 - fr : French

 - es : Spanish

 - de : German

 - it: Italian

 - pt: Portuguese

 - ru: Russian

 - zh: Chinese

 - ja: Japanese

 - ko: Korean

 - ar : Arabic

Use ```pyascii.ascii_help(language)``` to display instructions according to the selected language.

---

## License
This project is licensed under the MIT license - see the LICENSE file for details.

---

## Contact
Created by Alexandre Poggioli - alexandrepoggioli09@gmail.com

More information on https://slinky-presentation.netlify.app