def remove_extras(lst):
    lst.reverse()
    for elem in lst:
        while elem in lst[lst.index(elem)+1:]:
            lst.remove(elem)
            #print(lst)
    lst.reverse()
    return lst
            
