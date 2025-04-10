import os
from PIL import Image
import piexif
from datetime import datetime, timedelta
import re

def get_image_id(filename):
    """Extract the ID number from the filename."""
    match = re.search(r'(\d+)-(\d+)\.jpg$', filename)
    if match:
        return int(match.group(2))
    return 0

def update_image_metadata(image_path, creation_time):
    """Update the image's EXIF metadata with the new creation time while preserving original quality."""
    try:
        # Load the image
        img = Image.open(image_path)
        
        # Get existing EXIF data or create new if none exists
        try:
            exif_dict = piexif.load(img.info['exif'])
        except:
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
        
        # Convert datetime to EXIF format
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = creation_time.strftime("%Y:%m:%d %H:%M:%S")
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = creation_time.strftime("%Y:%m:%d %H:%M:%S")
        
        # Save the updated EXIF data while preserving original quality
        exif_bytes = piexif.dump(exif_dict)
        
        # Save with original quality settings
        img.save(image_path, 
                "jpeg", 
                exif=exif_bytes,
                quality='keep',  # Preserve original quality
                optimize=False,  # Don't optimize to prevent quality changes
                subsampling=0)   # Keep original subsampling
        
        img.close()
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def main():
    # Directory containing the images
    images_dir = "Images"
    
    # Get all JPEG files
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith('.jpg')]
    
    # Sort files by their ID number
    image_files.sort(key=get_image_id)
    
    # Get current time
    current_time = datetime.now()
    
    # Process each image
    for i, filename in enumerate(image_files):
        image_path = os.path.join(images_dir, filename)
        # Calculate creation time (current time + i seconds)
        creation_time = current_time + timedelta(seconds=i)
        print(f"Processing {filename} - Setting creation time to {creation_time}")
        update_image_metadata(image_path, creation_time)

if __name__ == "__main__":
    main() 