# Simple Captcha Solver

**English | [简体中文](README.md)**

A simple and easy-to-use Python tool for recognizing captcha images. It supports loading images from a URL or local path and uses `ddddocr` for recognition.

## Features

- Supports single captcha recognition (from a local file or network URL)
- Supports batch processing of all image files in a directory
- Supports batch captcha recognition based on a list of URLs in a text file
- Automatically detects system language settings and adjusts output language (Chinese or English)
- Provides command-line argument support for direct execution of specific tasks

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-captcha-solver.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If there is no `requirements.txt` file, you can manually install the dependencies:
   ```bash
   pip install ddddocr requests
   ```

## Usage
### 1. Invoke with Command-Line Arguments

When running the script, you can specify the following arguments:

- `-f <url_or_path>`: Recognize a captcha from the provided URL or file path.
- `-d <directory>`: Batch recognize all files in the specified directory.
- `-i <url_file>`: Batch recognize captchas from URLs listed in the provided text file.

Examples:

```bash
python captcha_tool.py -f "http://example.com/captcha.jpg"
python captcha_tool.py -d "/path/to/directory"
python captcha_tool.py -i "/path/to/urls.txt"
```

### 2. Interactive Input

If no command-line arguments are specified, the program will display an interactive menu where you can select the corresponding function by entering a number:

1. Recognize a single file or URL
2. Batch recognize all files in a directory
3. Batch recognize online URLs
4. Exit the program

Follow the prompts to enter relevant information to start the recognition process.


## Code Structure
```plaintext
simple-captcha-solver/
├── main.py                # Main program entry point
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


## Notes
1. **Dependencies**:
   - `ddddocr`: Used for captcha recognition.
   - `requests`: Used for downloading images from URLs.
2. **Cache Cleanup**:
   - The program caches downloaded images in the `pic_cache` directory and automatically cleans up after execution.
3. **Language Support**:
   - The program automatically switches between Chinese and English based on system language settings.

## Contribution Guide
Contributions are welcome! If you find any issues or have suggestions for new features, please submit an [Issue](https://github.com/yourusername/simple-captcha-solver/issues).

## Open Source License
This project is licensed under the [GPL-3.0 License](LICENSE).