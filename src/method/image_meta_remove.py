# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/remove_exif/installer/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import os
from pathlib import Path
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# 自作モジュール
from method.logger import Logger
from method.path import BaseToPath

# ----------------------------------------------------------------------------------
# **********************************************************************************
# 一連の流れ


class ImageMetaRemove:
    def __init__(self):
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

    #? ----------------------------------------------------------------------------------

    # メタデータが除去されているか確認するには
    # ターミナルにて [exiftool] コマンドを使う → exiftool my_file_path

    #? ----------------------------------------------------------------------------------
    #!###################################################################################
    # 1行のみあるtext画像のOCR抽出(canvas画像)

    def flow_process(self, input_path: Path, extension: str = ".png") -> Path:
        try:
            input_path_file_name = os.path.basename(input_path)
            add_word = "_meta除去済み"
            file_name = input_path_file_name.split('.')[0] + add_word
            self.logger.debug(f'only_file_name: {file_name}')

            sub_dir_name = "meta_remove_photo"
            output_path = self._get_output_path(sub_dir_name=sub_dir_name, file_name=file_name, extension=extension)
            self.logger.debug(f'output_path: {output_path}')

            image = Image.open(input_path)
            data = list(image.getdata())
            image_no_exif = Image.new(image.mode, image.size)
            self.logger.debug(f'image_no_exif: {image_no_exif}')

            image_no_exif.putdata(data)
            image_no_exif.save(output_path)

        except Exception as e:
            self.logger.error(f'{self.__class__.__name__} 処理中にエラー発生: {e}')

        return output_path

    #!###################################################################################
    # ----------------------------------------------------------------------------------


    def _get_output_path(self, sub_dir_name: str, file_name: str, extension: str) -> Path:
        path = BaseToPath()
        return path.getResultSubDirFilePath(subDirName=sub_dir_name, fileName=file_name, extension=extension)

    # ------------------------------------------------------------------------------

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()


    # ファイル選択ダイアログを表示
    input_path = filedialog.askopenfilename(title="meta情報を除去したいPhotoファイルを選択してください")

    # 出力パスを "_noexif" をファイル名に付けて同じディレクトリに保存
    output_path = input_path.with_stem(input_path.stem + "_noexif")


    image_meta_remove = ImageMetaRemove()
    image_meta_remove.flow_process(input_path=input_path, output_path=output_path)
