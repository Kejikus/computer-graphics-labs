
if __name__ == "__main__":
    import base64
    import cv2
    from algorithms.task_03 import task_3, CropRect

    step_value = 100

    imagefile = "images\\test.jpg"

    image_file = open(imagefile, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_3(encoded_string, 200, CropRect(**{'x': 550, 'y': 15, 'w': 150, 'h': 100}))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
