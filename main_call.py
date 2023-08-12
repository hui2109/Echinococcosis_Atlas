import os.path
import pickle
import time

from utils import get_data

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import pandas as pd


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('包虫图谱图片筛选')
        self.initWidgets()
        self.showMaximized()
        self.initData()

    def initWidgets(self):
        self.ce1_btn = QCheckBox('CE1')
        self.ce1_btn.toggled.connect(self.on_ce1_btn_toggled)
        self.ce1_btn.setProperty('666', 'CE1')
        self.ce1_btn.setShortcut(Qt.Key.Key_1)

        self.ce2_btn = QCheckBox('CE2')
        self.ce2_btn.toggled.connect(self.on_ce2_btn_toggled)
        self.ce2_btn.setProperty('666', 'CE2')
        self.ce2_btn.setShortcut(Qt.Key.Key_2)

        self.ce3_btn = QCheckBox('CE3')
        self.ce3_btn.toggled.connect(self.on_ce3_btn_toggled)
        self.ce3_btn.setProperty('666', 'CE3')
        self.ce3_btn.setShortcut(Qt.Key.Key_3)

        self.ce4_btn = QCheckBox('CE4')
        self.ce4_btn.toggled.connect(self.on_ce4_btn_toggled)
        self.ce4_btn.setProperty('666', 'CE4')
        self.ce4_btn.setShortcut(Qt.Key.Key_4)

        self.ce5_btn = QCheckBox('CE5')
        self.ce5_btn.toggled.connect(self.on_ce5_btn_toggled)
        self.ce5_btn.setProperty('666', 'CE5')
        self.ce5_btn.setShortcut(Qt.Key.Key_5)

        self.ae_hailstorm_btn = QCheckBox('AE Hailstorm')
        self.ae_hailstorm_btn.toggled.connect(self.on_ae1_btn_toggled)
        self.ae_hailstorm_btn.setProperty('666', 'AE Hailstorm')
        self.ae_hailstorm_btn.setShortcut(Qt.Key.Key_Q)

        self.ae_pseudocystic_btn = QCheckBox('AE Pseudocystic')
        self.ae_pseudocystic_btn.toggled.connect(self.on_ae2_btn_toggled)
        self.ae_pseudocystic_btn.setProperty('666', 'AE Pseudocystic')
        self.ae_pseudocystic_btn.setShortcut(Qt.Key.Key_W)

        self.ae_hemangioma_like_btn = QCheckBox('AE Hemangioma-like')
        self.ae_hemangioma_like_btn.toggled.connect(self.on_ae3_btn_toggled)
        self.ae_hemangioma_like_btn.setProperty('666', 'AE Hemangioma-like')
        self.ae_hemangioma_like_btn.setShortcut(Qt.Key.Key_E)

        self.ae_ossification_btn = QCheckBox('AE Ossification')
        self.ae_ossification_btn.toggled.connect(self.on_ae4_btn_toggled)
        self.ae_ossification_btn.setProperty('666', 'AE Ossification')
        self.ae_ossification_btn.setShortcut(Qt.Key.Key_R)

        self.ae_metastasis_like_btn = QCheckBox('AE Metastasis-like')
        self.ae_metastasis_like_btn.toggled.connect(self.on_ae5_btn_toggled)
        self.ae_metastasis_like_btn.setProperty('666', 'AE Metastasis-like')
        self.ae_metastasis_like_btn.setShortcut(Qt.Key.Key_T)

        self.ID_label = QLabel('住院号')
        self.ID_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_ID_label = QLabel('946628')
        self.true_ID_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.exam_ID_label = QLabel('检查号')
        self.exam_ID_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_exam_ID_label = QLabel('228551')
        self.true_exam_ID_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.name_label = QLabel('姓名')
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_name_label = QLabel('张三')
        self.true_name_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.sex_label = QLabel('性别')
        self.sex_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_sex_label = QLabel('男')
        self.true_sex_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.age_label = QLabel('年龄')
        self.age_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_age_label = QLabel('45')
        self.true_age_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.exam_Datetime_label = QLabel('检查日期')
        self.exam_Datetime_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_exam_Datetime_label = QLabel('2021-08-01')
        self.true_exam_Datetime_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.pathology_Diag_label = QLabel('病理结论')
        self.pathology_Diag_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.true_pathology_Diag_label = QLabel('CE1')
        self.true_pathology_Diag_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.exam_See_label = QLabel('检查所见')
        self.exam_See_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.exam_Diag_label = QLabel('检查结论')
        self.exam_Diag_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.pathology_See_label = QLabel('病\n理\n所\n见')

        font = QFont('Times New Roman', 17)
        self.exam_See_text = QTextEdit()
        self.exam_See_text.setReadOnly(True)
        self.exam_See_text.setFont(font)
        self.exam_Diag_text = QTextEdit()
        self.exam_Diag_text.setReadOnly(True)
        self.exam_Diag_text.setFont(font)
        self.pathology_See_text = QTextEdit()
        self.pathology_See_text.setReadOnly(True)
        self.pathology_See_text.setFont(QFont('Times New Roman', 15))

        self.patient_list_label = QLabel('患者列表')
        self.patient_list_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.patient_list = QListWidget()
        self.patient_list.currentItemChanged.connect(self.patient_list_currentItemChanged)

        self.images_list_label = QLabel('图像列表')
        self.images_list_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.images_list = QListWidget()
        self.images_list.currentItemChanged.connect(self.images_list_currentItemChanged)

        self.image_text = QTextEdit()
        self.image_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.save_btn = QPushButton('保存')
        self.save_btn.clicked.connect(self.save_btn_clicked)
        self.save_btn.setShortcut(Qt.Key.Key_S)

        self.export_btn = QPushButton('导出')
        self.export_btn.clicked.connect(self.export_btn_clicked)

        self.status_bar = QStatusBar()

        button_ce_layout = QHBoxLayout()
        button_ce_layout.addWidget(self.ce1_btn)
        button_ce_layout.addWidget(self.ce2_btn)
        button_ce_layout.addWidget(self.ce3_btn)
        button_ce_layout.addWidget(self.ce4_btn)
        button_ce_layout.addWidget(self.ce5_btn)

        button_ae_layout = QHBoxLayout()
        button_ae_layout.addWidget(self.ae_hailstorm_btn)
        button_ae_layout.addWidget(self.ae_pseudocystic_btn)
        button_ae_layout.addWidget(self.ae_hemangioma_like_btn)
        button_ae_layout.addWidget(self.ae_ossification_btn)
        button_ae_layout.addWidget(self.ae_metastasis_like_btn)

        button_layout = QVBoxLayout()
        button_layout.addLayout(button_ce_layout)
        button_layout.addLayout(button_ae_layout)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        image_btn_layout = QVBoxLayout()
        image_btn_layout.addWidget(self.image_text, 10)
        image_btn_layout.addLayout(button_layout)

        exam_See_Diag_layout = QVBoxLayout()
        exam_See_Diag_layout.addWidget(self.exam_See_label)
        exam_See_Diag_layout.addWidget(self.exam_See_text, 10)
        exam_See_Diag_layout.addWidget(self.exam_Diag_label)
        exam_See_Diag_layout.addWidget(self.exam_Diag_text, 2)

        patient_info_layout = QVBoxLayout()
        patient_info_layout.addWidget(self.name_label)
        patient_info_layout.addWidget(self.true_name_label)
        patient_info_layout.addWidget(self.exam_ID_label)
        patient_info_layout.addWidget(self.true_exam_ID_label)
        patient_info_layout.addWidget(self.ID_label)
        patient_info_layout.addWidget(self.true_ID_label)
        patient_info_layout.addWidget(self.sex_label)
        patient_info_layout.addWidget(self.true_sex_label)
        patient_info_layout.addWidget(self.age_label)
        patient_info_layout.addWidget(self.true_age_label)
        patient_info_layout.addWidget(self.exam_Datetime_label)
        patient_info_layout.addWidget(self.true_exam_Datetime_label)
        patient_info_layout.addWidget(self.pathology_Diag_label)
        patient_info_layout.addWidget(self.true_pathology_Diag_label)
        patient_info_layout.addWidget(self.save_btn)

        patient_list_layout = QVBoxLayout()
        patient_list_layout.addWidget(self.patient_list_label)
        patient_list_layout.addWidget(self.patient_list)
        patient_list_layout.addWidget(self.export_btn)

        other_layout = QHBoxLayout()
        other_layout.addWidget(self.status_bar, 1)
        other_layout.addWidget(self.pathology_See_label)
        other_layout.addWidget(self.pathology_See_text, 9)

        images_list_layout = QVBoxLayout()
        images_list_layout.addWidget(self.images_list_label)
        images_list_layout.addWidget(self.images_list)

        up_layout = QHBoxLayout()
        up_layout.addLayout(image_btn_layout, 10)
        up_layout.addLayout(images_list_layout, 1)
        up_layout.addLayout(exam_See_Diag_layout, 3)

        right_layout = QHBoxLayout()
        right_layout.addLayout(patient_info_layout)
        right_layout.addLayout(patient_list_layout)

        left_layout = QVBoxLayout()
        left_layout.addLayout(up_layout, 10)
        left_layout.addLayout(other_layout, 1)

        final_layout = QHBoxLayout()
        final_layout.addLayout(left_layout, 8)
        final_layout.addLayout(right_layout, 2)

        self.setLayout(final_layout)

    def patient_list_currentItemChanged(self, current_item, _):
        self.patient_index = current_item.data(666)
        self.setting_some_data()

    def images_list_currentItemChanged(self, current_image_item, _):
        self.image_index = current_image_item.data(666)
        # 设置图像
        self.setting_image()
        # 获取复选框状态
        self.load_all_check_box()

    def initData(self):
        # 获取数据
        self.atlas_data = get_data()
        self.max_num = len(self.atlas_data)

        # 定义初始值
        if not os.path.exists('./asset/indexes.pkl'):
            self.indexes = (0, 0)
            self.patient_index = self.indexes[0]
            self.image_index = self.indexes[1]
            self.flag = True
        else:
            with open('./asset/indexes.pkl', 'rb') as f:
                self.indexes = pickle.loads(f.read())
                self.patient_index = self.indexes[0]
                self.image_index = self.indexes[1]
                self.flag = True

        if not os.path.exists('./asset/selected_patient_list.pkl'):
            self.selected_patient_list = set()
        else:
            with open('./asset/selected_patient_list.pkl', 'rb') as f:
                self.selected_patient_list = pickle.loads(f.read())

        font = QFont('Times New Roman', 16)

        # 获取患者列表
        self.patient_item_list = []
        for i in range(self.max_num):
            exam_ID = list(self.atlas_data[i].keys())[0]
            list_item = QListWidgetItem(str(i + 1) + '. ' + self.atlas_data[i][exam_ID]['name'], self.patient_list)
            list_item.setData(666, i)
            list_item.setFont(font)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.patient_item_list.append(list_item)

        # 设置列表项颜色
        for i in range(self.max_num):
            if i in self.selected_patient_list:
                self.setting_color(None, i)

        self.patient_list.setCurrentItem(self.patient_item_list[self.patient_index])

        # 设置快捷键
        shortcut_up = QShortcut(QKeySequence(Qt.Key.Key_Up), self)
        shortcut_up.activated.connect(self.pre_patient)

        shortcut_down = QShortcut(QKeySequence(Qt.Key.Key_Down), self)
        shortcut_down.activated.connect(self.next_patient)

        shortcut_left = QShortcut(QKeySequence(Qt.Key.Key_Left), self)
        shortcut_left.activated.connect(self.pre_image)

        shortcut_right = QShortcut(QKeySequence(Qt.Key.Key_Right), self)
        shortcut_right.activated.connect(self.next_image)

        self.status_bar.showMessage('Ready!')

    def setting_some_data(self):
        # 获取图像列表
        self.setting_image_list()

        # 设置患者数据
        self.setting_data()

        # 设置列表项颜色
        index = list(range(self.image_max_num))
        index.reverse()
        if self.flag:
            index.pop(self.indexes[1])
            index.append(self.indexes[1])
        for i in index:
            self.image_index = i
            # 获取复选框状态
            self.load_all_check_box()

        self.flag = False

    def setting_image(self):
        curr_image_path = self.images_Path[self.image_index][0]
        self.image_text.clear()

        tc = self.image_text.textCursor()
        tif = QTextImageFormat()
        tif.setName(curr_image_path)
        tif.setWidth(self.image_text.size().width())
        tc.insertImage(tif, QTextFrameFormat.Position.InFlow)
        self.image_text.setReadOnly(True)
        self.image_text.setAttribute(Qt.WidgetAttribute.WA_Disabled, True)

    def setting_image_list(self):
        if not self.flag:
            self.image_index = 0

        self.exam_ID = list(self.atlas_data[self.patient_index].keys())[0]
        self.images_Path = self.atlas_data[self.patient_index][self.exam_ID]['images_Path']
        font = QFont('Times New Roman', 16)

        # 断开信号
        self.images_list.currentItemChanged.disconnect(self.images_list_currentItemChanged)
        self.images_list.clear()
        # 恢复信号
        self.images_list.currentItemChanged.connect(self.images_list_currentItemChanged)

        self.image_item_list = []
        self.image_max_num = len(self.images_Path)
        for i in range(self.image_max_num):
            list_item = QListWidgetItem(self.images_Path[i][0].split('/')[-1][:-4], self.images_list)
            list_item.setData(666, i)
            list_item.setFont(font)
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.image_item_list.append(list_item)

        self.images_list.setCurrentItem(self.image_item_list[self.image_index])

    def setting_data(self):
        patient_basic_info = self.atlas_data[self.patient_index][self.exam_ID]

        self.true_ID_label.setText(patient_basic_info['ID'])
        self.true_exam_ID_label.setText(self.exam_ID)
        self.true_name_label.setText(patient_basic_info['name'])
        self.true_sex_label.setText(patient_basic_info['sex'])
        self.true_age_label.setText(patient_basic_info['age'])
        self.true_exam_Datetime_label.setText(patient_basic_info['exam_Datetime'])
        self.true_pathology_Diag_label.setText(patient_basic_info['pathology_Diag'])

        self.exam_See_text.setText(patient_basic_info['exam_See'])
        self.exam_Diag_text.setText(patient_basic_info['exam_Diag'])
        self.pathology_See_text.setText(patient_basic_info['pathology_See'])

    def load_all_check_box(self):
        _type = self.atlas_data[self.patient_index][self.exam_ID]['images_Path'][self.image_index][1]
        if _type == 'CE1':
            self.changeStatus(self.ce1_btn, False)
        elif _type == 'CE2':
            self.changeStatus(self.ce2_btn, False)
        elif _type == 'CE3':
            self.changeStatus(self.ce3_btn, False)
        elif _type == 'CE4':
            self.changeStatus(self.ce4_btn, False)
        elif _type == 'CE5':
            self.changeStatus(self.ce5_btn, False)
        elif _type == 'AE Hailstorm':
            self.changeStatus(self.ae_hailstorm_btn, False)
        elif _type == 'AE Pseudocystic':
            self.changeStatus(self.ae_pseudocystic_btn, False)
        elif _type == 'AE Hemangioma-like':
            self.changeStatus(self.ae_hemangioma_like_btn, False)
        elif _type == 'AE Ossification':
            self.changeStatus(self.ae_ossification_btn, False)
        elif _type == 'AE Metastasis-like':
            self.changeStatus(self.ae_metastasis_like_btn, False)
        elif _type == '':
            self.changeStatus(None, False)

    def save_btn_clicked(self):
        with open('./asset/atlas.pkl', 'wb') as f:
            pickle.dump(self.atlas_data, f)

        with open('./asset/indexes.pkl', 'wb') as f:
            indexes = (self.patient_index, self.image_index)
            pickle.dump(indexes, f)

        with open('./asset/selected_patient_list.pkl', 'wb') as f:
            pickle.dump(self.selected_patient_list, f)

        self.status_bar.showMessage('已保存！', 5000)

    def export_btn_clicked(self):
        self.export_df = pd.DataFrame(
            columns=['Image Path', 'Image Type', 'exam ID', 'exam Datetime', 'pathology See', 'pathology Diag'])
        for patient in self.atlas_data:
            exam_ID = list(patient.keys())[0]
            patient_info = patient[exam_ID]
            pathology_Diag = patient_info['pathology_Diag']
            pathology_See = patient_info['pathology_See']
            exam_Datetime = patient_info['exam_Datetime']
            for ip, _type in patient_info['images_Path']:
                if _type != '':
                    image_path = ip
                    image_type = _type
                    self.export_data_list = [
                        image_path,
                        image_type,
                        exam_ID,
                        exam_Datetime.replace('-', '/'),
                        pathology_See,
                        pathology_Diag
                    ]
                    self._export_data()

        if not os.path.exists('./asset/exported'):
            os.makedirs('./asset/exported')

        if len(self.export_df) > 0:
            file_name = os.path.join('./asset/exported', 'exported' + '_' + str(int(time.time())) + '.xlsx')
            with pd.ExcelWriter(file_name) as writer:
                self.export_df.to_excel(writer, index=False)
            self.status_bar.showMessage('已成功导出！', 5000)

    def _export_data(self):
        self.export_df.loc[len(self.export_df)] = self.export_data_list

    def next_image(self):
        if self.image_index < self.image_max_num - 1:
            self.image_index += 1
            self.images_list.setCurrentItem(self.image_item_list[self.image_index])

    def pre_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.images_list.setCurrentItem(self.image_item_list[self.image_index])

    def next_patient(self):
        if self.patient_index < self.max_num - 1:
            self.patient_index += 1
            self.patient_list.setCurrentItem(self.patient_item_list[self.patient_index])

    def pre_patient(self):
        if self.patient_index > 0:
            self.patient_index -= 1
            self.patient_list.setCurrentItem(self.patient_item_list[self.patient_index])

    def on_ce1_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ce1_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ce2_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ce2_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ce3_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ce3_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ce4_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ce4_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ce5_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ce5_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ae1_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ae_hailstorm_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ae2_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ae_pseudocystic_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ae3_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ae_hemangioma_like_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ae4_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ae_ossification_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def on_ae5_btn_toggled(self, checked):
        if checked:
            self.changeStatus(self.ae_metastasis_like_btn, True)
        else:
            self.unchecked()
            self.erase_color()

    def erase_color(self):
        self.image_item_list[self.image_index].setBackground(QColor(255, 255, 255))
        self.patient_item_list[self.patient_index].setBackground(QColor(255, 255, 255))

    def setting_color(self, image_index, patient_index):
        if image_index is not None:
            self.image_item_list[image_index].setBackground(QColor(156, 252, 229))
        if patient_index is not None:
            self.patient_item_list[patient_index].setBackground(QColor(156, 252, 229))
            self.selected_patient_list.add(patient_index)

    def changeStatus(self, btn, setting_status):
        # 禁用信号与槽
        self.ce1_btn.toggled.disconnect(self.on_ce1_btn_toggled)
        self.ce2_btn.toggled.disconnect(self.on_ce2_btn_toggled)
        self.ce3_btn.toggled.disconnect(self.on_ce3_btn_toggled)
        self.ce4_btn.toggled.disconnect(self.on_ce4_btn_toggled)
        self.ce5_btn.toggled.disconnect(self.on_ce5_btn_toggled)
        self.ae_hailstorm_btn.toggled.disconnect(self.on_ae1_btn_toggled)
        self.ae_pseudocystic_btn.toggled.disconnect(self.on_ae2_btn_toggled)
        self.ae_hemangioma_like_btn.toggled.disconnect(self.on_ae3_btn_toggled)
        self.ae_ossification_btn.toggled.disconnect(self.on_ae4_btn_toggled)
        self.ae_metastasis_like_btn.toggled.disconnect(self.on_ae5_btn_toggled)

        self.ce1_btn.setChecked(False)
        self.ce2_btn.setChecked(False)
        self.ce3_btn.setChecked(False)
        self.ce4_btn.setChecked(False)
        self.ce5_btn.setChecked(False)
        self.ae_hailstorm_btn.setChecked(False)
        self.ae_pseudocystic_btn.setChecked(False)
        self.ae_hemangioma_like_btn.setChecked(False)
        self.ae_ossification_btn.setChecked(False)
        self.ae_metastasis_like_btn.setChecked(False)

        if setting_status:
            self.atlas_data[self.patient_index][self.exam_ID]['images_Path'][self.image_index][1] = btn.property('666')

        if btn:
            btn.setChecked(True)
            self.setting_color(self.image_index, self.patient_index)

        # 恢复信号与槽
        self.ce1_btn.toggled.connect(self.on_ce1_btn_toggled)
        self.ce2_btn.toggled.connect(self.on_ce2_btn_toggled)
        self.ce3_btn.toggled.connect(self.on_ce3_btn_toggled)
        self.ce4_btn.toggled.connect(self.on_ce4_btn_toggled)
        self.ce5_btn.toggled.connect(self.on_ce5_btn_toggled)
        self.ae_hailstorm_btn.toggled.connect(self.on_ae1_btn_toggled)
        self.ae_pseudocystic_btn.toggled.connect(self.on_ae2_btn_toggled)
        self.ae_hemangioma_like_btn.toggled.connect(self.on_ae3_btn_toggled)
        self.ae_ossification_btn.toggled.connect(self.on_ae4_btn_toggled)
        self.ae_metastasis_like_btn.toggled.connect(self.on_ae5_btn_toggled)

    def unchecked(self):
        self.atlas_data[self.patient_index][self.exam_ID]['images_Path'][self.image_index][1] = ''


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    # 设置样式
    with open('./asset/stylesheet.qss', 'r', 1, 'utf-8') as f:
        app.setStyleSheet(f.read())

    # 设置窗口图标
    app_icon = QIcon('./asset/disease.png')
    app.setWindowIcon(app_icon)

    window = MyWindow()
    window.show()
    sys.exit(app.exec())
