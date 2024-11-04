
# loop over len(s) times
    # if s == goal - return true
    # else rotate the string one character
# if we reached here - return false
def rotateString1(s, goal):
    for index in len(s):
        if s == goal:
            return True

        # make one rotation
        else:
            part1 = s[0]
            part2 = s[1:]
            s = part2 + part1

    return False

# one liner :)
def rotateString2(s, goal):
    if len(s) != len(goal):
        return False
    return goal in s+s

#with functions - more readable than both
def rotateString3(s, goal):
    for i in range(len(s)):
        if rotate(s, i) == goal:
            return True

    return False



def rotate(s, rounds):
    return s[rounds:] + s[:rounds]

#some documentation