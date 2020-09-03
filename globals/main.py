
A = 1
C = {'A': A}


def f1(**kwargs):
    for k, v in globals().items():
        if k[0] != "_":
            print(kwargs.get("msg", ""), "\t", k, v)
    f2()


def f2(msg=""):
    c, d = 3, 4

    for k, v in globals().items():
        if k[0] != "_":
            print(msg, "\t", k, v)


class E:
    def m1(self, msg=""):
        for k, v in globals().items():
            if k[0] != "_":
                print(msg, "\t", k, v)


if __name__ == "__main__":
    f1(a=1, b=2, msg="f1()")
    f2("f2()")
    e = E()

    globals()['f2']("globals()[\'f2\']")
    e.m1("e.m1")
    globals()['e'].m1("globals()[\'e\'].m1")
