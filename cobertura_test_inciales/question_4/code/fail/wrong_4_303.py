def sort_age(lst):
    lst.sort(key=lambda x:x[1])
    lst.reverse()
    print(lst)
