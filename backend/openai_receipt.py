# いったん完成(2026.07.03)

from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
import json
import mimetypes

from prompts import RECEIPT_PROMPT

# .env 読み込み
load_dotenv("../.env") # フォルダ構造変更に伴って変更する部分

# apiキー読み込み
api_key = os.getenv("OPENAI_API_KEY")

# クライアント作成（環境変数から取得）
client = OpenAI(api_key=api_key)

def encode_image(image_path):
    """
    画像ファイルをbase64に変換する
    """
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def extract_foods(image_path: str):
    """
    レシート画像を解析し、購入日と食品情報をJSON(dict)で返す。

    Parameters:
        image_path (str): レシート画像のパス

    Returns:
        dict: AIが抽出した購入情報
    """

    # 画像タイプ適応
    mime_type, _ = mimetypes.guess_type(image_path)
    mime_type = mime_type or "image/jpeg"

    base64_image = encode_image(image_path) # 画像をbase64へ変換

    # OpenAIへリクエスト
    response = client.responses.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": RECEIPT_PROMPT
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{base64_image}"
                    }
                ]
            }
        ]
    )

    # JSONに変換して返す
    try:
        return json.loads(response.output_text)
    except Exception:
        return {
            "purchase_date": None,
            "foods": []
        }