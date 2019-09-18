# Import Python System Libraries
import subprocess
import time

# Import Blinka
from board import SCL, SDA
import busio
import adafruit_ssd1306

# Import Python Imaging Library
from PIL import Image, ImageDraw, ImageFont

start_time = time.time()

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position
# for drawing shapes.
xl1 = 0
xl2 = 10

# Load nice silkscreen font
font = ImageFont.truetype('/home/pi/fonts/slkscr.ttf', 16)

def clrdisp():
       disp.fill(0)
       disp.show()

while (time.time() - start_time) <= 10:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    timestr = time.asctime().split(' ')
    line1 = f'{timestr[0]}, {timestr[1]} {timestr[2]}'
    line2 = f'{timestr[3]}'
    
    draw.text((xl1, top), line1, font=font, fill=255)
    draw.text((xl2, top+15), line2, font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    #xl1 += 1
    #xl2 += 2
    time.sleep(.1)

print("All done")
draw.rectangle((0, 0, width, height), outline=0, fill=0)
draw.text((0,0), "ALL DONE!", font = font, fill=255)
disp.image(image)
disp.show()
time.sleep(3)
clrdisp()
