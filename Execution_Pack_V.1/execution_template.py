# 不吉な宝物庫-目押し全自動ツール! by DonutSuZu
#2025/06/30:19:32
from ultralytics import YOLO
from multiprocessing import freeze_support
import pyautogui
import mss
import mss.tools
import numpy as np
import time
import cv2
import keyboard
import os
import sys
from Log import setup_logger

# print出力をログファイルに保存
sys.stdout = setup_logger()


#setting_info
# モデルの読み込み
model = YOLO("./PT/Ominous.pt")  # 学習済みのファイル名

#対象のクラスid
setting_id = 0
"""
0:ヘビーコア
#1:金リンゴ
2:エンチャント金リンゴ
3:エメラルド
4:クロスボウ
5:レコード
6:ダイアモンド
7:ウインドチャージ
8:旗の模様
9:鈍化の矢
10:不吉な瓶
11:ダイヤモンドの斧
12:NONE(使われていない)
13:ダイヤモンド防具
14:エメラルドブロック
15:鍛冶型
16:鉄ブロック
17:エンチャント本
18:ダイヤモンドブロック
"""
iolist = ['heavycore', 'apple', 'goldenapple', 'emerald', 'crossbow', 'record', 'diamond', 'windburst', 'hennano', 'string', 'hukitu', 'AXE', 'Back', 'diamond_chestplate', 'Emeblock', 'KAGIGATA', 'iron_block', 'Book', 'diamond_brock']


# スクリーンキャプチャ関数
def grab_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # メイン画面（複数あるなら注意）
        img = np.array(sct.grab(monitor))
        return img[..., :3]  # RGB
        

def clear_console():
    """OSに応じてコマンドプロンプト/ターミナルの表示をクリアします。"""
    if os.name == 'nt':  # Windowsの場合
        os.system('cls')
    else:  # macOSやLinuxの場合
        os.system('clear')

def search_on_Display():
    try:
        while True:
            frame = grab_screen()
            results = model.predict(source=frame, conf=0.45, verbose=False)
        
            for r in results:
                for box in r.boxes:
                    class_id = int(box.cls[0])
                    #print(f"[Debug]:検知: ({iolist[class_id]})")
                    if class_id == setting_id:  # 対象のクラスID
                        pyautogui.rightClick(942, 640)
                        print(f"✅[Notify]:指定のアイテムを検知しました。: ({iolist[class_id]})")                     
                        time.sleep(1.0)  # 連続クリック防止
            if keyboard.is_pressed("esc"):
                print("⛔[Debug]:Process/search_on_Display_停止しました。")
                break
    except:
        print("[Debug]:Error.Function_search_on_Display") 
        
        
# メインループ
def main():
    global setting_id
    try:
        print(f"ID_List\n0:ヘビーコア\n1:金リンゴ\n2:エンチャント金リンゴ\n3:エメラルド\n4:クロスボウ\n5:レコード\n6:ダイアモンド\n7:ウインドチャージ\n8:旗の模様\n9:鈍化の矢\n10:不吉な瓶\n11:ダイヤモンドの斧\n12:NONE(使われていない)\n13:ダイヤモンド防具\n14:エメラルドブロック\n15:鍛冶型\n16:鉄ブロック\n17:エンチャント本\n18:ダイヤモンドブロック")
        # ユーザーからの入力を受け取る
        user_input = input("対象のID(整数/半角)を入力してください: ")
        time.sleep(3) 
        #print("⛔[Debug]:入力を受け付けました。設定を開始します。")
        # 入力を整数に変換して変数に格納する
        number = int(user_input)
        # 格納された数値を出力して確認する
        print(f"入力されたIDは: {number} です。")
        #print(f"⛔[Debug]:変数の型は: {type(number)} です。")
        setting_id = number
        #print(f"⛔[Debug]:setting_idは: {setting_id} です。")
    
    except ValueError:
        print("⛔[Error]: 有効な整数が入力されませんでした。数字を入力してください。")
    except Exception as e:
        print(f"⛔[Error]:予期せぬエラーが発生しました: {e}")
        
    print("✅[System]:設定中...起動を開始します。")
    time.sleep(3) 
    #クリア()
    clear_console()
    
    print(f"😸不吉な宝物庫-目押し全自動ツール! by DonutSuZu😸")
    print("V.1.0.0-Win11-Cu126-LateMiMiLion-TrialCat")
    print(f"Target_Block:Ominous_vault_Container_[{iolist[setting_id]}]")
    print("Devlopment by SuZu")
    print(f"🕵️‍♂️[{iolist[setting_id]}]の検出を開始します（Esc長押しで終了)‍😸")

    # ESCキーが押されるまでループ
    while not keyboard.is_pressed('esc'):
        search_on_Display()
        
    print("⛔[Debug]:Process/main_停止しました。")

if __name__ == "__main__":
    main()    