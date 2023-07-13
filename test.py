from time import sleep

erl = [None,"text"]
err = 1

def main():
    print('ee')
    sleep(12)
    print('oo')


try:
    main()
except:
    print("_error "+str(err))
    print(erl[1])