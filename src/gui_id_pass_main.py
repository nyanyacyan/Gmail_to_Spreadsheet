# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/LGRAM_auto_processer/installer/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import sys
from PySide6.QtWidgets import ( QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout )


# flow
from 01_src.method.image_meta_remove import ImageMetaRemove

# ----------------------------------------------------------------------------------
# **********************************************************************************
# Dirを取得するGUI

class GuiIdPassMain(QWidget):
    def __init__(self, window_title: str, size_x: int, size_y: int, explain: str, position_x: int=100, position_y: int=100):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(position_x, position_y, size_x, size_y)


        #? --- ディレクトリ選択 ---
        # 説明書き部分のラベル
        self.explain_label = QLabel(explain)


        # id入力欄
        self.id_label = QLabel("IDを入力して下さい。")
        self.id_input = QLineEdit()  # 入力するメソッド
        self.id_input.setFixedWidth(300)

        # pass入力欄
        self.pass_label = QLabel("パスワードを入力して下さい。")
        self.pass_input = QLineEdit()  # 入力するメソッド
        self.pass_input.setFixedWidth(300)

        # pathボタン
        self.dir_button = QPushButton("ファイル選択")  # ボタンを定義
        self.dir_button.clicked.connect(self.select_directory)

        # 実行ボタン
        self.submit_button = QPushButton("実行")
        self.submit_button.setFixedWidth(100)
        self.submit_button.clicked.connect(self.handle_submit)

        # キャンセルボタン
        self.cancel_button = QPushButton("閉じる")
        self.cancel_button.setFixedWidth(100)
        self.cancel_button.clicked.connect(self.handle_cancel)


        #? --- レイアウト設定 ---
        # 基礎になるレイアウト　→　ここに追加していく
        layout = QVBoxLayout()

        # ラベルをレイアウトに追加
        layout.addWidget(self.explain_label)

        # ID入力欄をレイアウトに追加
        id_layout = QHBoxLayout()  # 横並びにするレイアウト
        id_layout.addWidget(self.id_label)
        id_layout.addWidget(self.id_input)

        # pass入力欄をレイアウトに追加
        pass_layout = QHBoxLayout()  # 横並びにするレイアウト
        pass_layout.addWidget(self.pass_label)
        pass_layout.addWidget(self.pass_input)

        # ボタンレイアウトを基礎レイアウトに追加
        layout.addLayout(id_layout)
        layout.addLayout(pass_layout)

        # ボタンの行のレイアウト
        button_layout = QHBoxLayout()  # 横並びにするレイアウト
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.cancel_button)

        # ボタンレイアウトを基礎レイアウトに追加
        layout.addLayout(button_layout)


        #? --- 実際に表示させる ---
        self.setLayout(layout)


# **********************************************************************************


    #!##############################################################################
    #? 実行処理

    def handle_submit(self):
        pass

    #!##############################################################################


    def handle_cancel(self):
        QApplication.quit()

    #!##############################################################################
    # ------------------------------------------------------------------------------


    def select_directory(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "指定のファイルを選択")
        if file_path:
            self.dir_path_display.setText(file_path)

    # ------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------


if __name__ == "__main__":
    # 入力欄
    window_title = "〇〇自動化ツール"
    explain = "〇〇の〇〇自動抽出ツール"
    position_x = 30
    position_y = 30
    size_x = 500
    size_y = 200

    app = QApplication(sys.argv)
    window = GuiIdPassMain(window_title=window_title, position_x=position_x, explain=explain, position_y=position_y, size_x=size_x, size_y=size_y)
    window.show()
    sys.exit(app.exec())

# ----------------------------------------------------------------------------------
