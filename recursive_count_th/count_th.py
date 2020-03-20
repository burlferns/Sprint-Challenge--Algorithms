'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # TBC

    if len(word) <= 1:
        return 0

    if len(word) == 2:
        if word == "th":
            return 1
        else:
            return 0

    # if the length is > 2 the following runs
    if word[0:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])
