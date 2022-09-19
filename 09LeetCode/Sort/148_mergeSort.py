#mergeSort
#두 정렬 리스트 병합
def mergeTwoLists(self, l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2) #하나의 l1으로 정렬
    return l1 or l2 #l1이 None이면 l2반환


def sortList(self, head):
    if not (head and head.next):
        return head
    
    #Runner기법 => 연결List의 끝 몰라서 half:중앙의 이전, slow:중앙, fast:맨 끝
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None #연결리스트를 끊음
    
    #분할 재귀 호출
    l1 = self.sortList(head) #head~half로 쪼갬
    l2 = self.sortList(slow) #slow~fast로 쪼갬
    
    return self.mergeTwoLists(l1, l2)