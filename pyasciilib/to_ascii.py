def ascii_help(lang: str = "en") -> None:
    """This function displays the usage instructions for the library based on the selected language."""

    translations = {
    "en": """The function image_to_ascii takes an image link as input (str), a return method ("list" for a list of lists, "text" for directly printable text), a size (tuple = width, height) for the output image, which defaults to the same as the input, as well as an optional modifiable list of ASCII characters to use from most to least dense to transform the image into ASCII.
The function array_to_ascii takes a list of lists containing the brightness of each pixel (between 0 and 255), a return method ("list" for a list of lists, "text" for directly printable text), as well as an optional modifiable list of ASCII characters to use from most to least dense to transform the image into ASCII.""",

    "fr": """La fonction image_to_ascii prend le lien d'une image en entrée (str), une méthode de retour ("list" pour une liste de listes, "text" pour un texte directement imprimable), une taille (tuple = largeur, hauteur) pour l'image de sortie, qui est par défaut la même que celle d'entrée, ainsi qu'une liste modifiable de caractères ASCII à utiliser du plus au moins dense pour transformer l'image en ASCII.
La fonction array_to_ascii prend une liste de listes contenant la luminosité de chaque pixel (entre 0 et 255), une méthode de retour ("list" pour une liste de listes, "text" pour un texte directement imprimable), ainsi qu'une liste modifiable de caractères ASCII à utiliser du plus au moins dense pour transformer l'image en ASCII.""",

    "es": """La función image_to_ascii toma un enlace de imagen como entrada (str), un método de retorno ("list" para una lista de listas, "text" para texto directamente imprimible), un tamaño (tupla = ancho, alto) para la imagen de salida, que por defecto es igual al de entrada, así como una lista modificable de caracteres ASCII opcional para usar de mayor a menor densidad para transformar la imagen en ASCII.
La función array_to_ascii toma una lista de listas que contiene el brillo de cada píxel (entre 0 y 255), un método de retorno ("list" para una lista de listas, "text" para texto directamente imprimible), así como una lista modificable de caracteres ASCII opcional para usar de mayor a menor densidad para transformar la imagen en ASCII.""",

    "pt": """A função image_to_ascii recebe um link de imagem como entrada (str), um método de retorno ("list" para uma lista de listas, "text" para texto diretamente imprimível), um tamanho (tupla = largura, altura) para a imagem de saída, que por padrão é o mesmo da entrada, bem como uma lista opcional de caracteres ASCII modificáveis para usar do mais ao menos denso para transformar a imagem em ASCII.
A função array_to_ascii recebe uma lista de listas contendo o brilho de cada pixel (entre 0 e 255), um método de retorno ("list" para uma lista de listas, "text" para texto diretamente imprimível), bem como uma lista opcional de caracteres ASCII modificáveis para usar do mais ao menos denso para transformar a imagem em ASCII.""",

    "de": """Die Funktion image_to_ascii nimmt einen Bildlink als Eingabe (str), eine Rückgabemethode ("list" für eine Liste von Listen, "text" für direkt druckbaren Text), eine Größe (Tupel = Breite, Höhe) für das Ausgabebild, die standardmäßig der Eingabegröße entspricht, sowie eine optionale modifizierbare Liste von ASCII-Zeichen, die von am dichtesten bis am wenigsten dicht verwendet werden, um das Bild in ASCII umzuwandeln.
Die Funktion array_to_ascii nimmt eine Liste von Listen, die die Helligkeit jedes Pixels (zwischen 0 und 255) enthalten, eine Rückgabemethode ("list" für eine Liste von Listen, "text" für direkt druckbaren Text), sowie eine optionale modifizierbare Liste von ASCII-Zeichen, die von am dichtesten bis am wenigsten dicht verwendet werden, um das Bild in ASCII umzuwandeln.""",

    "it": """La funzione image_to_ascii prende un link di immagine come input (str), un metodo di ritorno ("list" per una lista di liste, "text" per testo direttamente stampabile), una dimensione (tupla = larghezza, altezza) per l'immagine di output che di default è uguale a quella di input, così come una lista modificabile opzionale di caratteri ASCII da usare dal più al meno denso per trasformare l'immagine in ASCII.
La funzione array_to_ascii prende una lista di liste contenente la luminosità di ciascun pixel (tra 0 e 255), un metodo di ritorno ("list" per una lista di liste, "text" per testo direttamente stampabile), così come una lista modificabile opzionale di caratteri ASCII da usare dal più al meno denso per trasformare l'immagine in ASCII.""",

    "ru": """Функция image_to_ascii принимает ссылку на изображение в качестве входных данных (str), метод возврата ("list" для списка списков, "text" для печатного текста), размер (кортеж = ширина, высота) для выходного изображения, который по умолчанию совпадает с входным, а также необязательный изменяемый список символов ASCII для использования от наиболее к наименее плотного для преобразования изображения в ASCII.
Функция array_to_ascii принимает список списков, содержащих яркость каждого пикселя (от 0 до 255), метод возврата ("list" для списка списков, "text" для печатного текста), а также необязательный изменяемый список символов ASCII для использования от наиболее к наименее плотного для преобразования изображения в ASCII.""",

    "zh": """image_to_ascii 函数接受图像链接作为输入（str），返回方法（“list”表示列表列表，“text”表示直接可打印的文本），输出图像的大小（元组=宽度，高度），默认为与输入相同，以及一个可选的可修改 ASCII 字符列表，用于从最密到最稀疏的字符来将图像转换为 ASCII。
array_to_ascii 函数接受包含每个像素亮度的列表（0 到 255 之间），返回方法（“list”表示列表列表，“text”表示直接可打印的文本)，以及一个可选的可修改 ASCII 字符列表，用于从最密到最稀疏的字符来将图像转换为 ASCII。""",

    "ja": """image_to_ascii 関数は、画像リンクを入力 (str) として受け取り、戻り方法 ("list" はリストのリスト、"text" は直接印刷可能なテキスト)、出力画像のサイズ (タプル = 幅、高さ) を指定し、デフォルトでは入力と同じサイズになります。また、最も密から最も希薄なものまでの可変 ASCII 文字リスト (オプション) を使用して、画像を ASCII に変換します。
array_to_ascii 関数は、各ピクセルの明るさ（0 から 255 の間）を含むリストを受け取り、戻り方法 ("list" はリストのリスト、"text" は直接印刷可能なテキスト) を指定し、最も密から最も希薄なものまでの可変 ASCII 文字リスト (オプション) を使用して、画像を ASCII に変換します。""",

    "ko": """image_to_ascii 함수는 이미지 링크를 입력 (str)으로 받고, 반환 방법("list"는 리스트의 리스트, "text"는 직접 인쇄 가능한 텍스트), 출력 이미지의 크기 (튜플 = 너비, 높이)를 입력과 동일하게 기본 설정하며, 밀도 높은 순서에서 낮은 순서로 사용할 수 있는 수정 가능한 ASCII 문자 목록 (선택 사항)을 사용하여 이미지를 ASCII로 변환합니다.
array_to_ascii 함수는 각 픽셀의 밝기 (0에서 255 사이)를 포함하는 리스트를 입력으로 받고, 반환 방법 ("list"는 리스트의 리스트, "text"는 직접 인쇄 가능한 텍스트)을 지정하며, 밀도 높은 순서에서 낮은 순서로 사용할 수 있는 수정 가능한 ASCII 문자 목록 (선택 사항)을 사용하여 이미지를 ASCII로 변환합니다.""",

    "ar": """تأخذ الدالة image_to_ascii رابط صورة كمدخل (str)، وطريقة الإرجاع ("list" لقائمة القوائم، "text" لنص يمكن طباعته مباشرة)، وحجم الصورة الناتجة (tuple = العرض، الارتفاع)، والذي يكون بشكل افتراضي نفس حجم الإدخال، بالإضافة إلى قائمة اختيارية قابلة للتعديل من أحرف ASCII للاستخدام من الأكثر كثافة إلى الأقل لتحويل الصورة إلى ASCII.
تأخذ الدالة array_to_ascii قائمة من القوائم تحتوي على سطوع كل بكسل (بين 0 و 255)، وطريقة الإرجاع ("list" لقائمة القوائم، "text" لنص يمكن طباعته مباشرة)، بالإضافة إلى قائمة اختيارية قابلة للتعديل من أحرف ASCII للاستخدام من الأكثر كثافة إلى الأقل لتحويل الصورة إلى ASCII.""",
    }

    print(translations.get(lang, "Language not supported."))
    print()

    
    
    
