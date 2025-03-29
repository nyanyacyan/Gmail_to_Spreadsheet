# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/remove_meta_in_image/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import sys
from PySide6.QtWidgets import ( QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout )


# flow
from method.logger import Logger
from method.image_meta_remove import ImageMetaRemove

# ----------------------------------------------------------------------------------
# **********************************************************************************
# Dirを取得するGUI

class GuiDirMain(QWidget):
    def __init__(self, window_title: str, size_x: int, size_y: int, explain: str, position_x: int=100, position_y: int=100):
        super().__init__()
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

        self.setWindowTitle(window_title)
        self.setGeometry(position_x, position_y, size_x, size_y)


        #? --- ディレクトリ選択 ---
        # 説明書き部分のラベル
        self.dir_label = QLabel(explain)

        # 選んだPathを表示
        self.dir_path_display = QLineEdit()  # Pathの表示させるメソッド
        self.dir_path_display.setReadOnly(True)

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

        # Pathを選択するレイアウト
        dir_layout = QHBoxLayout()  # 横並びにするレイアウト
        dir_layout.addWidget(self.dir_path_display)
        dir_layout.addWidget(self.dir_button)

        # Pathを選択するレイアウトを基礎レイアウトに追加
        layout.addWidget(self.dir_label)
        layout.addLayout(dir_layout)

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
        self.image_meta_remove = ImageMetaRemove()
        input_path = self.dir_path_display.text()
        self.logger.debug(f'input_path: {input_path}')

        self.image_meta_remove.flow_process(input_path=self.dir_path_display.text())

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
    window_title = "Meta情報除去ツール"
    explain = "Meta情報を除去したいファイルを選択して下さい。"
    position_x = 30
    position_y = 30
    size_x = 500
    size_y = 150

    app = QApplication(sys.argv)
    window = GuiDirMain(window_title=window_title, position_x=position_x, explain=explain, position_y=position_y, size_x=size_x, size_y=size_y)
    window.show()
    sys.exit(app.exec())

# ----------------------------------------------------------------------------------
