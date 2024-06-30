# Extracting-Information-from-Images
If the image quality is poor and it is not possible to extract the information, it will be necessary to use both `OpenCV` and `Tesseract` to process the image.

### Installation Guide for OpenCV and Tesseract

#### OpenCV Installation

- **Ubuntu:**
  ```bash
  sudo apt update
  sudo apt install python3-opencv
  ```

- **Windows:**
  ```bash
  pip install opencv-python
  ```


#### Tesseract Installation

- **Ubunto:**
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  sudo apt install tesseract-ocr-por # Install Portuguese language support if needed
  ```

- **Windows:**
 ```bash
  pip install pytesseract
```

### Finding the pytesseract Executable

1. **Locate the Python Installation:**
   - Python is typically installed in `C:\PythonXX`, where `XX` denotes the Python version (e.g., `C:\Python39` for Python 3.9).

2. **Navigate to the Scripts Folder:**
   - Go to the `Scripts` subfolder within your Python installation directory (e.g., `C:\Python39\Scripts`).

3. **Find the pytesseract Executable:**
   - Inside the `Scripts` folder, look for `pytesseract.exe`.

4. **Copy the Executable Path:**
   - Right-click on `pytesseract.exe`, select "Properties," and copy the full file path displayed in the properties window.
