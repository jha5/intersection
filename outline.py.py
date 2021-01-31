# Assumptions
# 1. Input array in in order of rectangles position on x-axis

# input_arr = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]
# output_arr = [(1, 10), (5, 8), (6, 0), (10, 10), (15, 0)]

# input_arr = [(1,10,4),(1,8,6),(1,6,8)]
# output_arr = [(1,8),(6,6),(8,4),(10,0)]

# input_arr = [(0, 6, 2), (5, 10, 8), (7, 8, 12)]
# output_arr = [(0,2),(5,8),(7,12),(8,8),(10,0)]

input_arr = [(1, 2, 8), (3, 6, 4), (3, 6, 10), (4, 7, 6), (5, 8, 12)]
output_arr = [[1, 8], [2, 0], [3, 10], [5, 12], [8, 0]]

input_arr = sorted(input_arr, key=lambda x: (x[0], -x[2]))
# print(sorted(input_arr, key=lambda x: (x[0], -x[2])), "sorted")


def cleanup(input_arr):
    # remove rectangles which is overlapping and is lower in height.
    final_arr = input_arr[:]
    x_long = None
    gap = 0
    for k in range(0, len(final_arr)):
        overlap_left = False
        overlap_right = False
        for x in range(0, len(final_arr)):
            if k == x or final_arr[x] is None or final_arr[k] is None:
                # skip
                continue

            # checks for rectangle with overlapping x-axis or y-axis
            if final_arr[k][0] >= final_arr[x][0] and final_arr[k][1] >= final_arr[x][1] and final_arr[k][2] <= final_arr[x][2]:
                # this means overlap is on left side
                # print("overlap left")
                overlap_left = final_arr[x]

            if final_arr[k][0] <= final_arr[x][0] and final_arr[k][1] <= final_arr[x][1] and final_arr[k][2] <= final_arr[x][2]:
                # this means overlap is on right side
                # print("overlap right")
                overlap_right = final_arr[x]

            # check for rectangle with equal width on x-axis
            if final_arr[x][0] <= final_arr[k][0] and final_arr[x][1] >= final_arr[k][1]:
                # print("YAY", final_arr[x], final_arr[k])
                if final_arr[x][2] >= final_arr[k][2]:
                    # print(f"removed {final_arr[k]}")
                    final_arr[k] = None


            # print(k, x)
        if overlap_left and overlap_right:
            # print("CHECKING OVERLAP", overlap_left, overlap_right)
            if overlap_left[1] >= overlap_right[0]:
                # this means the boxes are overlapping making the k hidden
                # print("OVERLAP BETWEEN", k, final_arr[k], "by", overlap_left, overlap_right)
                final_arr[k] = None
    # print("*"*80)
    final_arr = [x for x in final_arr if x is not None]
    return final_arr


def main(input_arr):
    # intialise temporary variables
    starting_point = None
    previous_point = None
    next_point = None
    last_point = None
    output = list()

    # loop through all rectangle coordinates
    for x1, x2, h in input_arr:
        # print(x1, x2, h)

        if not starting_point:
            starting_point = [x1, h]
            output.append(starting_point)
            # print("adding starting point")
        if not previous_point:
            previous_point = (x1, x2, h)
            # print("Setting previous point")
        else:
            if x1 == previous_point[0] and x2 == previous_point[1] and h < previous_point[2]:
                # this means the rectangle is exactly overlapping with the previous rectangle
                # and is smaller in height
                # skip this iteration without setting previous point.
                # print("skipping this iteration")
                # print("="*80)
                continue
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
                last_point = [x2, 0]

            if x1 > previous_point[1]:
                # this means the rectangle is not overlapping
                # print("not overlapping")
                x_intersection = previous_point[1]
                y_intersection = 0
                output.append([x_intersection, y_intersection])
                output.append([x1, h])
                last_point = [x2, 0]

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


main(cleanup(input_arr))
# cleanup(input_arr)
# print(input_arr)
print(output_arr)
