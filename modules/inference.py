import os
from ludwig.api import LudwigModel
import pandas as pd
from modules.database import CreateConnection
from datetime import datetime

cursor = CreateConnection()
category = {
    '0': 'letter',
    '1': 'form',
    '2': 'email',
    '3': 'handwritten',
    '4': 'advertisement'
}



def get_prediction(file_path,original_file):

    model_path = './model'

    if not os.path.isfile(file_path):
        pass

    original_filename = file_path.split(r"uploads")[1]
    file = original_filename.split(".")[0]
    print(file)

    data = pd.DataFrame.from_dict({'image_path':[file_path]})
    model = LudwigModel.load(model_path)
    predictions = model.predict(data_df=data, skip_save_unprocessed_output=True)
    model.close()

    label = category[predictions['label_predictions'].loc[0]]
    score = predictions['label_probability'].loc[0]

    cursor.insert(file,original_file, label, score,datetime.now())








