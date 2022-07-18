import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create('https://www.linkedin.com/in/diceasa/')
url.svg('MiQR.svg', scale=8)
print(url)