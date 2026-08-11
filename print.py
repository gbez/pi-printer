import urllib.request
from PIL import Image
from escpos.printer import Serial
from escpos.capabilities import Profile

url = "https://fastly.picsum.photos/id/63/5000/2813.jpg?hmac=HvaeSK6WT-G9bYF_CyB2m1ARQirL8UMnygdU9W6PDvM"
img = Image.open(urllib.request.urlopen(url))

my_profile = Profile()
my_profile.data['media']['width']['pixel'] = 384
# Initialize the serial printer on /dev/serial0
# Match your printer's baud rate (usually 9600 or 19200)
p = Serial(
    devfile='/dev/serial0',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1.0,
    profile=my_profile
)

# Print an image (Pillow handles formatting/dithering automatically)
p.image(img)

# Feed paper and cut (if supported)
p.ln(2)
p.cut()