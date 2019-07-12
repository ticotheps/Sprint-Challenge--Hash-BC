#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        print(weights[i])
        hash_table_insert(ht, weights[i], limit-weights[i])
        
    for j in range(len(ht.storage)):
        print(ht.storage[j])
        # print(hash_table_retrieve(ht, ht.storage[j]))
        
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

ht = HashTable(16)
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
# print(ht.storage)