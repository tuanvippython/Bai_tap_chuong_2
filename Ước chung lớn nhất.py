def UCLN(x,y):
    if x == 0:
        return y
    else:
        r = y % x
        return UCLN(r,x)

if __name__ == "__main__":
    print(UCLN(2,4))

