def search(x, seq):
    seq = list(seq)
    if seq == []: return 0
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
            else: continue
        return len(seq)
