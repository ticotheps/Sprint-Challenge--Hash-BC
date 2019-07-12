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
        # Step 3a: If the item's weight does already exist as a key in 
        #          the hash table...
        if hash_table_retrieve(ht, weight):
            # Step 4: Retrieve the existing key.
            # Step 5: Hash
            print("The key does exist.")
            
        # Step 3b: If the item's weight does NOT already exist as a key in 
        #          the hash table...
        else:
            # Step 4: Insert item's: weight as 'key', index as 'value
            hash_table_insert(ht, weight, item_index)
            print(f'{weight} was inserted successfully at index {item}')
            print(f'diff_from_limit of {weight} is: {diff_from_limit}')
            # Step 5: Search hash table for ANOTHER item whose 'key' is
            #         equal to the 'diff_from_limit' value of THIS item.
            print(diff_from_limit)
            # Step 6: If the the 'diff_from_limit' value of this item exists
            #          as a key in the hash table...
            if hash_table_retrieve(ht, diff_from_limit):
                # Step 7a: ...Set that key's value to a new variable...
                value_of_matching_key = hash_table_retrieve(ht, diff_from_limit)
                print(f'YES; value of matching key is: {value_of_matching_key}')
                # Step 7b: ...and create a tuple 'answer' with item_index positioned
                #          in the ZEROITH index, followed by the value_of_matching_key.
                answer = (item_index, value_of_matching_key)
                print(f'\n***ANSWER***: {answer} \n')
                return answer
            # Step 8: If the the 'diff_from_limit' value of this item IS
            #         a key in the hash table...
            else:
                # Step 6b: ...print "not a match"
                answer = None
                print("not a match")
            
            
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
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")


# ht = HashTable(16)
print_answer(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))