def image_to_ascii(path_to_image: str, returned: str, size: tuple = (0, 0), chars: list = ["@", "#", "%", "*", "+", "=", "-", ":", "."]):
    """
    This function takes as input : 
     - an image link (str), 
     - a return method ("list" for a list of lists, "text" for directly printable text), 
     - a size (tuple = width, height) for the output image which defaults to the same as the input,
     - an optional modifiable list of ASCII characters to use from most to least dense.
    """

    from PIL import Image

    image = Image.open(path_to_image).convert("L")

    if size == (0, 0):
        size =  image.size
    else :
        image = image.resize(size)

    image_array = []
    for h in range(size[1]):
        line = []
        for w in range(size[0]):
            pixel = image.getpixel((w, h))
            line.append(pixel)
        image_array.append(line)
    
    return array_to_ascii(image_array, returned, chars)




def array_to_ascii(image_array: list, returned: str, chars: list = ["@", "#", "%", "*", "+", "=", "-", ":", "."]):
    """
    This function takes as input : 
     - a list of lists which contains the brightness of each pixel (between 0 and 255), 
     - a return method ("list" for a list of lists, "text" for directly printable text), 
     - an optional modifiable list of ASCII characters to use from most to least dense.
    """

    tailles = [min(256,  256 * i // len(chars)) for i in range(len(chars) + 1)]

    ascii_array = []
    ascii_text = ""
    for y in image_array:
        texte_ligne = []
        for x in y:
            for count in range(len(chars)):
                if x in range(tailles[count], tailles[count+1]):
                    texte_ligne.append(chars[count])
                    ascii_text += chars[count] + " "
        ascii_array.append(texte_ligne)
        ascii_text += "\n"

    return ascii_array if returned == "list" else ascii_text