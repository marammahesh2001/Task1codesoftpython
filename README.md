# Image-to-Sound and Binary Search Algorithm Project

This project consists of two distinct functionalities: converting image text to sound and performing a binary search on a sorted array. The first part uses the Tesseract OCR engine to extract text from an image and then converts it to speech using the gTTS library. The second part implements the binary search algorithm for a sorted list of integers.

## Image-to-Sound Conversion

### Setup

1. Install the required Python libraries:
    ```
    pip install Pillow
    pip install gTTS
    pip install pytesseract
    ```

2. Make sure Tesseract OCR is installed on your system and set the path to the Tesseract executable file:
    ```
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

### Usage

- Call the `convert_to_sound` function with the path to the image file as an argument.
- The function will extract text from the image, convert it to speech, and save it as an MP3 file.

## Binary Search Algorithm

### Description

The binary search algorithm implementation searches for an element in a sorted array and returns its index.

### Usage

- Define the list of integers you want to search through.
- Call the `binary_search_algo` function with the list and the target value as arguments.
- The function will return the index of the target if found; otherwise, it will return "Element Not Found".

### Example

```
a = [7, 3, 4, 5, 1, 2, 9]
a.sort()
s = int(input("Enter search: "))
print(binary_search_algo(a, s))
```

## Requirements

- Python 3.x
- The Tesseract OCR engine

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
