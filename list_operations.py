
def sort_list(list):
    list.sort()


def search_by_value(list,value):
    if value in list:
        return True
    else:
        return False

def find_five_min_elem(list):
    min = list[0]
    lst = []
    for x in range(5):
        min = list[0]
        for x in list:
            if x < min:
                min = x
        lst.append(min)
        list.remove(min)
    return lst

def find_five_max_elem(list):
    max = list[0]
    lst = []
    for x in range(5):
        max = list[0]
        for x in list:
            if x > max:
                max = x
        lst.append(max)
        list.remove(max)
    return lst

def list_avg(list):
    # тут буде ексепшин якщо список порожній - ділення на 0, тому
    try:
        return sum(list) / len(list) # спробували поділити, якщо все ок то виконажється ретурн
    except ZeroDivisionError: # якщо при діленні отримали помилку ділення на 0 то повертаємо, наприклад нічого - None
        return None