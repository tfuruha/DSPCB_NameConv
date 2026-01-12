import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class DSPCBRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("PCB製造データ・リネーマー")
        self.root.geometry("400x200")
        
        # 変換ルールの定義 (接尾辞と拡張子の対応)
        self.rename_map = {
            " - Top Copper.gbr": ".gtl",
            " - Top Resist.gbr": ".gts",
            " - Top Silkscreen.gbr": ".gto",
            " - Bottom Copper.gbr": ".gbl",
            " - Bottom Resist.gbr": ".gbs",
            " - Bottom Silkscreen.gbr": ".gbo",
            " - Mechanical.gbr": ".gko",
            " - NC Drill Data - [Through Hole].drl": ".txt"
        }

        self.setup_ui()

    def setup_ui(self):
        """UIのセットアップ"""
        label = tk.Label(self.root, text="PCB製造ファイル(gbr/drl)を1つ選択してください。\n一括でリネームを開始します。", pady=20)
        label.pack()

        btn_select = tk.Button(self.root, text="ファイルを選択して実行", command=self.process_conversion, 
                               width=25, height=2, bg="#0078d4", fg="white", font=("BIZ UDゴシック", 10, "bold"))
        btn_select.pack(pady=10)

    def extract_project_name(self, filename):
        """ファイル名からプロジェクト名を抽出する"""
        if " - " in filename:
            return filename.split(" - ")[0]
        return None

    def process_conversion(self):
        """リネーム処理のメインフロー"""
        # 1. ファイル選択 (Windows標準インターフェース)
        file_path = filedialog.askopenfilename(
            title="製造データを1つ選択",
            filetypes=[("Gerber/Drill files", "*.gbr *.drl"), ("All files", "*.*")]
        )
        
        if not file_path:
            return

        target_path = Path(file_path)
        directory = target_path.parent
        filename = target_path.name
        
        # 2. プロジェクト名の特定
        project_name = self.extract_project_name(filename)
        if not project_name:
            messagebox.showerror("エラー", "ファイル名からプロジェクト名（' - ' より前の部分）を特定できませんでした。")
            return

        # 3. 全8ファイルの存在確認
        missing_files = []
        file_list_to_rename = []
        
        for suffix, new_ext in self.rename_map.items():
            src_name = f"{project_name}{suffix}"
            src_path = directory / src_name
            dest_name = f"{project_name}{new_ext}"
            dest_path = directory / dest_name
            
            if src_path.exists():
                file_list_to_rename.append((src_path, dest_path))
            else:
                missing_files.append(src_name)

        # 全て揃っているかチェック
        if missing_files:
            msg = "以下のファイルが見つかりません。中断します。\n\n" + "\n".join(missing_files)
            messagebox.showwarning("ファイル不足", msg)
            return

        # 4. 上書き確認
        overwrite_needed = any(dest.exists() for _, dest in file_list_to_rename)
        if overwrite_needed:
            if not messagebox.askyesno("上書き確認", "変換後のファイル名が既にいくつか存在します。上書きしてもよろしいですか？"):
                return

        # 5. リネーム実行
        try:
            for src, dest in file_list_to_rename:
                # 既にdestが存在する場合に備え、一度削除する(Windowsでの上書き保証)
                if dest.exists():
                    dest.unlink()
                src.rename(dest)
            
            # リネーム成功後、該当フォルダをエクスプローラーで開く
            try:
                os.startfile(directory)
            except:
                pass

            messagebox.showinfo("成功", f"プロジェクト '{project_name}' のリネームが完了しました！")
        except Exception as e:
            messagebox.showerror("エラー", f"エラーが発生しました:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    # Windowsでフォントを綺麗にするための設定(オプション)
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
    
    app = DSPCBRenamer(root)
    root.mainloop()
