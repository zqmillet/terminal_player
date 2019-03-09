import shutil
import numpy
import cv2

def get_window_size():
    return shutil.get_terminal_size()

def image_to_ascii(image, width, threshold_gray = 3, height_width_rate = 7/4):
    chars = numpy.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    size = (round(image.shape[0] * height_width_rate / pixels_in_char), round(image.shape[1] / pixels_in_char) )
    image = numpy.sum(cv2.resize(image, size), axis = 2)
    image -= image.min()
    image = (1.0 - image / image.max())**threshold_gray * (chars.size - 1)
    return '\n'.join( (''.join(r) for r in chars[image.astype(int)]))

def testcases():
    image = cv2.imread('./videos/JZM1947.jpg')
    print(image_to_ascii(image))

if __name__ == '__main__':
    testcases()
