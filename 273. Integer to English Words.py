class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d_0 = {0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
        d_10 = {11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"}
        d_100 = {10: "Ten",
                20: "Twenty",
                30: "Thirty",
                40: "Forty",
                50: "Fifty",
                60: "Sixty",
                70: "Seventy",
                80: "Eighty",
                90: "Ninety"}
        d_1000 = {1000: "Thousand",
                1000000: "Million",
                1000000000: "Billion"}
        def hundred(n):
            s = ''
            flag = False
            if n > 0:
                flag = True
            hundred = int(n / 100)
            if hundred != 0:
                s+=d_0[hundred]
                s+= ' '
                s += 'Hundred'
                s += ' '
            n = n % 100
            if n in d_100.keys():
                s += d_100[n]
                return s.strip()
            ten = int(n / 10)
            if ten == 1:
                s += d_10[n]
                return s.strip()
            elif ten != 0:
                print(ten)
                s += d_100[ten*10]
                s += ' '
                
            n = n % 10
            if n == 0 and flag:
                return s.strip()
            
            s += d_0[n]
            return s.strip()
        number = ''
        billion = int(num / 1000000000)
        if billion != 0:
            number = hundred(billion)
            number += ' '
            number += "Billion"
            num = num % 1000000000
            if num == 0:
                return number.strip()
            else:
                number += ' '
        million = int(num / 1000000)
        if million != 0:
            number += hundred(million)
            number += ' '
            number += "Million"
            num = num % 1000000
            if num == 0:
                return number.strip()
            else:
                number += ' '
        thousand = int(num / 1000)
        if thousand != 0:
            number += hundred(thousand)
            number += ' '
            number += "Thousand"
            num = num % 1000
            if num == 0:
                return number.strip()
            else:
                number += ' '
        
        number += hundred(num)
        return number.strip()
