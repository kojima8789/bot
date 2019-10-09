import threading,time
print('プログラム開始')

def take_a_nap():
    time.sleep(5)
    print('起きた')

thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('プログラム終了')