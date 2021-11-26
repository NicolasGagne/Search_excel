'''
Main entry point for
'''

from search_excel import sexcel

import pandas as pd

def check_excel(excelList  ):
    #excelList = sexcel()
    excelList = 'excelfile.txt'

    l_excelFile = ()
    with open(excelList) as f:
        l_excelFile = f.readlines()
    print("start print")
    print(l_excelFile)
    keywords = ['Waters', 'waters', 'water', 'Water', 'High', 'high', 'flood', 'flooding', 'erosion' ]

    for file in l_excelFile:

        df = pd.read_excel(file.strip("\n"))
        for w in keywords:
            if w in df.to_string():
                print(file.strip("\n"))
                with open('result.txt', 'a') as f:
                    f.write(file.strip('\n'))
                    f.write('\n')
                break


if __name__ == '__main__':
    check_excel('excelfile.txt')