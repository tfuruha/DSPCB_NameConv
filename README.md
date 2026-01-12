# PCBリネームツール (DSPCB_Renamer)

DesignSpark PCB から出力される製造データ（ガーバーファイル・ドリルファイル）を、PCBwayなどの基板製造業者が指定するファイル名形式へ一括変換するGUIアプリです。

## 🚀 特徴
- **直感的な操作**: 変換したいプロジェクトのファイルを1つ選択するだけで、他の関連ファイルを自動的に特定しリネームします。
- **安心のバリデーション**: リネーム前に必要なファイル（8種類）が揃っているかチェックし、不足があれば警告します。
- **誤操作防止**: 変換後のファイルが既に存在する場合は、上書き確認ダイアログを表示します。
- **自動エクスプローラー起動**: リネーム成功後、対象フォルダを自動で開きます。

## 🛠️ インストールと実行
Python 3.x がインストールされていれば、追加のライブラリは不要（標準ライブラリのみ使用）で動作します。

```bash
python DSPCB_Renamer.py
```

## 📋 変換ルール
以下の接尾辞を持つファイルを対応する拡張子へリネームします。

| 元ファイル名の接尾辞 | リネーム後の拡張子 | 内容 |
| :--- | :--- | :--- |
| ` - Top Copper.gbr` | `.gtl` | Top Copper |
| ` - Top Resist.gbr` | `.gts` | Top Solder Resist |
| ` - Top Silkscreen.gbr` | `.gto` | Top Silkscreen |
| ` - Bottom Copper.gbr` | `.gbl` | Bottom Copper |
| ` - Bottom Resist.gbr` | `.gbs` | Bottom Solder Resist |
| ` - Bottom Silkscreen.gbr` | `.gbo` | Bottom Silkscreen |
| ` - Mechanical.gbr` | `.gko` | Keep-out Layer / Outline |
| ` - NC Drill Data - [Through Hole].drl` | `.txt` | NC Drill Data |

※ `[プロジェクト名] - [リソース名]` というファイル名形式を想定しています。

## 🧪 テスト方法
1. `python create_test_files.py` を実行して、`test_data` フォルダにダミーファイルを生成します。
2. `python DSPCB_Renamer.py` を起動し、生成されたファイルをどれか1つ選択して動作を確認してください。

---
Developed for Windows 11.
