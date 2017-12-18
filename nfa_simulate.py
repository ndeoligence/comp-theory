edges = {(1, 'a'): [2, 3], (2, 'a'): [2], (3, 'b'): [4, 3], (4, 'c'): [5]}
accepting = [2, 5]
start_state = 1


def nfsmsim(string, current, edges, accepting):
    if len(string) == 0:
        return current in accepting
    else:
        node = (current, string[0])
        if node in edges:
            states = edges[node]
            return True in [nfsmsim(string[1:], state, edges, accepting) for state in states]
        else:
            return False


def main():
    assert nfsmsim("abc", 1, edges, accepting)
    assert nfsmsim("aaa", 1, edges, accepting)
    assert nfsmsim("abbbc", 1, edges, accepting)
    assert not nfsmsim("aabc", 1, edges, accepting)
    assert not nfsmsim("", 1, edges, accepting)


if __name__ == '__main__':
    main()
