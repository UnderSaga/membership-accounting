from pyzbar import pyzbar
import cv2

def draw_barcode(decoded, image):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                        (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                        color=(0, 255, 0),
                        thickness=5)
    return image

def decode(image):
    code128 = "CODE128"
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        if obj.type == code128:
            cleartype = str(obj.data).find('\'')
            data = str(obj.data)[(cleartype + 1):-1]
            print(data)
            raise SystemExit
        else:
            print('Wrong type')
            raise SystemExit
    return image

def camera():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = decode(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break

if __name__ == '__main__':
    camera()
