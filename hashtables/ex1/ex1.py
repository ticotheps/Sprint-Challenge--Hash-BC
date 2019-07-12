#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    ht_length = len(ht.storage)

    for i in range(length):
        # print(weights[i])
        weight = weights[i]
        weight_list_index = i
        diff_from_limit = limit - weight
        
        hash_table_insert(ht, weight, weight_list_index)
        print("Insert was successful")
        print("diff_from_limit: ", diff_from_limit)
        
    print("weights: ", weights)
    
    for j in range(ht_length):
        if ht.storage[j] == None:
            pass
        else:
            print("pair: ", ht.storage[j])
            # print("value: ", hash_table_retrieve(ht, ht.storage[j].key))
            pass
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


ht = HashTable(16)
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
# print(ht.storage)