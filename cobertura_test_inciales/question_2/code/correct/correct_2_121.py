def unique_day(date, possible_birthdays):
    j = 0
    for i in possible_birthdays:
        if date == i[1]:
            j = j+1
        else:
            j = j
    if j == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    j = 0
    for i in possible_birthdays:
        if month == i[0]:
            j = j+1
        else:
            j = j
    if j == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    dayi = ()
    result = False
    for i in possible_birthdays:
        if month == i[0]:
            dayi += (i[1],)
    for j in dayi:
        result = result or unique_day(j, possible_birthdays)
    return result
        
            
        
