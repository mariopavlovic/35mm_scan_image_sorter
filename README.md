# Scan Sorter

A Python utility to sort and update metadata of scanned images based on their filenames.

## Description

This tool is designed to help organize scanned images where the metadata (creation date) doesn't match the intended order. It works with JPEG images that follow a specific naming pattern: `[project_number]-[auto_incremented_id].jpg` (e.g., `38384-000383840001.jpg`).

The script will:
1. Sort images based on their ID number
2. Update their metadata (creation date) in sequential order
3. Set the first image's creation date to the current time
4. Each subsequent image will have a creation date one second later than the previous one

## Requirements

- Python 3.x
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone git@github.com:mariopavlovic/35mm_scan_image_sorter.git
cd 35mm_scan_image_sorter
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your images in the `Images` directory
2. Run the script:
```bash
python sort_images.py
```

The script will process all JPEG files in the `Images` directory and update their metadata with sequential creation times.

## Notes

- The script preserves the original image quality and only modifies the metadata
- Images should follow the naming pattern: `[project_number]-[auto_incremented_id].jpg`
- The script will print progress as it processes each file

## License

MIT License

Copyright (c) 2024 Mario Pavlovic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 