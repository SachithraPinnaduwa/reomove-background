from tkinter import Tk, filedialog
from rembg import remove
from PIL import Image

def main():
    # Set up the Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )

    # Check if a file was selected
    if file_path:
        # Open the image
        image = Image.open(file_path)

        # Remove the background
        output = remove(image)

        # Save the output image
        output_path = file_path.rsplit('.', 1)[0] + '_removed.png'
        output.save(output_path)

        print(f"Background removed. Output saved as '{output_path}'")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
