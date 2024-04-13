
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
            "top": 200,
            "left": 2420,
            "width": 500,
            "height": 300,
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
    
    # cv.THRESH_BINARY
    # cv.THRESH_BINARY_INV
    # cv.THRESH_TRUNC
    # cv.THRESH_TOZERO
    # cv.THRESH_TOZERO_INV

    thresh = cv2.adaptiveThreshold(gray, 180, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)

    # Save the preprocessed image
    cv2.imwrite('preprocessed.png', thresh)

    # Apply OCR to the preprocessed image
    text = pytesseract.image_to_string(Image.open('preprocessed.png'))
    if text.find('TOTAL TRANSPORTED') == -1:
        position = text.find('TOTAL EXTRACTION')
    else:
        position = text.find('TOTAL TRANSPORTED')
    # print(text)
    # define multiplier, as 1.2B/S > 1.3 M/S
    multiplier = 1
    if text.find('M/S') != -1:
        multiplier=10**6
    if text.find('B/S') != -1:
        multiplier=10**7

    text_init = text[position+19:position+25]
    print(text_init)
    match = re.search(r"(\d+)", text_init)
    if match:
        print(f"found {match.group(1)}")
        return float(match.group(1)*multiplier)
    else:
        print("wasn't able to extract value")
        return -1

get_capacity()