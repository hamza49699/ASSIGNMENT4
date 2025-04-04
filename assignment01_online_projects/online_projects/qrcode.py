# Import the qrcode library to generate QR codes
import qrcode

# Define the data to be encoded in the QR code
data = 'QR code using make() function'

# Generate the QR code using the make() function
img = qrcode.make(data)

# Save the generated QR code as an image file
img.save('qr_code_QR_encoder_decoder.png')
