# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/remove_meta_in_image/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import sys, os
import gspread
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from typing import Dict, List
import pandas as pd

# flow
from method.logger import Logger
from method.image_meta_remove import ImageMetaRemove
from method.path import BaseToPath

# ----------------------------------------------------------------------------------
# **********************************************************************************
# Dirを取得するGUI

class Gmail:
    def __init__(self):
        super().__init__()
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

        self.path = BaseToPath()


# **********************************************************************************


    #!##############################################################################
    #? 実行処理

    def handle_submit(self):
        pass

    #!##############################################################################
    # Gmailの認証してサービスオブジェクトの作成

    def creds(self, token_path: str, json_key_name: str):
        SCOPES = ['https://www.googleapis.com/auth/gmail.modify']  # 送信+受信
        json_key_path = self.path._get_secret_key_path(file_name=json_key_name)  # jsonKeyNameのパスを取得
        token_path = self._get_token_path(file_name=token_path)  # tokenのパスを取得

        creds = None

        # tokenが存在する場合は、tokenを読み込む
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

        # tokenが存在しない場合は、認証を行う
        if not creds or not creds.valid:  # tokenがない、またはtokenが無効な場合
            if creds and creds.expired and creds.refresh_token:  # tokenが期限切れで、refresh_tokenがある場合
                creds.refresh(Request())  # トークンの更新
            else:
                flow = InstalledAppFlow.from_client_secrets_file(json_key_path, SCOPES)  # 認証フローの作成
                creds = flow.run_local_server(port=0)  # ブラウザを開いて認証を行い、tokenを取得する

            # トークンを保存
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        # Gmailのサービスオブジェクトを作成
        gmail_service = build('gmail', 'v1', credentials=creds)
        return gmail_service

    # ----------------------------------------------------------------------------------
    # token_path

    def _get_token_path(self, file_name: str="token.json"):
        token_path = os.path.join(self.path._get_secret_key_path(), file_name)
        return token_path

    # ----------------------------------------------------------------------------------
    # 対象のメールを検索して取得する（メールIDの取得）

    def _get_search_mail(self, gmail_service, query: str):
        mail_id_list = gmail_service.users().messages().list(userId='me', q=query).execute()
        self.logger.debug(f'results: {mail_id_list}')
        mail_list = mail_id_list.get('messages', [])
        self.logger.debug(f'mail_list: {mail_list}')

        if not mail_list:
            self.logger.info('対象のメールはありませんでした。')
            return []

        else:
            self.logger.debug(f'対象のメールを {len(mail_list)} 件、取得しました。')
            return mail_list

    # ----------------------------------------------------------------------------------
    # クエリ例文
    # subject:xxx	件名に xxx を含む
    # from:xxx@gmail.com	差出人が xxx@gmail.com
    # after:2024/12/01	2024年12月1日以降のメール
    # before:2025/01/01	2025年1月1日より前のメール
    # has:attachment	添付ファイルありのメールだけ取得



    # ----------------------------------------------------------------------------------
    # メールの中身をデバッグする

    # メール件名からメールを取得する


    # メール本文を取得


    # メール本文から特定のワードの内容を取得する（辞書で返す）
