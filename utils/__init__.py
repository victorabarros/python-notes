def printDict(data: dict, prefix: str = ''):
    for k, v in data.items():
        if type(v) == dict:
            print(f"{prefix}{k}")
            printDict(v, f"{prefix}\t")
        else:
            print(f"{prefix}{k}\t{v}")


if __name__ == "__main__":
    # tests:
    printDict(dict(
        a=1,
        b=dict(
            c=None,
            d=dict(
                e=True
            )
        ),
        f=[1, 2, 3, dict(g=30.2)]
    ))
