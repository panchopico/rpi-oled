import time
import subprocess
from board import SCL, SDA
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
disp.fill(0)
disp.show()
w, h = disp.width, disp.height
image = Image.new('1', (w, h))
draw = ImageDraw.Draw(image)
cmd = "hostname -I | cut -d\' \' -f1 | tr -d \'\\n\'"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
cmd = "hostname | tr -d \'\\n\'"
HOST = subprocess.check_output(cmd, shell=True).decode("utf-8")
cmd = "top -bn1 | grep load | awk " \
          "'{printf \"CPU Load: %.2f\", $(NF-2)}'"
CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
cmd = "free -m | awk 'NR==2{printf " \
          "\"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
cmd = "df -h | awk '$NF==\"/\"{printf " \
          "\"Disk: %d/%dGB %s\", $3,$2,$5}'"
Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
x = 0
draw.text((x, -2), "IP: " + str(IP) + "( " + HOST + ")", fill=255)
disp.image(image)
disp.show()

def clrdisp():
       disp.fill(0)
       disp.show()

	
clrdisp()
disp.show()
disp.image(image)
disp.show()
# clrdisp()
