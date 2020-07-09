class Mock:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


if __name__ == "__main__":
    mock = Mock(**dict(a="1", b=3, c=None))
    print(mock)
    print(mock.a)
    print(mock.b)
    print(mock.c)
