#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # Step 1: Creates a hash table with 16 buckets
    ht = HashTable(16)
    # Step 2: Loop through each item in the 'weights' list
    for item in range(length):
        # weight of item
        weight = weights[item]
        # index of item
        item_index = item
        # difference between item's weight and the limit
        diff_from_limit = limit - weight
        
        # Step 3: Insert item's: weight as 'key', index as 'value
        hash_table_insert(ht, weight, item_index)
        print(f'{weight} was inserted successfully at index {item}')
        print(f'diff_from_limit of {weight} is: {diff_from_limit}')
        
        # Step 4: Search hash table for ANOTHER item whose 'key' is
        #         equal to the 'diff_from_limit' value of THIS item.
        print(diff_from_limit)
        if hash_table_retrieve(ht, diff_from_limit):
            print("YES")
        else:
            print("no")

    # {
    #     4: 0,
    #     6: 1,
    #     10: 2, 
    #     15: 3,
    #     16: 4
    # }
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


ht = HashTable(16)
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)