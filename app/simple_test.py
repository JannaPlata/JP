from paddleocr import PaddleOCR
import urllib.request

# Initialize
ocr = PaddleOCR(lang='en')

# Download a simple image
url = "https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/release/2.7/doc/imgs_en/254.jpg"
urllib.request.urlretrieve(url, "test.jpg")

# Run OCR
result = ocr.ocr("test.jpg")

# Print first few characters of result to see structure
print(str(result)[:500])