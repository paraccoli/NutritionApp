# 栄養トラッカーアプリケーション

## 概要
このアプリケーションは、日々の食事と栄養摂取を追跡するためのPython製のGUIツールです。SQLiteデータベースを使用してデータを保存し、ユーザーインターフェースは日本語と英語に対応しています。

## 特徴
- ユーザー認証システム
- 食事の記録と追跡
- 日別および週別の栄養サマリー
- カスタム食品の追加機能
- 栄養摂取のグラフ表示
- 食事記録の編集と削除機能
- データのエクスポートとインポート機能（未実装）
- 日本語と英語に対応したユーザーインターフェース
- ユーザープロファイル管理

## 必要条件
- Python 3.6以上
- tkinter
- SQLAlchemy
- matplotlib
- bcrypt

## インストール方法
1. このリポジトリをクローンまたはダウンロードします。
2. 必要なライブラリをインストールします：
```
pip install sqlalchemy matplotlib bcrypt
```

## 使用方法
1. 以下のコマンドでアプリケーションを実行します：
```
python main.py
```
2. GUIウィンドウが開きます。
3. 新規ユーザーの場合は登録を行い、既存ユーザーの場合はログインします。
4. ダッシュボードで栄養摂取の概要を確認できます。
5. 「食事を追加」タブで新しい食事を記録します。
6. 「栄養サマリー」タブで詳細な栄養情報を確認できます。
7. 「プロフィール」タブでユーザー情報を管理します。
8. 言語を変更するには、「File」メニューから「Settings」を選択します。

## ファイル構成
- `main.py`: アプリケーションのエントリーポイント
- `gui/`: GUIコンポーネントを含むディレクトリ
- `services/`: ビジネスロジックを提供するサービス
- `database/`: データベース関連のファイル
- `utils/`: ユーティリティ関数とローカライゼーション
- `resources/`: 言語リソースファイル

## セキュリティについて
- このアプリケーションはbcryptを使用してパスワードをハッシュ化しています。
- ユーザーデータはローカルのSQLiteデータベースに保存されます。
- このツールは個人使用を目的としています。

## 今後の展望
- モバイルアプリとの連携機能
- 栄養目標の設定と進捗トラッキング
- レシピ推奨機能
- データの視覚化の強化

## 作成者 Developer
- 作成者: パラッコリー(ID：Paraccoli)
- GitHub: https://github.com/paraccoli
- Zenn: https://zenn.dev/miguel

---

# Nutrition Tracker Application

## Overview
This application is a Python-based GUI tool for tracking daily meals and nutritional intake. It uses SQLite database for data storage and supports user interfaces in Japanese and English.

[English version of the features, requirements, installation, usage, etc.. update coming soon]
