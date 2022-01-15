import cv2
# import numpy as np
# from pyzbar.pyzbar import decode # helps to detect and localise the the QR code
# img = cv2.imread('F:\DESKTOP BACKUP\QR code generator\Student_QR\Std_yogesh.png')
# code=decode(img)
# print(code)
d = cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread("Std_yogesh.png"))
print(val)
print(straight_qrcode)