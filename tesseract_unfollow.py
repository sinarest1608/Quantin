def extract(image):
    from PIL import Image
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r"tesseract"
    image = Image.open(image)
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    return image_to_text
