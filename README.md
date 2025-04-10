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
