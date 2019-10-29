import itertools

class method2(object):
    def __init__(self,nums):
        self.nums = nums
    def get_combs(self,index):
        self.index = index
        self.combs = itertools.permutations(self.index)
        all_combs = []
        for i in self.combs:
            l = list()
            for c in i:
                l.append(self.nums[c])
            all_combs.append(l)
        self.combs = all_combs
    def make_set(self):
        a = []
        b = []
        for e in self.combs:
            a = [e[0],e[1]]
            b = [e[2],e[3]]
            self.check(a,b)
    def check(self,a,b):
        ops = ['+','-','*','**','/']
        first = []
        second = []
        for o in ops:
            try:
                first.append(eval("{}{}{}".format(a[0],o,a[1])))
                second.append(eval("{}{}{}".format(b[0], o, b[1])))
            except Exception as ex:
                pass
        final = 0
        for val in second:
            final = abs(24-val)
            if final in first:
                print(str(val)+ '+' + str(final))
        for val in second:
            try:
                final = 24/val
            except Exception as ex:
                pass
            if final in first:
                print(str(val) + '*' + str(final))

    def make_3_set(self):
        c = []
        d = 0
        for z in self.combs:
            c = [z[0], z[1], z[2]]
            d = z[3]
            self.check_threes(c,d)
    def check_threes(self,c,d):
        ops = ['+', '-', '*', '**', '/']
        ops2 = ['+', '-', '*', '**', '/']
        first = d
        second = []
        for e in ops:
            for q in ops2:
                try:
                    second.append(eval("{}{}{}{}{}".format(c[0],e,c[1],q,c[2])))
                except Exception as ex:
                    pass
            final = 0
            for val in second:
                final = abs(24 - val)
                if final == first:
                    print(str(val) + '+' + str(final))
            for val in second:
                try:
                    final = 24 / val
                except Exception as ex:
                    pass
                if final == first:
                    print(str(val) + '*' + str(final))

index = [0,1,2,3]
nums = [10,2,13,5]
b = method2(nums)
b.get_combs(index)
b.make_set()
b.make_3_set()


