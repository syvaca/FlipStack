from collections import deque
from utils import TextbookStack

def breadth_first_search(stack):
    visited_ = []
    queue_ = deque()
    visited_.append(stack)
    queue_.append((stack, []))

    while queue_:
        text_stack, seq = queue_.popleft()
        if text_stack.check_ordered():
            return seq
        for i in range(1, text_stack.num_books + 1):
            temp_seq = seq.copy() + [i]
            copy = text_stack.copy()
            copy.flip_stack(i)
            if copy not in visited_:
                visited_.append(copy)
                queue_.append((copy, temp_seq))
    return []


def depth_first_search(stack):
    visited_ = []
    queue_ = deque()
    queue_.appendleft((stack, []))

    while queue_:
        text_stack, seq = queue_.popleft()

        if text_stack.check_ordered():
            return seq
        if text_stack in visited_:
            continue
        visited_.append(text_stack)
        for i in range(1, text_stack.num_books + 1):
            temp_seq = seq.copy() + [i]
            copy = text_stack.copy()
            copy.flip_stack(i)
            queue_.appendleft((copy, temp_seq))
    return []
