from PIL import Image
import cv2
import ascii_magic

vidcap = cv2.VideoCapture('test-videos/1.mp4') # enter video path here
success, image = vidcap.read()
filename = 'test-animations/1.txt' # enter output txt filename here

with open(filename, 'a') as f:
    while success:
        frame = Image.fromarray(image)
        ascii_ = ascii_magic.from_image(frame)
        f.write(ascii_)
        f.write('\n\x1b[H')
        success, image = vidcap.read()

print('done check it out')
