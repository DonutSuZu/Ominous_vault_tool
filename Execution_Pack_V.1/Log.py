#V.1.0.0-Win11-Cu126-LateMiMiLion-TrialCat
import os
import sys
from datetime import datetime

class Logger:
    def __init__(self, file):
        self.terminal = sys.__stdout__
        self.log = file

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

def setup_logger():
    # ログディレクトリ作成
    log_dir = "Log"
    os.makedirs(log_dir, exist_ok=True)

    # 基本ファイルパス
    base_log_path = os.path.join(log_dir, "log.txt")

    # ファイル名が存在する場合 → 名前を変更して退避
    if os.path.exists(base_log_path):
        now = datetime.now().strftime("%Y_%m月%d日_%H時%M分")
        new_log_name = f"Latest_{now}_log.txt"
        new_log_path = os.path.join(log_dir, new_log_name)
        os.rename(base_log_path, new_log_path)

    # ログ.txt を新規作成（print 出力をここにリダイレクト）
    log_file = open(base_log_path, "w", encoding="utf-8")
    #print(f"✅[Debug]:Log_file_Create_Success.✅")
    return Logger(log_file)