def mystery(n) :
        if n <= 0 :
                return 0
        else:
                return mystery(n // 2) + 1
print("Mystery(20) is:", mystery(20))
