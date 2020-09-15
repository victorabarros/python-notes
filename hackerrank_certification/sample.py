def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split(" ")
    response = ""
    for word in reversed(words):
        wordSwap = ""
        for char in word:
            if char.islower():
                wordSwap += char.upper()
            else:
                wordSwap += char.lower()

        wordSwap += " "
        response += wordSwap

    print(response[:-1])

def mostBalancedPartition(parent, files_size):
    # Write your code here
    branches = []
    for ii in range(1, len(parent) - 1):
        branches.append([ii, parent[ii]])
    
    lowerOption = sum(files_size)
    choiced = []
    for dire, dad in branches:
        sideU, sideD = 0, 0
        for ii in range(1, len(parent) - 1):
            if parent[ii] <= dad and ii != dire:
                sideU += files_size[ii]
            else:
                sideD += files_size[ii]
        load = abs(sideU - sideD)
        choiced = [dire, dad]

        print(choiced, load)

        if load < lowerOption:
            lowerOption = load
            choiced = [dire, dad]

    return lowerOption

if __name__ == "__main__":
    # reverse_words_order_and_swap_cases("A b")
    # reverse_words_order_and_swap_cases("aWESOME is cODING")

    r = mostBalancedPartition([-1, 0, 1, 2], [1, 4, 3, 4])
    print(r)
