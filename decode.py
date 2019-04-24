import shutil
import numpy
import cv2

class Symbols:
    A = '▀▄'
    B = '██'
    C = '▄▀'
    S0000 = '  '
    S0001 = ' ▄'
    S0010 = '▄ '
    S0011 = ' ▀'
    S000 = ' ▀'
    G = '  '
    D = '▀ '
    E = ' '
    F = '▄ '
    G = ' ▄ '

def get_window_size():
    return shutil.get_terminal_size()

def decode(image, width = None, threshold_gray = 3, height_width_rate = 2.2):
    if width is None:
        width, _ = get_window_size()
    pixels_in_char = image.shape[1] / width

    chars = numpy.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    size = width, round(image.shape[0] / height_width_rate / pixels_in_char)
    image = numpy.sum(cv2.resize(image, size), axis = 2)
    image -= image.min()
    image = (1.0 - image / image.max())**threshold_gray * (chars.size - 1)
    return '\n'.join((''.join(r) for r in chars[image.astype(int)])), image.shape[0]

def testcases():
    image = cv2.imread('./videos/JZM1947.jpg')
    print(image_to_ascii(image))

if __name__ == '__main__':
    testcases()
