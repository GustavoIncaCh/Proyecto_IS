def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for index in range(len(seq)):
        if x<= seq[index]:
            return index
    return len(seq)
