#  coding: utf-8
# 文字列をすべてここに保管する
# ----------------------------------------------------------------------------------
# 2024/7/17 更新
# tree -I 'venv|resultOutput|__pycache__'
# ? Command + F10で大文字変換
# ----------------------------------------------------------------------------------
# import
import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()


# ----------------------------------------------------------------------------------
# GSS情報


class GmailInfo(Enum):

    GMAIL = {
        "JSON_KEY_NAME": "sns-auto-430920-08274ad68b41.json",
    }

# ----------------------------------------------------------------------------------

class GmailSearchQueryParams(Enum):

    QUERY_PARAMS_DICT = {
        # 検索条件
        # 検索条件に入れない場合には「 "" 」で問題なし
        "subject": "ボランティア応募フォーム",
        "from_email": "",
        "after": "",
        "before": "",
        "has_attachment": False,
    }

# ----------------------------------------------------------------------------------

class GmailBodySearchList(Enum):

    search_word_list_first = [
        '氏名（フリガナ）',
        '氏名',
        '住所',
        '年齢',
        '電話番号',
        'Eメール',
        '活動できる地域',
        '活動できる期間',
        '活動できる内容',
        '自由記入欄',
    ]

# ----------------------------------------------------------------------------------
# GSS情報


class GssInfo(Enum):

    GMAIL = {
        "JSON_KEY_NAME": "sns-auto-430920-08274ad68b41.json",
        "SHEET_URL": "https://docs.google.com/spreadsheets/d/1dghp-9A1vd9WZbybka-2MmrV2-rpm-7wwsI-tRp9jYM/edit?gid=675546558#gid=675546558",
        "WORKSHEET_NAME": "アカウント",

        # column名
        "FURIGANA": "氏名（フリガナ）",
        "NAME": "氏名",
        "ADDRESS": "住所",
        "AGE": "年齢",
        "TEL": "電話番号",
        "MAIL_ADDRESS": "Eメール",
        "REGION": "活動できる地域",
        "ACTION": "活動できる内容",
        "FREE_WRITE": "自由記入欄",
        "": "",
        "": "",

    }


# ----------------------------------------------------------------------------------
# ログイン情報


