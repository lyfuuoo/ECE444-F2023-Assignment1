class utils:
    def reversed(num):
        if isinstance(num, int):
            reversed_num = 0
            num_pos = True
            if num < 0:
                num_pos = False
                num = -num

            while(num>0):
                a = num % 10
                reversed_num = reversed_num*10 + a
                num = num // 10
            
            if num_pos != True:
                reversed_num = -reversed_num
            return reversed_num
        else:
            raise TypeError

    def formatter(num):
        if isinstance(num, int):
            binary = bin(num)
            octal = oct(num)
            return "{},{}".format(binary, octal)
        else:
            raise TypeError
