# Simple Captcha Solver

**[简体中文](README.md) | English**

A simple and easy-to-use Python tool for recognizing graphical captchas. It supports loading images from URLs or local paths and uses `ddddocr` for recognition.

## Features
1. **Multi-language Support**: Automatically switches between Chinese and English interfaces based on the system language.
2. **Image Download**: Supports downloading captcha images from URLs.
3. **Local File Support**: Supports loading images directly from local paths.
4. **Multiple File Format Support**: Supports various image formats.
5. **Cache Cleanup**: Automatically cleans up cached files to avoid excessive disk space usage.
6. **Error Handling**: Handles common errors and provides friendly error messages.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-captcha-solver.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If the `requirements.txt` file is not available, you can manually install the dependencies:
   ```bash
   pip install ddddocr requests
   ```

## Usage
### 1. Calling via Command Line Arguments
Run the following command:
```bash
python main.py -f <image_url_or_path>
```

#### Examples
- **Recognize Captcha from URL**:
  ```bash
  python main.py -f https://example.com/captcha.jpg
  ```
- **Recognize Captcha from Local Path**:
  ```bash
  python main.py -f ./captcha.jpg
  ```

### 2. Interactive Input
If the `-f` parameter is not provided, the program will prompt for the image URL or path:
```bash
python main.py
```

#### Example
```bash
Please enter the image URL or path: https://example.com/captcha.jpg
```

### 3. Output Results
- **Recognition Success**:
  ```
  Captcha text: 1234
  ```
- **Recognition Failure**:
  ```
  Error occurred during solving captcha: Unable to recognize captcha
  ```

## Code Structure
```plaintext
simple-captcha-solver/
├── main.py                # Main program entry
├── captcha_solver.py/     # Captcha recognition module
├── requirements.txt       # Dependency file
├── test_image/            # Test images
│   ├── test.png
│   ├── test.bmp
│   ├── test.jpg
│   ├── test.webp
├── README.md              # Project documentation
└── LICENSE                # Open source license
```

## Parameter Description
| Parameter | Description |
|-----------|-------------|
| `-f`      | Specify the URL or local path of the captcha image |
| `-h`      | Display help information and exit |

## Example Runs
### 1. Recognize Captcha from URL
```bash
$ python main.py -f https://example.com/captcha.jpg
Captcha text: 1234
```

### 2. Recognize Captcha from Local Path
```bash
$ python main.py -f ./captcha.jpg
Captcha text: 5678
```

### 3. Interactive Input
```bash
$ python main.py
Please enter the image URL or path: https://example.com/captcha.jpg
Image downloaded successfully.
Captcha text: 1234
```

## Notes
1. **Dependencies**:
   - `ddddocr`: Used for captcha recognition.
   - `requests`: Used for downloading images from URLs.
2. **Cache Cleanup**:
   - The program caches downloaded images in the `pic_cache` directory and automatically cleans them up after execution.
3. **Language Support**:
   - The program automatically switches to Chinese or English based on the system language.

## Contribution Guide
We welcome contributions of code or suggestions for improvements! If you encounter any issues or have new feature requests, please submit an [Issue](https://github.com/yourusername/simple-captcha-solver/issues).

## Open Source License
This project is licensed under the [GPL-3.0 License](LICENSE).

