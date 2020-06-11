from collections import deque  # queue

GRAPH = dict(
    you=["alice", "bob", "claire"],
    bob=["anuj", "peggy"],
    alice=["peggy"],
    claire=["thom", "jonny"],
    anuj=[],
    peggy=[],
    thom=[],
    jonny=[],
)


def find_seller(graph):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, "is mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    # Mango seller are how name finish with "m"
    return name[-1] == "m"


if __name__ == "__main__":
    find_seller(GRAPH)
