import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create('https://www.tuweb.cl/')
url.svg('MiQR.svg', scale=8)
print(url)
