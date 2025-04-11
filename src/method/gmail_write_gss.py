# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/remove_meta_in_image/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import sys, os, base64, time
import gspread
from googleapiclient.discovery import Resource
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from typing import Dict, List, Any
import pandas as pd

# const
from const_element import GssInfo, GmailSearchQueryParams, GmailBodySearchList

# 自作モジュール
from method.gmail import Gmail
from method.spreadsheetRead import GetDataGSSAPI
from method.select_cell import GssSelectCell
from method.spreadsheetWrite import GssWrite

# flow
from method.logger import Logger
from method.image_meta_remove import ImageMetaRemove
from method.path import BaseToPath

# ----------------------------------------------------------------------------------
# **********************************************************************************
# Dirを取得するGUI

class GmailWriteGss:
    def __init__(self):
        super().__init__()
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

        # インスタンス
        self.gss_read = GetDataGSSAPI()
        self.gss_write = GssWrite()
        self.gmail = Gmail()
        self.path = BaseToPath()
        self.select_cell = GssSelectCell()

        # const
        self.const_gss_info = GssInfo.GMAIL.value

# **********************************************************************************
    #!##############################################################################

    def process(self):
        body_data_list = self._get_gmail_body_dict_list()

    #!##############################################################################
    # ----------------------------------------------------------------------------------
    #? 指定の件名のGmailを取得して、本文から特定のワードを取得する
    #? 取得したワードはリスト型で返す

    def _get_gmail_body_dict_list(self):
        return self.gmail.process()

    # ----------------------------------------------------------------------------------

    def _get_gss_df(self):
        # GSSへアクセス→gss_row_dataにあるURLへアクセス
        worksheet_name = self.const_gss_info["WORKSHEET_NAME"]
        self.logger.debug(f'worksheet_name: {worksheet_name}')
        gss_df = self.gss_read._get_gss_df_to_gui(gui_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=worksheet_name)
        self.logger.debug(f'gss_df: \n{gss_df.head()}')
        return gss_df

    # ----------------------------------------------------------------------------------
    # dfの長さを取得する

    def _get_input_row_num(self, gss_df: pd.DataFrame) -> int:
        return self.gss_read._get_input_row_num(gss_df)

    # ----------------------------------------------------------------------------------

    def _get_none_sell_row_num(self, gss_df: pd.DataFrame) -> int:
        if gss_df.empty:
            self.logger.info("対象のスプレッドシートは空です。全データを書き込み対象とします。")
            none_row_num = 1  # ヘッダー行を除いた次の行
        else:
            # 空白の行数
            none_row_num = self.gss_df(df=gss_df)

        self.logger.debug(f'none_row_num: {none_row_num}')
        return none_row_num

    # ----------------------------------------------------------------------------------


    def _gss_row_write(self, gss_df: pd.DataFrame, col_name: str, none_row_num: int, gmail_body_data: Dict) -> None:
        for i, row in  gss_df.iterrows():
            row_num = i + none_row_num
            self.logger.debug(f'row_num: {row_num}')



            # 対象のセルアドレスに書込

    # ----------------------------------------------------------------------------------
    # body_data → 辞書データ → 存在確認 → 書き込む

    def _write_exits_value(self, gmail_body_data: Dict, cell_address: str) -> None:
        furigana_data =  gmail_body_data[self.const_gss_info["GMAIL"]["FURIGANA"]]
        name_data =  gmail_body_data[self.const_gss_info["GMAIL"]["NAME"]]
        address_data =  gmail_body_data[self.const_gss_info["GMAIL"]["ADDRESS"]]
        age_data =  gmail_body_data[self.const_gss_info["GMAIL"]["AGE"]]
        tel_data =  gmail_body_data[self.const_gss_info["GMAIL"]["TEL"]]
        mail_address_data =  gmail_body_data[self.const_gss_info["GMAIL"]["MAIL_ADDRESS"]]
        region_data =  gmail_body_data[self.const_gss_info["GMAIL"]["REGION"]]
        action_data =  gmail_body_data[self.const_gss_info["GMAIL"]["ACTION"]]
        free_write_data =  gmail_body_data[self.const_gss_info["GMAIL"]["FREE_WRITE"]]

        furigana_col_name = self.const_gss_info.Gmail.FURIGANA.value
        name_col_name = self.const_gss_info.Gmail.NAME.value
        address_col_name = self.const_gss_info.Gmail.ADDRESS.value
        age_col_name = self.const_gss_info.Gmail.AGE.value
        tel_col_name = self.const_gss_info.Gmail.TEL.value
        mail_address_col_name = self.const_gss_info.Gmail.MAIL_ADDRESS.value
        region_col_name = self.const_gss_info.Gmail.REGION.value
        action_col_name = self.const_gss_info.Gmail.ACTION.value
        free_write_col_name = self.const_gss_info.Gmail.FREE_WRITE.value

        # ふりがな書込
        if furigana_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=furigana_col_name, row_num=furigana_data)
            self.logger.debug(f'{furigana_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=furigana_data)
        else:
            self.logger.debug(f'{furigana_col_name} は空白です。')

        # 氏名書込
        if name_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=name_col_name, row_num=name_data)
            self.logger.debug(f'{name_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=name_data)
        else:
            self.logger.debug(f'{name_col_name} は空白です。')

        # 住所書込
        if address_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=address_col_name, row_num=address_data)
            self.logger.debug(f'{address_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=address_data)
        else:
            self.logger.debug(f'{address_col_name} は空白です。')

        # 年齢書込
        if age_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=age_col_name, row_num=age_data)
            self.logger.debug(f'{age_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=age_data)
        else:
            self.logger.debug(f'{age_col_name} は空白です。')

        # 電話番号書込
        if tel_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=tel_col_name, row_num=tel_data)
            self.logger.debug(f'{tel_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=tel_data)
        else:
            self.logger.debug(f'{tel_col_name} は空白です。')

        # メールアドレス書込
        if mail_address_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=mail_address_col_name, row_num=mail_address_data)
            self.logger.debug(f'{mail_address_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=mail_address_data)
        else:
            self.logger.debug(f'{mail_address_col_name} は空白です。')

        # 地域書込
        if region_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=region_col_name, row_num=region_data)
            self.logger.debug(f'{region_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=region_data)
        else:
            self.logger.debug(f'{region_col_name} は空白です。')

        # 活動内容書込
        if action_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=action_col_name, row_num=action_data)
            self.logger.debug(f'{action_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=action_data)
        else:
            self.logger.debug(f'{action_col_name} は空白です。')

        # 自由記入書込
        if free_write_data:
            # セルのアドレスを取得
            cell_address = self.select_cell.get_cell_address(gss_row_dict=gmail_body_data, col_name=free_write_col_name, row_num=free_write_data)
            self.logger.debug(f'{free_write_col_name} の cell_address: {cell_address}')

            # セルのアドレスに書込
            self.gss_write.write_gss_base_cell_address(gss_info=self.const_gss_info, sheet_url=self.const_gss_info["SHEET_URL"], worksheet_name=self.const_gss_info["WORKSHEET_NAME"], cell_address=cell_address, input_value=free_write_data)
        else:
            self.logger.debug(f'{free_write_col_name} は空白です。')
    # ----------------------------------------------------------------------------------
