# Extracting Information from Images with OpenCV and Tesseract
This guide outlines the installation of `OpenCV` and `Tesseract`, essential tools for extracting text from images, especially when dealing with poor image quality.

### Installation `OpenCV` :
Ubuntu/Debian:
```
sudo apt update
sudo apt install python3-opencv
```

Windows:

Use the `pip` package manager for Python:
```
pip install opencv-python
```

Tesseract OCR is crucial for pytesseract to function. Install it before proceeding:
### Installation `Tesseract OCR` :

Ubuntu/Debian:
```
sudo apt update
sudo apt install tesseract-ocr
# Install language packs (e.g., Portuguese):
sudo apt install tesseract-ocr-por
```

Windows:
>Download Tesseract OCR from the official GitHub repository: https://github.com/tesseract-ocr/tesseract
Extract the downloaded archive and add the Tesseract installation directory to your system's `PATH` environment variable.

Finding the pytesseract Executable (Windows):
1. Locate Python Installation:
   * Python is typically installed in `C:\PythonXX` (replace `XX` with your version, e.g., `C:\Python39`).
2. Navigate to the `Scripts` Folder:
   * Go to the `Scripts` subfolder within your Python installation directory (e.g., `C:\Python39\Scripts`).
3. Find the pytesseract Executable:
   * Look for `pytesseract.exe` in the `Scripts` folder.
4. Copy the Executable Path:
   * Right-click on `pytesseract.exe`, select "Properties," and copy the full file path displayed.
  
Example Python Code:
```
  import cv2  # Import OpenCV library
  
  # Read the image
  image = cv2.imread("images/email.JPG")  # Replace with your image path
  
  # Set the path to Tesseract OCR executable (replace with your path)
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  
  # Extract text using Tesseract
  text = pytesseract.image_to_string(image)
  
  # Print the extracted text
  print("Extracted Text:", text)
```
