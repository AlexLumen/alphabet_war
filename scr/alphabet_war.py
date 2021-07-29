def alphabet_war(string):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_side_value = []
    right_side_value = []

    for char in string:
        if char in list(left_side.keys()):
            for dict_elem in left_side.keys():
                if char == dict_elem:
                    left_side_value.append(left_side[dict_elem])
        elif char in list(right_side.keys()):
            for dict_elem in right_side.keys():
                if char == dict_elem:
                    right_side_value.append(right_side[dict_elem])

    if sum(left_side_value) == sum(right_side_value):
        return f'Let\'s fight again!'
    elif sum(left_side_value) > sum(right_side_value):
        return 'Left side wins!'
    else:
        return 'Right side wins'
