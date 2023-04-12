
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1, num2 = [], []

        digit = l1
        while digit:
            num1.append(digit.val)
            digit = digit.next
        to_sum_1 = int(''.join(map(str, num1))[::-1])

        digit = l2
        while digit:
            num2.append(digit.val)
            digit = digit.next
        to_sum_2 = int(''.join(map(str, num2))[::-1])

        summa = str(to_sum_1+to_sum_2)

        next_node = None
        for i in range(len(summa)):
            node = ListNode(val=int(summa[i]), next=next_node)
            next_node = node
        return next_node
    