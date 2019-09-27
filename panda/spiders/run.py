# -*- coding: utf-8 -*-
import os
from time import sleep


def main():
    while True:
        os.system('run.bat')
        print("等待开始")
        for i in range(10):
            sleep(60)
            print("第{}分钟".format(i + 1))
        print("等待结束")


if __name__ == '__main__':
    main()
