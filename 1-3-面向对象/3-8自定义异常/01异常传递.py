import time

try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        print('意外终止')
    finally:
        f.close()
        print('关闭文件')
except:
    print('文件不存在')

