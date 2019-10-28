class method_2(object):

    def __init__(self, nums):
        self.nums = nums

    def get_combs(self):

        combs = [
            [0, 3, 1, 2],
            [0, 2, 1, 3],
        ]

        all_combs = [self.nums]

        for c in combs:
            l = list()
            for i in c:
                l.append(self.nums[i])

            all_combs.append(l)

        print(all_combs)
        self.combs = all_combs

    def make_sets(self):

        for e in self.combs:
            a = [e[0], e[1]]
            b = [e[2], e[3]]

            self.check(a, b)

    def check(self, a, b):
        ops = ["+", "-", "*", "**", "/"]
        set1 = set()
        set2 = set()

        for o in ops:
            try:
                set1.add(eval("{}{}{}".format(a[0], o, a[1])))
                set2.add(eval("{}{}{}".format(b[0], o, b[1])))
            except Exception as ex:
                pass

        for first in set1:
            for second in set2:
                for o in ops:

                    try:
                        curr = eval("{}{}{}".format(first, o, second))
                    except Exception as ex:
                        # print (ex)
                        pass

                    if curr == 24:
                        print(curr, "{}{}{}".format(first, o, second))
nums = [13,4,9,2]
b = method_2(nums)
b.get_combs()
b.make_sets()