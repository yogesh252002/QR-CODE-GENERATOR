import cv2
from pyzbar.pyzbar import decode
img=cv2.imread('Std_yogesh.png')
print(decode(img))
# from PIL import Image 
# d=decode(Image.open("Std_yogesh.png"))
# print(d[0].data.decode())


# import cv2
# d = cv2.QRCodeDetector()
# val,points,straight_qrcode=d.detectAndDecode(cv2.imread("Std_yogesh.png"))
# print(val)
# print(straight_qrcode)
#from qrtools.qrtools import QR 

# from qrtools import qrtools
# qr = qrtools.QR()
# #import qrtools
# qr = qrtools.QR()
# qr.decode("Std_yogesh.png")
# print(qr.data) 

# import qrtools
# qr = qrtools.QR()
# qr.decode("Std_yogesh.png")
# #True
# print(qr.data)
