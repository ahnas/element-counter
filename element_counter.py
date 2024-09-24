from collections import Counter

def element_counter(sequence):
    return dict(Counter(sequence))

## Example

print(element_counter('elementCounter'))
print(element_counter([1,2,3,1,1,4,1,2,3,2,4,2,2]))