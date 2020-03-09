import base64
from datetime import datetime

from flask import Flask, render_template, request

import algorithms
import settings

app = Flask(__name__,
            static_folder='static')


@app.context_processor
def custom_context():
    return dict(
        dt_now=datetime.now,
        author=settings.AUTHOR,
        primary_color=settings.PRIMARY_COLOR,
        secondary_color=settings.SECONDARY_COLOR,
        accent_color=settings.ACCENT_COLOR,
        accent_text_color=settings.ACCENT_TEXT_COLOR,
        btn_color=settings.BTN_COLOR,
        author_color=settings.AUTHOR_COLOR,
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lab-1', methods=['GET', 'POST'])
def lab_1():
    if request.method == 'POST'\
            and 'image' in request.files\
            and 'threshold' in request.form:
        threshold = request.form.get('threshold', None, type=int)
        image = request.files['image']
        if image.filename != '' and threshold is not None:
            image_string = base64.b64encode(image.read())
            image_string = image_string.decode('utf-8')

            result_img, result_param = algorithms.task_1(image_string, threshold)

            context = {
                'input_image': image_string,
                'output_image': result_img[0].decode('utf-8'),
                'input_threshold': threshold,
                'output_width': result_param.width,
                'output_height': result_param.height,
                'output_channels': result_param.channels
            }

            return render_template('labs/lab_1.html', **context)

    return render_template('labs/lab_1.html')


@app.route('/lab-2', methods=['GET', 'POST'])
def lab_2():
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image_string = base64.b64encode(image.read())
            image_string = image_string.decode('utf-8')

            _, result_param = algorithms.task_2(image_string)

            context = {
                'input_image': image_string,
                'first_diff_min': result_param.first_diff_min,
                'first_diff_max': result_param.first_diff_max,
                'second_diff_min': result_param.second_diff_min,
                'second_diff_max': result_param.second_diff_max,
            }

            return render_template('labs/lab_2.html', **context)

    return render_template('labs/lab_2.html')


if __name__ == '__main__':
    app.run()
