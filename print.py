import urllib.request
from PIL import Image
from escpos.printer import Serial

url = "https://fastly.picsum.photos/id/63/5000/2813.jpg?hmac=HvaeSK6WT-G9bYF_CyB2m1ARQirL8UMnygdU9W6PDvM"
img = Image.open(urllib.request.urlopen(url))
# Initialize the serial printer on /dev/serial0
# Match your printer's baud rate (usually 9600 or 19200)
p = Serial(
    devfile='/dev/serial0',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1.0,
    profile='PT280'
)

# Print an image (Pillow handles formatting/dithering automatically)
p.image(img)

# Feed paper and cut (if supported)
p.ln(2)
p.cut()