# Image Steganography — Hide & Extract Text

A Python-based **image steganography utility** that allows users to hide short text messages inside images and extract the hidden messages when required.

The project uses **LSB (Least Significant Bit) steganography**, where the least significant bits of the image's RGB pixel values are modified to store the message.

## Features

* Hide text messages inside images
* Extract hidden messages from stego images
* Check approximate message capacity of an image
* Supports **PNG and BMP** image formats
* Checks message size against available image capacity
* Simple command-line interface
* Includes cover image, stego image, and extraction proof

## Technologies Used

* **Python 3**
* **Pillow (PIL)**

## Project Structure

```text
Steganography-Text-in-Image/
│
├── stenographer.py
├── README.md
├── requirements.txt
│
├── images/
│   ├── cover.png
│   └── stego.png
│
└── proof/
    └── extraction_proof.png
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Steganography-Text-in-Image.git
cd Steganography-Text-in-Image
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python stenographer.py
```

The program provides four options:

```text
1. Hide message
2. Extract message
3. Check image capacity
4. Exit
```

### 1. Hide a Message

Select option `1` and provide the cover image, output stego image, and message.

Example:

```text
Enter your choice: 1
Enter cover image path: cover.png
Enter output stego image path: stego.png
Enter message to hide: Cybersecurity is about protecting data, systems, and information.
```

The program creates a new image named `stego.png` containing the hidden message.

### 2. Extract a Message

Select option `2` and provide the stego image:

```text
Enter your choice: 2
Enter stego image path: stego.png
```

Example output:

```text
Message successfully extracted!
--------------------------------
Hidden Message:
Cybersecurity is about protecting data, systems, and information.
--------------------------------
```

### 3. Check Image Capacity

Select option `3` to check the approximate number of characters that can be stored in an image.

Example:

```text
Image Capacity
----------------
Image Size : 1024 x 768
Capacity   : approximately 294903 characters
```

## Supported Formats

The utility supports:

* **PNG** (`.png`)
* **BMP** (`.bmp`)

JPEG/JPG images are not recommended because lossy compression can modify pixel values and corrupt the hidden data.

## Capacity Limitations

The message capacity depends on the dimensions of the image.

This implementation uses the RGB channels of each pixel and stores approximately **1 bit per color channel**.

Therefore:

```text
Total available bits = Width × Height × 3
```

The actual usable text capacity is slightly lower because the program uses a delimiter to identify the end of the hidden message.

Larger images can store longer messages.

## Testing & Verification

The implementation was tested by:

1. Hiding a text message inside `cover.png`
2. Generating `stego.png`
3. Extracting the message from `stego.png`
4. Comparing the extracted message with the original message

### Test Message

```text
Cybersecurity is about protecting data, systems, and information.
```

The hidden message was successfully extracted from the generated stego image.

## Limitations

* Intended for **short text messages**
* Supports only PNG and BMP formats
* JPEG/JPG should not be used for storing hidden data
* Steganography does not encrypt the message; it only hides its presence
* Image editing, resizing, compression, or format conversion may destroy the hidden message
* The stego image may contain detectable statistical changes if analyzed with specialized steganalysis tools

## Learning Outcomes

Through this project, I learned about:

* Image steganography
* LSB-based data hiding
* RGB pixel manipulation
* Message capacity calculation
* Data extraction and verification
* Limitations of image-based information hiding

## Author

**Bhavya**
