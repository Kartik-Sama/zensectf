rand_map = [47, 20, 77, 91, 7, 18, 55, 46, 17, 60, 27, 40, 85, 15, 11, 12, 92, 9, 76, 62, 16, 80, 44, 13, 10, 67, 86, 65, 89, 81, 68, 26, 6, 64, 54, 57, 25, 45, 1, 83, 38, 71, 36, 75, 33, 79, 29, 63, 50, 70, 90, 56, 51, 37, 61, 42, 39, 93, 66, 43, 0, 2, 53, 74, 5, 22, 69, 82, 3, 28, 30, 34, 23, 19, 31, 84, 24, 41, 59, 4, 52, 73, 8, 35, 88, 78, 14, 49, 58, 32, 21, 72, 87, 48]

res = "4=ZB=XR iH1US5ZCks1<kC_RkA}DkW1sjkP6_{_k2RkBy1{y_85Q"

l = [c for c in res]
for i in range(len(l)):
    print(pow(1,(ord(l[i]))),ord(l[i])%2,-1**0)
    l[i] = chr(ord(l[i])+pow(-1,ord(l[i])%2))
    print(i,l[i],ord(l[i]))
    l[i] = chr(rand_map.index((ord(l[i])-32))+32)
    print(i,l[i],ord(l[i]))

ans = ""
for i in l:
    ans = ans + str(i)

print(ans)