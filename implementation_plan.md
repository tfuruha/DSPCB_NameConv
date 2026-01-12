# 実装計画 - PCBリネームツール

## 1. 概要
DesignSpark PCB から出力される製造データのファイル名を、PCBway等の製造業者の指定形式に一括変換するツールです。

## 2. 実装詳細

### A. プロジェクト名の特定
選択されたファイルパスからファイル名を取得し、` - ` で分割。最初の要素をプロジェクト名として保持します。

### B. 変換マップ
以下の対応表に基づいてリネームを行います（DesignSpark PCB 標準形式）。
- ` - Top Copper.gbr` -> `.gtl`
- ` - Top Resist.gbr`   -> `.gts`
- ` - Top Silkscreen.gbr`   -> `.gto`
- ` - Bottom Copper.gbr` -> `.gbl`
- ` - Bottom Resist.gbr`   -> `.gbs`
- ` - Bottom Silkscreen.gbr`   -> `.gbo`
- ` - Mechanical.gbr`   -> `.gko`
- ` - NC Drill Data - [Through Hole].drl` -> `.txt`

### C. バリデーション
- 8つすべてのファイルが存在するか確認。
- 1つでも欠けていれば、欠落しているファイル名をリストアップして警告。

### D. GUI構成
- `tkinter` を使用。
- リネーム開始ボタン。
- 処理結果（成功/失敗/キャンセル）の通知ダイアログ。
- 成功時にフォルダを自動で開く機能。

## 3. リスクと対策
- 同名ファイルが既に存在する場合：`messagebox.askyesno` で上書き確認を行います。
