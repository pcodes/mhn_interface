import operator


def get_frequency(list, key):
    total = {}
    for x in list:
        ip = x[key]
        if ip in total:
            total[ip] += 1
        else:
            total[ip] = 1
    return total


def get_top_5(list, key):
    total = get_frequency(list, key)
    top_5 = dict(sorted(iter(total.items()), key=operator.itemgetter(1), reverse=True)[:5])
    #print(top_5)
    #print(sorted(top_5, key=top_5.get, reverse=True))
    return sorted(top_5, key=top_5.get, reverse=True)

