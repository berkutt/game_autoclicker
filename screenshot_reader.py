
import pytesseract
from PIL import Image
import cv2
import mss
import mss.tools
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_capacity():
    with mss.mss() as sct:
        # Get information of monitor 2
        monitor_number = 2
        mon = sct.monitors[monitor_number]

        # The screen part to capture
        monitor = {
            "top": 150,
            "left": 2420,
            "width": 1020,
            "height": 600,
            "mon": monitor_number,
        }
        output = "screenshot.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    # # Load the image from file
    image = cv2.imread('screenshot.png')

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 80, 180, cv2.THRESH_TRUNC)

    # Save the preprocessed image
    cv2.imwrite('preprocessed.png', thresh)

    # Apply OCR to the preprocessed image
    text = pytesseract.image_to_string(Image.open('preprocessed.png'))
    if text.find('TOTAL TRANSPORTED') == -1:
        position = text.find('TOTAL EXTRACTION')
    else:
        position = text.find('TOTAL TRANSPORTED')

    text_init = text[position+19:position+25]
    match = re.search(r"(\d+\.\d+)", text_init)
    if match:
        return float(match.group(1))
    else:
        return -1
# print(text)