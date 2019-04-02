# Name: Hayden Tam
# Professor: Professor Einakian
# CPE 202- 03
# Lab2

# Purpose: list all permutations for a given string
# Signature: string->list


def permutate(stringInput):

    if (len(stringInput) == 0):
        raise ValueError
    elif (len(stringInput) == 1):
        return stringInput
    else:

        listStrings = []
        for k in range(len(stringInput)):
            part = stringInput[:k] + stringInput[k+1:]

            for i in permutate(part):

                listStrings.append(stringInput[k:k+1] + i)

        return listStrings


'''


def string_permutation(stringInput):

    if not stringInput:
        return [stringInput]  # is an empty sequence
    else:
        temp = []
        for k in range(len(stringInput)):
            part = stringInput[:k] + stringInput[k+1:]
            # print k, part  # test
            for m in string_permutation(part):
                temp.append(stringInput[k:k+1] + m)
                # print m, seq[k:k+1], temp  # test
        print(temp)

'''
