import shutil
import numpy
import cv2

class Symbols:

def get_window_size():
    return shutil.get_terminal_size()

class Decoder(object):
    gray_chars = numpy.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    block_char = '█'
    threshold_gray = 3
    height_width_rate = 2.2

    def decode_with_chars(image, width = None):
        if width is None:
            width, _ = get_window_size()
        pixels_in_char = image.shape[1] / width

        chars =
        size = width, round(image.shape[0] / self.height_width_rate / pixels_in_char)
        image = numpy.sum(cv2.resize(image, size), axis = 2)
        image -= image.min()
        image = (1.0 - image / image.max())**self.threshold_gray * (chars.size - 1)
        return '\n'.join((''.join(r) for r in chars[image.astype(int)])), image.shape[0]

    def decode_with_blocks(image, width = None):
        pass

def testcases():
    image = cv2.imread('./videos/JZM1947.jpg')
    print(image_to_ascii(image))

if __name__ == '__main__':
    testcases()
