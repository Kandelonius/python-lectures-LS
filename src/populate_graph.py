def reset(self):
    self.last_id = 0
    self.users = {}
    self.friendships = {}


def populate_graph(self, num_users, avg_friendships):
    """
    Takes a number of users and an average number of friendships
    as arguments

    Creates that number of users and a randomly distributed friendships
    between those users.

    The number of users must be greater than the average number of friendships.
    """
    # Reset graph
    self.reset()

    # Add users
    for i in range(num_users):
        self.add_user(f"User {i}")

    # Create friendships
    possible_friendships = []

    for user_id in self.users:
        for friend_id in range(user_id + 1, self.last_id + 1):
            possible_friendships.append((user_id, friend_id))

    random.shuffle(possible_friendships)

    for i in range(num_users * avg_friendships // 2):
        friendships = possible_friendships[i]
        self.add_friendship(friendships[0], friendships[1])