def search(x, seq):
    for i in range(seq):
        if x <= seq[i]:
            return i
        else:
            continue
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """

