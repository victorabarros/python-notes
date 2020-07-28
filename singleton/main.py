# https://github.com/ramalho/python-patterns-examples/blob/master/Ramalho/singleton.py

class Ordinaria(object):
    """Apenas ma classe ordinária."""


class Singleton(object):
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *a, **k)
        return cls._inst


class Foo(Singleton):
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    f1 = Foo()
    for ii in [s1, s2, f1]:
        print(id(ii))

# TODO: read https://github.com/victorabarros/challenge-bravo/blob/master/app/helper/singleton.py
