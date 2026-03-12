from paddleocr import PaddleOCR
import urllib.request
import os

# Suppress warnings
os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'

print("Initializing PaddleOCR...")
print("This will download models on first run (40-50MB)...")
ocr = PaddleOCR(lang='en', use_angle_cls=True, show_log=False)

print("Downloading test image...")
url = "https://paddleocr.bj.bcebos.com/dygraph_v2.1/ppocr_img/imgs_en/img_12.jpg"
urllib.request.urlretrieve(url, "test.jpg")

print("Running OCR on test image...")
result = ocr.ocr('test.jpg', cls=True)

if result and result[0]:
    print("\n📝 Extracted Text:")
    for line in result[0]:
        print(f"  - {line[1][0]} (confidence: {line[1][1]:.2f})")
else:
    print("No text found in test image.")

print("\n✅ Test complete!")