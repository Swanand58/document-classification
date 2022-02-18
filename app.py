from flask import Flask, request, render_template, flash, redirect, url_for
from modules.validation import check_file_ext, generate_thumbnail
from modules.inference import get_prediction
from modules.database import CreateConnection

import os
import uuid


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'



@app.route('/', methods=['GET', 'POST'])
def prediction():

    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file found.')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:

            if check_file_ext(file.filename):
                filename = str(uuid.uuid4()) + '.tif'
                print(file.filename)
                file.save(os.path.join('./uploads', filename))
                generate_thumbnail('./uploads/' + filename, size=(100, 100))
                get_prediction(os.path.abspath('./uploads/{}'.format(filename)),file.filename)

        return redirect('/results')

@app.route('/results', methods=['GET', 'POST'])
def results():
    results = CreateConnection().get_last_n_records(10)
    return render_template('results.html',results=results.iterrows())


if __name__ == "__main__":
    app.run( debug=True, threaded=True)