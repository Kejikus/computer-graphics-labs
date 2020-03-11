if __name__ == "__main__":
    import base64
    import cv2
    from algorithms.task_04 import task_4

    step_value = 100

    imagefile = "images\\test.jpg"

    image_file = open(imagefile, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_4(encoded_string, 127, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
