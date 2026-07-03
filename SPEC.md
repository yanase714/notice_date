# 共有事項


## フォルダ構成

```bash
receipt-expiration-app/
├─ frontend/
│ ├─app/
│ │ ├─ index.tsx
│ │ ├─ camera.tsx
│ │ ├─ confirm.tsx
│ │ ├─ edit.tsx
│ │ └─ notification.tsx
│ │
│ ├─components/
│ │ ├─ FoodItemCard.tsx
│ │ ├─ ExpirationForm.tsx
│ │ └─ NotificationCard.tsx
│ │
│ ├─utils/
│ │ ├─ api.ts
│ │ └─ date.ts
│ │
│ └─ package.json
│
├─ backend/
│ ├─ main.py
│ ├─ openai_receipt.py
│ ├─ food_normalizer.py
│ ├─ expiration.py
│ ├─ database.py
│ └─ models.py
│
├─ data/
│ └─ food_expiration_master.csv
│
├─ .env
├─ README.md
└─ requirements.txt
```


## JSON形式

### AI出力(消費期限・賞味期限計算前)

```bash
{
  "purchase_date": "YYYY-MM-DD",
  "foods": [
    {
      "name": "食材名",
      "quantity": "数量"
    }
  ]
}
```

### 消費期限・賞味期限計算後

```bash
{
  "purchase_date": "YYYY-MM-DD",
  "foods": [
    {
      "name": "食材名",
      "quantity": "数量",
      "expiration_date": "YYYY-MM-DD"

    }
  ]
}
```

### 項目
| キー | 型 | 説明 |
|------|----|------|
| purchase_date | string | レシートの購入日（YYYY-MM-DD） |
| foods | array | 食品一覧 |
| name | string | 一般的な食材名（例：牛乳，卵） |
| quantity | string \| null | 数量・容量（例：1本，500g）。取得できない場合は `null` |
| expiration_date | string | 消費期限・賞味期限（YYYY-MM-DD）．AI出力時には含まれず，バックエンドで追加 |

