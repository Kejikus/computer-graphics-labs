
if __name__ == '__main__':
    import base64
    import cv2
    from ..task_01 import task_1

    threshold = 100

    imagefile = "images\\test.jpg"

    image_file = open(imagefile, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_1(encoded_string, threshold, debug=True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
