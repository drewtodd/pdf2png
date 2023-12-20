import os
import fitz  # PyMuPDF
from PIL import Image

# Define the folder containing your PDF files
pdf_folder = "/Users/atodd/Desktop/HPSCANS/upload/"

# Define the output folder for the converted images
output_folder = "/Users/atodd/Desktop/HPSCANS/png/"

# Define the minimum width for the images
min_width = 1600

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the PDF folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        # Construct the full path to the PDF file
        pdf_file = os.path.join(pdf_folder, filename)

        # Open the PDF file
        pdf_document = fitz.open(pdf_file)

        # Loop through each page in the PDF
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_number]

            # Convert the page to an image (PNG)
            pix = page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Calculate the new height to maintain aspect ratio
            new_width = min_width
            aspect_ratio = image.width / image.height
            new_height = int(new_width / aspect_ratio)

            # Resize the image to the specified width
            image = image.resize((new_width, new_height), Image.LANCZOS)

            # Define the output image file name
            output_image_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_page_{page_number + 1}.png")

            # Save the resized image as PNG
            image.save(output_image_file, "png")

        # Close the PDF document
        pdf_document.close()

print("Conversion complete. Images saved in the output folder with a minimum width of 1600 pixels.")
