import time

def main():
    while(True):
        try:
            print('Loop processing')
            print('Use ctrl+c to break')
            time.sleep(100)
        except KeyboardInterrupt:
            print('User interrupted the loop...exiting...')
            break


if __name__=='__main__':
        main()
