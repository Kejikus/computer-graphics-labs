if __name__ == "__main__":
    import base64
    import cv2
    from algorithms.task_05 import task_5

    image_file_name = "algorithms\\images\\test2.jpg"

    image_file = open(image_file_name, "rb")
    encoded_string = base64.b64encode(image_file.read())

    task_5(encoded_string, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()