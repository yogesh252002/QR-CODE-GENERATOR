from pyzbar.pyzbar import decode
from PIL import Image 
d=decode(Image.open('F:\DESKTOP BACKUP\QR code generator\Student_QR\Std_yogesh.png'))
print(d)