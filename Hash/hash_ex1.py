# initialize hash
hash_set = set()

# add a new key

hash_set.add(3)
hash_set.add(2)
hash_set.add(1)
print(hash_set)


hash_set.remove(2)
# check if the key is in the hash set
if 2 not in hash_set:
    print("Key 2 is not in the hash set.")
else:
    print("Key 2 is in the hash set.")
print(hash_set)

print('size of hash_set: ', len(hash_set))

# 5. get the size of the hash set
print("Size of hashset is:", len(hash_set))

# 6. iterate the hash set
for x in hash_set:
    print(x, end=" ")
print("are in the hash set.")

# 7. clear the hash set
hash_set.clear()
print("Size of hashset:", len(hash_set))
