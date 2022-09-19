def sortList(self, head):
    #연결리스트->파이썬 리스트
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next
    #정렬    
    lst.sort()
    #파이썬 리스트->연결리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next
    return head