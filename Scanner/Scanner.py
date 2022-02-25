from pyzbar import pyzbar
import cv2


def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        if obj.type == "CODE128":
            cleartype = str(obj.data).find('\'')
            data = str(obj.data)[(cleartype + 1):-1]
            print(data)
            raise SystemExit
        else:
            cv2.putText(image, 'Wrong type',
                        (445, 470), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 0, 0), 2)
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
