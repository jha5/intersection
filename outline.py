# Assumptions
# 1. Input array in in order of rectangles position on x-axis

# input_arr = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]
# input_arr = [(1,10,4),(1,8,6),(1,6,8)]
input_arr = [(0, 6, 2), (5, 10, 8), (7, 8, 12)]

input_arr = sorted(input_arr, key=lambda x: (x[0], x[1]))
# print(sorted(input_arr, key=lambda x: (x[0], x[1])))


def main(input_arr):
    # intialise temporary variables
    starting_point = None
    previous_point = None
    next_point = None
    last_point = None
    output = list()

    # loop through all rectangle coordinates
    for x1, x2, h in input_arr:
       

        if not starting_point:
            starting_point = [x1, h]
            output.append(starting_point)
            # print("adding starting point")
        if not previous_point:
            previous_point = (x1, x2, h)
            # print("Setting previous point")
        else:
            if x1 < previous_point[1] and x2 > previous_point[1] and h < previous_point[2]:
                # this means this rectangle is overlapping with previous rectangle
                # and is smaller in height
                # and is longer than the previous rectangle
                # print("smaller in height and longer")
                x_intersection = previous_point[1]
                y_intersection = h
                output.append([previous_point[1], h])
                # print("setting last point")
                last_point = [x2, 0]

            if x1 < previous_point[1] and x2 < previous_point[1] and h < previous_point[2]:
                # this means this rectangle is overlapping with previous rectangle
                # and is smaller in height
                # and is shorter than the previous rectangle
                # print("smaller in height and shorter")
                x_intersection = previous_point[1]
                y_intersection = h
                output.append([previous_point[1], h])
                last_point = None

            if x1 < previous_point[1] and x2 > previous_point[1] and h > previous_point[2]:
                # this means this rectangle is overlapping with previous rectangle
                # and is taller in height.
                # print("taller in height")
                x_intersection = x1
                y_intersection = previous_point[2]
                output.append([x1, h])
                last_point = None

            if x1 > previous_point[1]:
                # this means the rectangle is not overlapping
                # print("not overlapping")
                x_intersection = previous_point[1]
                y_intersection = 0
                output.append([x_intersection, y_intersection])
                output.append([x1, h])
                last_point = None

            if x1 > previous_point[0] and x2 < previous_point[1] and h > previous_point[2]:
                # print("within previous rectangle")
                output.append([x1, h])
                output.append([x2, previous_point[2]])
                output.append([previous_point[1], 0])
                last_point = None

        previous_point = [x1, x2, h]
        # print(output)
        # print("="*80)

    # since last coordinate will always end at 0
    if last_point:
        # print(f"Appending the last point left {last_point}")
        output.append(last_point)
    output[-1][-1] = 0
    # print("*"*80)
    # print(output)
    return output


print(main(input_arr))