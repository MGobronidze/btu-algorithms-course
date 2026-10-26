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

