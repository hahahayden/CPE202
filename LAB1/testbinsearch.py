def bin_search(target, low, high, list_val):
    list_val = list_val[low:high+1]
    if (len(list_val) == 0):
        return None

    elif (target not in list_val):
        return None

    average = ((high-low)//2)  # average is mid
    averageNum = list_val[average]

    if (averageNum < target):
        # list_val=list_val[split it]
        return (bin_search(target, averageNum+1, high, list_val))
    elif(averageNum > target):

        return (bin_search(target, low, average-1, list_val))
    elif(averageNum == target):
        return list_val.index(averageNum)


print(bin_search(16, 1, 8, [0, 2, 10, 15, 16, 19, 20, 25, 30]))


def bin_search(target, low, high, list_val):
    list_val2 = list_val[low:high+1]

    if (len(list_val) == 0):
        return None

    elif (target not in list_val):
        return None

    average = (high-low)//2    # average is mid
    averageNum = list_val[average]

    if (averageNum < target):
        # list_val=list_val[split it]
        return (bin_search(target, average+1, high, list_val))
    elif(averageNum > target):

        return (bin_search(target, low, average-1, list_val))
    elif(averageNum == target):
        return average


#Lemar's Version


def bin_search(target, low,high, list_val):
    if(len(list_val)==0):
        return None
    mid_idx=(high+low)//2
    if(low>high):
        return None
    if target==list_val[mid_idx]:
        return mid_idx
    if target<list_val[mid_idx]:
        high=mid_idx-1
        return bin_search(target,low,high,list_val)
    else:
        low=mid_idx+1
        return bin_search(target, low,high, list_val)