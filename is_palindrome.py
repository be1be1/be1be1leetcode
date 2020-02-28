def isPalindrome(Node head):
	if head is None or head.next is None:
		return True
	
	Node tmp = head
	# We use python list to perform the stack.
	# List has function pop() which pops the last element.
	stack = []
	while tmp is not None:
		stack.append(tmp)
		tmp = tmp.next
	while len(stack) != 0:
		Node t = stack.pop()
		if t.value != head.value:
			return False
		head = head.next
		
	return True
	
	
def isPalindromeAfterK(Node head, k:int):
	Node cur = head
	cnt = 0
	while cur is not None:
		cnt += 1
		cur = cur.next
	if k == 1:
		head = head.next
		return isPalindrome(head)
	if k > 1:
		cur = head
		while k != 1:
			k -= 1
			cur = cur.next
		cur.next = cur.next.next
	return isPalindrome(head)
	
