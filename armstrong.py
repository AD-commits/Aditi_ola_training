class Check:
    def __init__(self, number):
        self.num = number

    def isArmstrong(self):
        temp = self.num
        r = 0
        while(temp != 0):
            rem = temp % 10
            r += rem ** 3
            temp //= 10
        if self.num == r:
            print(self.num, "is Armstrong")
        else:
            print(self.num, "is not Armstrong")


obj = Check(153)
obj.isArmstrong()
