# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/remove_meta_in_image/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import sys, os
import gspread
from googleapiclient.discovery import Resource
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from typing import Dict, List, Any
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

    def _get_search_mail(self, gmail_service: Resource, **query_params: Any):
        """
        対象のメールを検索して取得する（メールIDの取得）
        :param gmail_service: Gmailのサービスオブジェクト
        :param query_params: 検索条件
            subject: 件名
            from_email: 送信者
            after: 取得するメールの最終日付
            before: 取得するメールの最初日付
            has_attachment: 添付ファイルがあるメールを取得するかどうか

        :query_params渡し方例
            query_params = {
                'subject': '申込み',
                'after': '2025/01/01',
                'before': '2025/03/01'
            }
        """

        self.logger.debug(f'query_params: {query_params}')
        query = self._build_query(**query_params)
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
    # クエリを作成する

    def _build_query(self, subject: str=None, from_email: str=None, after: str=None, before: str=None, has_attachment: bool=False):
        query_parts = []
        if subject:
            query_parts.append(f'subject:{subject}')  # 件名に xxx を含む
        if from_email:
            query_parts.append(f'from:{from_email}')  # 送信してきた相手
        if after:
            query_parts.append(f'after:{after}')  # 2024年12月1日以降のメール
        if before:
            query_parts.append(f'before:{before}')  # 2025年1月1日より前のメール
        if has_attachment:
            query_parts.append('has:attachment')  # 添付ファイルありのメールだけ取得
        query = ' '.join(query_parts)
        self.logger.debug(f'query: {query}')
        return query

    # ----------------------------------------------------------------------------------
    # メールの中身をデバッグする

    # メール件名からメールを取得する


    # メール本文を取得


    # メール本文から特定のワードの内容を取得する（辞書で返す）
