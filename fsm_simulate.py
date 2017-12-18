edges = {
    (1, 'a'): 1,
    (1, 'b'): 2,
    (2, 'a'): 1,
    (2, 'b'): 3,
    (3, 'a'): 1,
    (3, 'b'): 3
}


def fsasim(string, transitions, start_state, final_states):
    """
    Checks if the given string is a word accepted by an FA defined by the given transitions
    :param string: the string to be checked for acceptance.
    :param transitions: an fsa definition
    :param start_state: the start state
    :param final_states: the final state
    :return: True iff the given string is a word in the FA
    """
    if len(string) == 0:
        return start_state in final_states
    else:
        try:
            return fsasim(string[1:], transitions, transitions[(start_state, string[0])], final_states)
        except KeyError:
            return False


def main():
    s = 'ababbaabbbbbab'
    assert fsasim(s + 'bb', edges, 1, [3])
    assert not fsasim(s + 'aa', edges, 1, [3])
    assert not fsasim(s + 'ab', edges, 1, [3])
    assert not fsasim(s + 'ba', edges, 1, [3])
    assert not fsasim('', edges, 1, [3])


if __name__ == '__main__':
    main()
