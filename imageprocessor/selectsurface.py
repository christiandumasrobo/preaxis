import cv2
import numpy as np

def doCanny(l, u, t1xy, t2xy):
    img = cv2.imread('images/0_color.png')
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    threshold1 = np.mean(img[t1xy[1], t1xy[0]])
    threshold2 = np.mean(img[t2xy[1], t2xy[0]])
    print(threshold1, threshold2)
    edges = cv2.Canny(image=blurred, threshold1=l, threshold2=u)

    final_image = np.zeros(edges.shape, dtype=np.uint8)

    for idx in range(24):
        img = cv2.imread(f'images/{idx}_color.png')
        blurred = cv2.GaussianBlur(img, (3, 3), 0)

        threshold1 = np.mean(img[t1xy[1], t1xy[0]])
        threshold2 = np.mean(img[t2xy[1], t2xy[0]])
        edges = cv2.Canny(image=blurred, threshold1=l, threshold2=u)

        final_image = cv2.bitwise_or(cv2.bitwise_xor(final_image, edges), final_image)
    return final_image

class SurfaceSelector:
    def __init__(self):
        self._img = cv2.imread('images/0_color.png', 0) #read image as grayscale
        self._canny = cv2.Canny(self._img, 85, 255) 
        self._window = cv2.namedWindow('image') # make a window with name 'image'
        self._trackbar1 = cv2.createTrackbar('L', 'image', 0, 255, self.callback) #lower threshold trackbar for window 'image
        self._trackbar1 = cv2.createTrackbar('U', 'image', 0, 255, self.callback) #upper threshold trackbar for window 'image
        self._click_pos = [1, 1]
        self._state = 'Init'
        self._thresholds = [1, 1]
        self._thresh1xy = [1, 1]
        self._thresh2xy = [1, 1]
        cv2.setMouseCallback('image', self.click_event)

    def callback(self, x):
        print(x)

    def click_event(self, event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
    
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)
            if self._state == 'Init' or self._state == 'Second':
                self._click_pos[0] = x
                self._click_pos[1] = y
                self._state = 'First'
            elif self._state == 'First':
                self._click_pos[0] = x
                self._click_pos[1] = y
                self._state = 'Second'

    
    def SpinOnce(self):
        canny = doCanny(self._thresholds[0], self._thresholds[1], self._thresh1xy, self._thresh2xy)

        numpy_horizontal_concat = np.concatenate((self._img, canny), axis=1) # to display image side by side
        cv2.imshow('image', numpy_horizontal_concat)
        k = cv2.waitKey(1) & 0xFF
        if k == 27: #escape key
            return True
        self._thresholds[0] = cv2.getTrackbarPos('L', 'image')
        self._thresholds[1] = cv2.getTrackbarPos('U', 'image')
        if self._state == 'First':
            #self._thresholds[0] = self._img[self._click_pos[1], self._click_pos[0]]
            self._thresh1xy = self._click_pos
            #print(self._thresholds[0])

        if self._state == 'Second':
            #self._thresholds[1] = self._img[self._click_pos[1], self._click_pos[0]]
            self._thresh2xy = self._click_pos
            #print(self._thresholds[1])
        print(self._state)



ss = SurfaceSelector()
while(1):
    breakVal = ss.SpinOnce()
    if breakVal:
        break
cv2.destroyAllWindows()
