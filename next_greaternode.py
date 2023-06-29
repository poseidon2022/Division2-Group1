class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = list()
        my_stack = list()
        dummy = head
        count = 0
        while dummy!=None:
            answer.append(0)
            dummy = dummy.next
        while head!=None:
            while my_stack and my_stack[-1][0]<head.val:
                answer[my_stack[-1][1]] = head.val
                my_stack.pop()
            my_stack.append((head.val,count))
            count+=1
            head = head.next
        return answer