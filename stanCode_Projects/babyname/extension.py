"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        targets = soup.find_all('tbody')
        male_total = 0
        female_total = 0

        for target in targets:
            num = target.text
            a = num.split()

            for i in range(2, 1002, 5):
                b=int(a[i].replace(',',""))
                male_total+= b
            print('Male Number: ', male_total)

            for j in range(4, 1004, 5):
                c=int(a[j].replace(',',""))
                female_total+= c
            print('Female Number: ', female_total)




if __name__ == '__main__':
    main()
