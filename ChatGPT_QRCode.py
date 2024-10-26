import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://chatgpt.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("chatgpte.svg", scale = 8)