"""
Slot
Index Chain (linked list)
----- -------------------------------
 0    ['qux',10] -> None
 1    ['plugh',20] -> ['foo',12] -> None
 2    ['xyzzy',50] -> ['baz',999] -> ['bar',30] -> None
 3    -> None

put("foo", 12)   # hashes to 1
put("bar", 30)   # hashes to 2
put("baz", 999 ) # hashes to 2--collision with "bar"!
put("qux", 10)   # hashes to 0
put("plugh", 20) # hashes to 1 (collision!)
put("xyzzy", 50) # hashes to 2 (collision!)

get("bar")  # Should give us 30 from index 2

Algorithm GET:
    Get the index for the key
    Search the linked list at that index for the entry for that key
    Return the value (or None if not found)

Algorithm PUT:
    Get the index for the key
    Search the list for the key
    If it exists, overwrite the value
    Else, insert the [key,value] at the head of the linked list at that slot

Algorithm DELETE:
    Left as an exercise!


put("foo", 12)   # hashes to 1
put("foo", 88)   # hashes to 1

Above lines equivalent to the following in a Python dict:

d = {}
d['foo'] = 12
d['foo'] = 88
"""

# How full does a hash table have to get before a collision happens?

import hashlib
import random


def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff


def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.8f}% full)")


how_many_before_collision(1000000000000, 10)
