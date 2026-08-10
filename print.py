from escpos.printer import Serial 

p = Serial(devfile="/dev/serial0", baudrate=9600)

p.image("/home/gmbmonkeyvp/Pictures/image.jpg")

p.ln(5)