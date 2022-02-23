from pyzbar import pyzbar
import cv2


def draw_barcode(decoded, image):
    # n_points = len(decoded.polygon)
    # for i in range(n_points):
    #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                        (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                        color=(0, 255, 0),
                        thickness=5)
    return image

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()
        break
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
