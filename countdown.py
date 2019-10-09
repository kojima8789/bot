#! python3
# countdown.py

import time, subprocess

time_left = 5
while time_left > 0:
    print(time_left, end='')
    time.sleep(1)
    time_left = time_left - 1

#TODO カウントダウン後音声ファイルを再生する

subprocess.Popen(['open','alarm.wav'])