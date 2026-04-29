# PCB製造データリネームツール (DSPCB_Renamer)

DesignSpark PCBから出力される製造データ（ガーバーファイルおよびドリルファイル）を、基板製造業者が指定するファイル名形式へ一括変換するためのGUIアプリケーションです。

## 主な機能
- **一括リネームと整理**: プロジェクトの構成ファイルを1つ選択するだけで、関連する全ファイルを特定し、指定の形式にリネームします。
- **自動フォルダ仕分け**: リネーム実行時、プロジェクト名に基づいたサブフォルダを自動的に作成し、変換後のファイルをその中へ集約します。これにより、製造依頼時のZIP圧縮作業が容易になります。
- **整合性チェック**: リネーム実行前に、必要な全8種類のファイルが揃っているかを確認し、不足がある場合は処理を中断します。
- **上書き保護**: 変換後のファイルが既に出力先に存在する場合、ユーザーに確認を促すダイアログを表示します。
- **自動フォルダ展開**: 処理完了後、変換後のファイルが格納されたフォルダをエクスプローラーで自動的に開きます。

## 実行環境
Python 3.x がインストールされている環境であれば、標準ライブラリのみで動作するため追加のライブラリインストールは不要です。

```bash
python DSPCB_Renamer.py
```

## 変換仕様
以下の接尾辞を持つファイルを検出し、対応する拡張子へリネームおよび移動を行います。

| 元ファイル名の接尾辞 | 変換後の拡張子 | 内容 |
| :--- | :--- | :--- |
| ` - Top Copper.gbr` | `.gtl` | Top Copper |
| ` - Top Resist.gbr` | `.gts` | Top Solder Resist |
| ` - Top Silkscreen.gbr` | `.gto` | Top Silkscreen |
| ` - Bottom Copper.gbr` | `.gbl` | Bottom Copper |
| ` - Bottom Resist.gbr` | `.gbs` | Bottom Solder Resist |
| ` - Bottom Silkscreen.gbr` | `.gbo` | Bottom Silkscreen |
| ` - Mechanical.gbr` | `.gko` | Keep-out Layer / Outline |
| ` - NC Drill Data - [Through Hole].drl` | `.txt` | NC Drill Data |

※ `[プロジェクト名] - [リソース名]` というファイル名形式を前提としています。

## テスト手順
1. `python create_test_files.py` を実行し、`test_data` ディレクトリ内に検証用のダミーファイルを生成します。
2. `python DSPCB_Renamer.py` を起動し、生成されたファイルのうちいずれか1つを選択して動作を検証してください。

---
対応OS: Windows 11