class LoginInfo(Enum):

    CCX = {
        "LOGIN_URL": "https://social.ccxcloud.io/login",
        "HOME_URL": "",
        "ID_BY": "id",
        "ID_VALUE": "username",
        "PASS_BY": "id",
        "PASS_VALUE": "password",
        "BTN_BY": "xpath",
        "BTN_VALUE": "//button[contains(text(), 'ログイン')]",
        "LOGIN_AFTER_ELEMENT_BY": "xpath",
        "LOGIN_AFTER_ELEMENT_VALUE": "//li[contains(@class, 'sidebar-item') and .//a[contains(text(), 'フォロワー分析')]]",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class ErrCommentInfo(Enum):

    CCX = {

        # POPUP_TITLE
        "POPUP_TITLE_SHEET_INPUT_ERR": "スプレッドシートをご確認ください。",
        "POPUP_TITLE_FACEBOOK_LOGIN_ERR": "ログインが必要です",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class PopUpComment(Enum):
    CCX = {
        "ALL_COMPLETE_TITLE": "完了通知",
        "ALL_COMPLETE_COMMENT": "すべての処理が完了しました。エラー内容をご確認ください",
        "": "",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class FollowerAnalysisElement(Enum):
    CCX = {
        "ZIP_FILE_HEAD_NAME": "Instagramマイアカウント フォロワー分析",
        "ZIP_EXTENSION": ".zip",
        "CSV_FILE_HEAD_NAME": "フォロワーチャート",
        "CSV_EXTENSION": ".csv",
        "DOWNLOAD_DIR_NAME": "downloads",
        "UPLOAD_DIR_NAME": "uploads_to_google_drive",

        "ANALYSIS_BY": "",
        "ANALYSIS_VOL": "//a[contains(text(), 'フォロワー分析')]",
        "BULK_DOWNLOAD_BTN_BY": "",
        "BULK_DOWNLOAD_BTN_VOL": "//button[.//span[contains(text(), '一括DL')]]",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class EngagementAnalysisElement(Enum):
    CCX = {
        "ZIP_FILE_HEAD_NAME": "Instagramマイアカウント エンゲージメント分析",

        "ZIP_EXTENSION": ".zip",
        "CSV_FILE_HEAD_FIRST_NAME": "エンゲージメントの推移",
        "CSV_FILE_HEAD_SECOND_NAME": "プロフィールインサイトチャート",

        "CSV_EXTENSION": ".csv",
        "DOWNLOAD_DIR_NAME": "downloads",
        "UPLOAD_DIR_NAME": "uploads_to_google_drive",

        "ANALYSIS_BY": "",
        "ANALYSIS_VOL": "//a[contains(text(), 'エンゲージメント分析')]",
        "BULK_DOWNLOAD_BTN_BY": "",
        "BULK_DOWNLOAD_BTN_VOL": "//button[.//span[contains(text(), '一括DL')]]",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class PostAnalysisElement(Enum):
    CCX = {
        "ZIP_FILE_HEAD_NAME": "Instagramマイアカウント 投稿一覧",
        "ZIP_EXTENSION": ".zip",
        "CSV_FILE_HEAD_NAME": "インサイト投稿一覧",
        "CSV_EXTENSION": ".csv",
        "DOWNLOAD_DIR_NAME": "downloads",
        "UPLOAD_DIR_NAME": "uploads_to_google_drive",

        "ANALYSIS_BY": "",
        "ANALYSIS_VOL": "//a[contains(text(), '投稿一覧')]",
        "BULK_DOWNLOAD_BTN_BY": "",
        "BULK_DOWNLOAD_BTN_VOL": "//button[.//span[contains(text(), '一括DL')]]",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------


class StoriesAnalysisElement(Enum):
    CCX = {
        "ZIP_FILE_HEAD_NAME": "Instagramマイアカウント ストーリーズ分析",
        "ZIP_EXTENSION": ".zip",
        "CSV_FILE_HEAD_NAME": "ストーリーズ投稿一覧",
        "CSV_EXTENSION": ".csv",
        "DOWNLOAD_DIR_NAME": "downloads",
        "UPLOAD_DIR_NAME": "uploads_to_google_drive",

        "ANALYSIS_BY": "",
        "ANALYSIS_VOL": "//a[contains(text(), 'ストーリーズ分析')]",
        "BULK_DOWNLOAD_BTN_BY": "",
        "BULK_DOWNLOAD_BTN_VOL": "//button[.//span[contains(text(), '一括DL')]]",
        "": "",
        "": "",
    }


# ----------------------------------------------------------------------------------

class Element(Enum):
    CCX = {
        "MATCH_RULES_BY": "",
        "MATCH_RULES_VOL": "//input[@id='has_condition2']",
        "MATCH_CHOICE_BY": "xpath",
        "MATCH_CHOICE_VOL": "//select[@name='condition[0][0][key]']",
        "MATCH_CHOICE_SELECT_VOL": "base_date",
        "DELIVERY_SETTING_SELECT_BY": "xpath",
        "DELIVERY_SETTING_SELECT_VALUE": "//select[contains(@class, 'condition-condition')]",
        "SETTING_SELECT_VALUE": "equal",
        "DATE_INPUT_BY": "xpath",
        "DATE_INPUT_VOL": "//div[contains(@class, 'condition-input')]//input[@type='date']",
        "SORTING_BY": "xpath",
        "SORTING_VOL": "//button[@type='submit' and contains(text(), '絞り込む')]",
        "CSV_OUTPUT_VOL": "//a[contains(text(), 'CSV出力')]",
        "CSV_FILE_NAME": "登録者_",
        "CSV_EXTENSION": ".csv",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",

    }

# ----------------------------------------------------------------------------------


