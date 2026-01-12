import os
from pathlib import Path

def create_mock():
    # テスト用のフォルダを作成
    test_dir = Path("test_data")
    test_dir.mkdir(exist_ok=True)
    
    project = "NiMHCHG_22025"
    suffixes = [
        " - Top Copper.gbr", " - Top Resist.gbr", " - Top Silkscreen.gbr",
        " - Bottom Copper.gbr", " - Bottom Resist.gbr", " - Bottom Silkscreen.gbr",
        " - Mechanical.gbr", " - NC Drill Data - [Through Hole].drl"
    ]
    
    for s in suffixes:
        file_path = test_dir / f"{project}{s}"
        with open(file_path, "w") as f:
            f.write("DUMMY DATA")
    
    print(f"'{test_dir}' フォルダにテスト用ファイルを作成しました。")
    print("DSPCB_Renamer.py を実行し、このフォルダ内のファイルをどれか1つ選んでみてください。")

if __name__ == "__main__":
    create_mock()
