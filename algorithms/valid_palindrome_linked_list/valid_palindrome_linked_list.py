def isPalindrome(self, head: 'ListNode') -> 'bool':
       vals = []
        while head:
            vals += [head.val]
            head = head.next
        return vals == vals[::-1]
