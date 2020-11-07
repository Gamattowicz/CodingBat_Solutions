''' Python 3.9
6.11.2020


We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks
(5 inches each). Return True if it is possible to make the goal
by choosing from the given bricks. This is a little harder than
it looks and can be done without any loops. See also:
Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True '''


def make_bricks(small, big, goal):
    for i in range(small + big+1):
        if goal >= 5 and big > 0:
            goal -= 5
            big -= 1
        elif goal >= 1 and small > 0:
            goal -= 1
            small -= 1
        elif goal == 0:
            return True
    return False


print(make_bricks(20, 4, 39))
