#! python3
# stopwatch.py - シンプルなストップウォッチプログラム

import time

#プログラムの説明を表示する
print('Enterを押すと開始します。その後、Enterを押せば経過時間を表示します。Ctrl-Cで終了します。')
input()
print('スタート')
start_time = time.time()
last_time = start_time
lap_num = 1

#TODO ラップタイムを計測する

try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time,2)
        total_time = round(now - start_time,2)
        print('ラップ #{}:{} ({})'.format(lap_num,total_time,lap_time),end='')
        lap_num += 1
        last_time = now

except KeyboardInterrupt:
    #Ctrl-C例外を処理してエラーメッセージを表示しないようにする
    print('\n終了.')