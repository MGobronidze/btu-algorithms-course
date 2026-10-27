# ფაქტორიალის გამოთვლა რექურსიული მეთოდით
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n უნდა იყოს არაუარყოფითი")
    if n <= 1:                      
        return 1
    return n * factorial(n - 1)    

# სიის ქვესიმრავლეობის შემოწმება
def is_subset(L1: list, L2: list) -> bool:
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

# სიების თანაკვეთის გამოთვლა
def intersect(L1: list, L2: list) -> list:
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):   # ეს შემოწმებაც თავად O(len(res))-ია!
            res.append(e)
    return res

# ბინარული ძებნა რეკურსიული მეთოდით
def binary_search_rec(arr: list, low: int,
                       high: int, target) -> int:
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, mid + 1, high, target)
    else:
        return binary_search_rec(arr, low, mid - 1, target)

# სიის ყველა ქვესიმრავლის გენერირება
def gen_subsets(items: list) -> list[list]:
    if len(items) == 0:
        return [[]]                        
    smaller = gen_subsets(items[:-1])        
    last = items[-1:]
    with_last = [s + last for s in smaller]  
    return smaller + with_last

# ფიბონაჩის იტერაციული მეთოდი
def fib_iter(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_i, fib_ii = 0, 1
    for _ in range(n - 1):
        fib_i, fib_ii = fib_ii, fib_i + fib_ii
    return fib_ii

#  რიცხვის სტრინგად გარდაქმნა
def int_to_str(i: int) -> str:
    digits = '0123456789'
    if i == 0:
        return '0'
    is_negative = i < 0
    i = abs(i)
    chars = []
    while i > 0:
        chars.append(digits[i % 10])
        i //= 10
    if is_negative:
        chars.append('-')
    return ''.join(reversed(chars))

# სწრაფი დალაგების ალგორითმი, ჰოარის დანაწილების სქემა
def hoare_partition(arr: list, low: int, high: int) -> int:
    pivot = arr[low]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j                
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort_hoare(arr: list, low: int, high: int) -> None:
    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pi)     
        quick_sort_hoare(arr, pi + 1, high)


# მატრიცაში ელემენტის ძებნა
def search_matrix(matrix: list, target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1      
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1              
        else:
            row += 1               
    return False

# ბმული სიები
# ბმული სიის კვანძის კლასის განსაზღვრა
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ბმული სიაში ელემენტის ძებნა
def search_linked_list(head: "Node", target) -> bool:
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return False

# ბმული სიაში ელემენტების რაოდენობის დათვლა
def find_length(head: "Node") -> int:
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
    return length


# ბმული სიაში ელემენტის ჩასმა კონკრეტულ პოზიციაზე
def insert_at_position(head: "Node", pos: int, data) -> "Node":
    if pos < 1:
        return head
    if pos == 1:
        new_node = Node(data)
        new_node.next = head
        return new_node

    prev = head
    count = 1
    while count < pos - 1 and prev is not None:
        prev = prev.next
        count += 1
    if prev is None:         
        return head

    new_node = Node(data)
    new_node.next = prev.next
    prev.next = new_node
    return head

# ბმული სიის კონკრეტული პოზიციიდან ელემენტის წაშლა
def delete_at_position(head: "Node", position: int) -> "Node":
    if head is None or position < 1:
        return head
    if position == 1:
        return head.next

    current = head
    for _ in range(position - 2):
        if current is not None:
            current = current.next
    if current is None or current.next is None:
        return head            

    current.next = current.next.next   
    return head

