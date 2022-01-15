import cv2
class mobileCamera :
    def getVideo(self,camera):
        self.camera=camera
        cap=cv2.VideoCapture(self.camera)
        while True:
            ret,frame=cap.read()
            cv2.imshow("mobile cam",frame)
            if cv2.waitKey ==ord('q'):
                break
        cap.release()
        cap.destroyAllWindows()
cam = mobileCamera()
cam.getVideo("http://25.5.51.30:8080/Video")


