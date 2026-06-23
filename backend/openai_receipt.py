# OpenAIクライアントを作るところまで

from openai import OpenAI
import os
from dotenv import load_dotenv

# .env 読み込み
load_dotenv("../.env") # フォルダ構造変更に伴って変更する部分

print("ライブラリ読み込み成功")

# apiキー読み込み
api_key = os.getenv("OPENAI_API_KEY")

# 読み込み可否判定
if api_key:
    print("APIキーを読み込めました")
else:
    print("APIキーが読み込めていません")

# クライアント作成（環境変数から取得）
client = OpenAI(api_key=api_key)