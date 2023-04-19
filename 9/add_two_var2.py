class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        
        carry = 0
        result = ListNode()
        current = result

        while(l1 or l2 or carry):
            current.next = ListNode()
            current = current.next
            num1 = l1.val if l1 else 0  # тернарный оператор
            num2 = l2.val if l2 else 0

            summa = num1 + num2 + carry
            val = summa % 10

            carry = summa // 10

            current.val = val


            if (l1) : l1 = l1.next
            if (l2) : l2 = l2.next

        return result.next