def jumpingOnClouds(c):
    # Start at cloud 0
    # We can jump 1 or 2 clouds
    # We have to avoid the clouds labeled 1
    # We win the game by reaching the last cloud in the path
    # It's always possible to win the game

    # At any cloud, we have a choice
    # do we jump 1 cloud away, or do we jump 2 clounds away?
    # we can check if the cloud 1 step ahead is valid
    # we can check if the cloud 2 steps ahead is valid
    # sometimes we only have one choice since one of the choices
    # isn't an option because it's a thunderhead

    # We're trying to find the minimum number of jumps
    # isn't it always better to jump 2 clouds if we can?

    # Let's always try to jump 2 clouds away unless the cloud 2
    # steps away is a thunderhead
    # if it is a thunderhead, jump 1 cloud away

    # Once we reach the last cloud in the list, we've won

    # we need to keep track of where we are in the path
    # we're going to update this variable as we progress
    # through the path of clouds
    current = 0
    jumps = 0

    # 0 0 1 0 0 1 0

    # keep iterating until we've won the game
    # stop when `current` == the index of the last cloud
    while current < len(c) - 1:
        # check the cloud 2 spots away to see if we can jump there
        if current + 2 < len(c) and c[current + 2] == 0:
            current += 2
        else:
            current += 1

        jumps += 1

    return jumps
