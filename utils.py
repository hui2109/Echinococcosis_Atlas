import pickle

import pandas as pd
import os
import imghdr


def get_data():
    if os.path.exists('./asset/atlas.pkl'):
        with open('./asset/atlas.pkl', 'rb') as f:
            atlas_data = pickle.loads(f.read())
        return atlas_data
    df = pd.read_excel('./asset/data.xlsx', sheet_name='sheet1', parse_dates=[5], dtype={
        'ID': str,
        'exam_ID': str,
        'age': str,
        'images_Link': str
    })
    atlas_data = []
    for i, exam_ID in enumerate(df['exam_ID']):
        patient_info = {
            exam_ID: {
                'ID': df.iloc[i, 0],
                'name': df.iloc[i, 2],
                'sex': df.iloc[i, 3],
                'age': df.iloc[i, 4],
                'exam_Datetime': df.iloc[i, 5].strftime('%Y-%m-%d'),
                'exam_See': df.iloc[i, 6],
                'exam_Diag': df.iloc[i, 7],
                'pathology_See': df.iloc[i, 8],
                'pathology_Diag': df.iloc[i, 9],
                'images_Path': _get_image_path(df.iloc[i, 10])
            }
        }
        atlas_data.append(patient_info)

    with open('./asset/atlas.pkl', 'wb') as f:
        pickle.dump(atlas_data, f)

    return atlas_data


def _get_image_path(image_dir_path):
    image_class = ''
    image_path_list = []

    if not os.path.exists(image_dir_path):
        print('找不到该文件')
        return []
    for image in sorted(os.listdir(image_dir_path)):
        image_path = os.path.join(image_dir_path, image)
        if imghdr.what(image_path):
            image_path_list.append([image_path, image_class])
    return image_path_list


if __name__ == '__main__':
    d = get_data()[0]['228551']['exam_Datetime']
    print(d, type(d))
    # print(len(get_data()))
