T = int(input())

def remove_left_cube():
    stacked.append(leftcube)
    sideLengths.pop(0)


def remove_right_cube():
    stacked.append(rightcube)
    sideLengths.pop(-1)

for y in range(T):
    # print('y=' + str(y))
    number_of_cubes = int(input())
    sideLengths = str(input()).split()
    sideLengths = [int(i) for i in sideLengths]
    # print(sideLengths)
    stacked = []

    for n in range(number_of_cubes):
        # print('n=' + str(n))
        leftcube = sideLengths[0]
        rightcube = sideLengths[-1]
        if stacked == []:
            if leftcube >= rightcube:
                remove_left_cube()
            else:
                remove_right_cube()
        else:
            # print('left', leftcube) # 1
            # print('right', rightcube) # 3
            # print('last stacked', stacked[-1]) # 2
            last_stacked = stacked[-1]
            if leftcube > last_stacked and rightcube > last_stacked:
                # print('Fail')
                print('No')
            elif leftcube >= rightcube and leftcube <= last_stacked:
                # print('pick left')
                remove_left_cube()
                if not sideLengths:
                    print('Yes')
                    break
            elif leftcube < rightcube and rightcube <= last_stacked:
                # print('pick right')
                remove_right_cube()
                if not sideLengths:
                    print('Yes')
                    break
            elif leftcube < rightcube and leftcube <= last_stacked:
                # print('pick left')
                remove_left_cube()
                if not sideLengths:
                    print('Yes')
                    break
            # print(stacked)

# test cases 1, 2, 4 wrong