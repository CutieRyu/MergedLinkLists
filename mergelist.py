class List: 
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = List()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # If one of the lists is not empty, append the remaining elements
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def create_sorted_list_with_duplicates(values):
    dummy = List()
    current = dummy
    
    for value in values:
        current.next = List(value)
        current = current.next
    
    return dummy.next


list1 = create_sorted_list_with_duplicates([1,2, 4])
list2 = create_sorted_list_with_duplicates([1, 3, 4])


merged_list = merge_sorted_lists(list1, list2)

print("Merged List:")
while merged_list is not None:
    print(merged_list.value, end=" -> ")
    merged_list = merged_list.next