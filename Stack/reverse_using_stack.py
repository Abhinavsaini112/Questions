def reverse_using_another_stack(s1, s2):
    n = len(s1)
    if n == 0:  # Base case: If the stack is empty, return
        return

    # Step 1: Pop all elements from s1 and push them to s2
    for i in range(n):
        s2.append(s1.pop())

    # Step 2: Pop the top element from s2 (which was the bottom-most in s1)
    value = s2.pop()

    # Step 3: Push all elements back from s2 to s1
    for i in range(len(s2)):
        s1.append(s2.pop())

    # Step 4: Recursively call the function to reverse the remaining stack
    reverse_using_another_stack(s1, s2)

    # Step 5: Push the saved element back to s1 (placing it at the correct reversed position)
    s1.append(value)

# Example usage
s1, s2 = [7, 8, 30, 12], []
reverse_using_another_stack(s1, s2)
print(s1)  # Output: [12, 30, 8, 7]
