"""
Hash Tables
-----------

What problem are we solving with this data structure?

Quick O(1) searches!


[ "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
   0        1        2        3      4       5              6             7

Hashing function:

f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("dolor") -> 2
f("consectetur") -> 5
f("beej") -> 5


Hash table: key-value store with a particular structure, and O(1) time complexity
Python dict: basically is a hash table
General "Dictionary" equivalent to a "key-value store"
Key-value store is a data structure that returns a value for a given key

"""
a = ['Alice', 'Bob', 'Charlie', 'Diane']

for name in a:  # o(n) over the number of names
    if name == 'Lisa':
        print("Yes, it is!")
        break
################################################

table1 = [None] * 8
table = [None] * 8192


def hashf(str):
    """Super-naive hashing function--do not use."""
    b = str.encode()

    total = 0
    for i in b:  # O(n) over the size of the key, O(1) over the size of the hash table
        total += i
    return total


def get_index(key):
    index_value = hashf(key)
    index_value %= len(table)

    return index_value


def put(key, value):  # O(1) over the size of the hash table
    # Which slot (aka index) in the table is the value going?
    index = get_index(key)
    # Store the value at that slot
    table[index] = value


def get(key):
    index = get_index(key)
    return table[index]


def delete(key):
    index = get_index(key)

    table[index] = None


print(get("Beej"))
print(hashf("beej"))
print(table1)
print(table1)
# print(table)
put("Beej", 3490)
# put("eBej", "foo")  # Collision! This would be bad. We'll fix tomorrow.
print(get("Beej"))  # 3490

delete("Beej")
print(get("Beej"))  # None

# print(table)

##### Load factor notes

"""
Loading
-------

"How 'full' is the hash table?"


0 |-> D -> M -> Q
1 |-> H -> R -> X -> Y
2 |-> A -> I -> 0
3 |-> C -> J -> L -> N -> Z
4 |-> G -> S -> U
5 |-> B -> O -> 1 -> 2
6 |-> E -> K -> P -> W
7 |-> F -> T -> V

load_factor = number_of_items / number_of_slots_in_array

load_factor = 29 / 8 = 3.625
load_factor = 29 / 256 = 0.113

When the load factor > 0.7, it's time to increase the number of slots
When the load factor < 0.2, it's time to decrease the number of slots (down to some minimum)

"Rehashing"
-----------

Make a new array of double the size
Go through all the elements in the old hash table
Insert them into the new array
"""


#####  rehash pseudocode
def rehash():
    new_table = [None] * (len(table) * 2)
    # pseudocode
    """
    for each slot in table:
        for each element in the linked list in that slot:
            PUT that element in new_table
    """


##### application notes

"""
The General Problem Hash Tables Solve
-------------------------------------

Good at O(1) lookups

If we have something we want to look up quickly, we can use a hash table

Especially true if the thing isn't normally quick to look up.

Can we do this expensive, time-consuming process one time, save the result, and then
just look it up?

Identify the time-consuming process.

The n in O(n)
-------------

Do we *need* to optimize this?

Linear search:
    if n is < 10:
        who cares what search you use?

    if n < 10000000000:
        now we might need to care

    if n < 100000000000000000000000000000000000000000000000:
        now we really need to care


Other applications of hash tables
---------------------------------

Apply to any time-consuming process

* Calculations
* Network access
* Indexing data

Counting and removing duplicates

"""


# Count the number of occurrences of a letter in a string
# "Hello there!"

def letter_count(s):
    d = {}

    for c in s:

        if c.isspace():
            continue

        c = c.upper()

        if c not in d:
            # d[c] = 0
            d[c] = 1
        else:
            d[c] += 1

    return d


print(letter_count("Hello there!"))
