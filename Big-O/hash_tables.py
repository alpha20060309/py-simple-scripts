### HASH SETS ##################################################
s : set = set()
print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in the set - O(1)

if 1 in s:
    print(True)

# Remove item in the set - O(1)
s.remove(3)

print(s)

# Set construction - O(S) - S is the length og the string
string = "aaaaaaaaabbbbbbbbbbbbccccccccccceeeeeeeeeeee"

unique_string: set = set(string)

print(unique_string)

# Loop over items in set - O(n)
for x in s:
    print(x)

#### HASH MAPS - DICTIONARIES #################################################

d : dict ={"Komol" : 18, "Dilbek": 19, "Ramz": 20}

print(d)

# Add key: val in dictionary: O(1)

d["Sherzod"] = 30

print(d)

# Check for presence of key in dictionary: O(1)

if 'Sherzod' not in d:
    print(True) 

# Check value corresponding to a key  in the dictionary: O(1)
print(d['Komol'])

# Loop over the key:val pairs of the dictionary : O(n)
for key,val in d.items():
    print(f"key {key}: val {val}")

# Defaultdict

from collections import defaultdict

default : dict = defaultdict(list)

print(default[2])
print(default[3])
print(default)

# Counter

from collections import Counter

print(string)

counter = Counter(string)

print(counter)