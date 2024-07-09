from collections import deque

# stack
stk = [1, 2, 3, 4]

stk.append(5)
print(stk)

stk.pop()
print(stk)

# queue
qu = ['가', '나', '다', '라']
qu.append('마')
print(qu)

qu.pop(0)
print(qu)

queue = deque(['a', 'b', 'c', 'd'])
queue.append('e')
print(queue)

queue.popleft()
print(queue)

# 튜플(tuple)
t1 = (10, 20, 30)
print(t1)

for i in t1:
    print(i)

t2 = ("가", )
print(t2)
print(type(t2))

t3 = ("가")
print(t3)
print(type(t3))

# set(집합)
s1 = {1, 2, 2, 3, 3, 3}
print(s1)

s2 = set(s1)
print(s2)

s1.add(4)
print(s1)

s1.remove(1)
print(s1)



