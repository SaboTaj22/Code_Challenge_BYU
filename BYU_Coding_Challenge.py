r = input()

def roman_int(r):
    dec_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0

    for i in range(len(r)):
        if i+1 != len(r) and dec_num[r[i]] < dec_num[r[i+1]]:
            ans = ans - dec_num[r[i]]
        else:
            ans = ans + dec_num[r[i]]
    return ans
print(roman_int(r))

def int_roman(x):
    rom_nu = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    int_num = [1, 5, 10, 50, 100, 500, 1000]





