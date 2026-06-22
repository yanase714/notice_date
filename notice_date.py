from openai import OpenAI
from dotenv import load_dotenv

print("ライブラリ読み込み成功")

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("APIキーを読み込めました")
else:
    print("APIキーが読み込めていません")