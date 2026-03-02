# Queue implemented with a singly linked list (head + tail pointers)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLLQueue:
    def __init__(self):
        self.head = None   # dequeue from head
        self.tail = None   # enqueue to tail -> ensures O(1) enqueue
        self.size = 0

    def enqueue(self, value):
        """Insert at tail in O(1)."""
        node = Node(value)
        if self.head is None:      # queue was empty
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        """
        Remove from head.
        Returns the removed value, or None if the queue is empty (underflow-safe).
        """
        if self.head is None:
            # Underflow-safe handling: return None (caller can detect)
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            # If queue becomes empty, ensure tail is cleared too
            self.tail = None
        self.size -= 1
        return val

    def front(self):
        """Peek at the front value without removing it. Returns None if empty."""
        return None if self.head is None else self.head.val

    def is_empty(self):
        return self.head is None

    def to_list(self):
        """Return queue contents from front->back as a Python list (for display)."""
        out = []
        cur = self.head
        while cur:
            out.append(cur.val)
            cur = cur.next
        return out

# Helper: process a sequence of operations (strings)
def process_operations(ops):
    """
    ops: list of strings. Allowed forms:
      "ENQ x" or "ENQUEUE x"  -> enqueue integer/string x
      "DEQ" or "DEQUEUE"     -> dequeue
      "FRONT"                -> optional (we use final front in returned result)
    Returns: (removed_values_list, current_front_or_None, final_state_list)
    - removed_values_list contains the values returned by each DEQ; if underflow happened, None is appended.
    """
    q = SLLQueue()
    removed = []
    for op in ops:
        parts = op.strip().split()
        if len(parts) == 0:
            continue
        cmd = parts[0].upper()
        if cmd in ("ENQ", "ENQUEUE"):
            if len(parts) < 2:
                raise ValueError(f"ENQ needs a value: '{op}'")
            # join remaining parts as the value (so values with spaces work)
            val = " ".join(parts[1:])
            # try to convert to int if it looks numeric
            if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
                val = int(val)
            q.enqueue(val)
        elif cmd in ("DEQ", "DEQUEUE"):
            removed_val = q.dequeue()
            removed.append(removed_val)
        elif cmd == "FRONT":
            # not removing; no change. We won't append anything, final front is returned later.
            pass
        else:
            raise ValueError(f"Unknown operation '{op}'")
    return removed, q.front(), q.to_list()

# Example usage & demonstration:
if __name__ == "__main__":
    ops = [
        "ENQ 10",
        "ENQ 20",
        "DEQ",
        "FRONT",
        "DEQ",
        "DEQ",        # underflow here
        "ENQ 30",
        "ENQ 40"
    ]
    removed, current_front, final_state = process_operations(ops)
    print("Operations:", ops)
    print("Removed values (in order):", removed)         # [10, 20, None]
    print("Current front:", current_front)              # 30
    print("Final queue state (front->back):", final_state)  # [30, 40]

    # Quick BFS demo using the same queue:
    def bfs(adj, start):
        q = SLLQueue()
        visited = set()
        order = []
        visited.add(start)
        q.enqueue(start)
        while not q.is_empty():
            v = q.dequeue()
            order.append(v)
            for nei in adj.get(v, []):
                if nei not in visited:
                    visited.add(nei)
                    q.enqueue(nei)
        return order

    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    print("BFS from node 2:", bfs(graph, 2))  # e.g. [2, 0, 3, 1]