# Import the 'qrcode' library to generate QR codes
import qrcode

# Import the 'Image' class from the 'PIL' library to handle image operations
from PIL import Image

# Define a function named 'create_qrcode' to generate and save a QR code
def create_qrcode(data):
    # Create a QR code object with specific settings
    qr = qrcode.QRCode(
        version=1,  # Set the version of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Set error correction level to Low
        box_size=2,  # Set the size of each box in the QR code
        border=1,  # Set the width of the border around the QR code
    )
    # Add the data to the QR code object
    qr.add_data(data)
    # Adjust the QR code object to fit the data
    qr.make(fit=True)
    # Create an image from the QR code object
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the QR code image as a PDF file to the specified file path
    img.save('/YOUR/FILEPATH/HERE/MyInfoSmallQR.pdf', "PDF")

# Define personal information variables
name = "Property Of: Your Name"  # User's name
phone = "tel:+1234567890"  # User's phone number in tel URI format
email = "mailto:email@example.com"  # User's email address in mailto URI format
whatsapp_url = "https://wa.me/1234567890"  # User's WhatsApp URL

# Format the data to include each piece of information on a new line
data = f"{name}\n{phone}\n{email}\n{whatsapp_url}"

# Call the 'create_qrcode' function to generate and save the QR code
create_qrcode(data)
