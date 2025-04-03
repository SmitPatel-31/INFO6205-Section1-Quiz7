from typing import List

class MSDSortBasic:
    """ 
    Basic implementation of MSD (Most Significant Digit) sorting for strings.
    """
    
    R = 256  

    def __init__(self):
        """Initialize a new MSDSortBasic instance."""
        self.accesses = 0  # Track character accesses
    
    def _char_at(self, s: str, d: int) -> int:
        """Return the ASCII value of character at position d or -1 if out of bounds."""
        self.accesses += 1
        return ord(s[d]) if d < len(s) else -1
    
    def sort_by_position(self, arr: List[str], d: int) -> None:
        """
        Sorts the array of strings based on the character at position d.
        
        Args:
            arr: List of strings to be sorted
            d: Character position (0-indexed)
        """
        n = len(arr)
        if n <= 1:
            return
        
        R = self.R + 2 
        count = [0] * R
        aux = [None] * n  # Auxiliary array
        
      
        for s in arr:
            char_index = self._char_at(s, d) + 2  # +2 to account for -1 case
            count[char_index] += 1

        for r in range(1, R):
            count[r] += count[r - 1]

        for s in arr:
            char_index = self._char_at(s, d) + 1  # +1 for correct position
            aux[count[char_index]] = s
            count[char_index] += 1

        for i in range(n):
            arr[i] = aux[i]

    def is_sorted_by_position(self, arr: List[str], d: int) -> bool:
        """Check if the array is sorted by the character at position d."""
        for i in range(1, len(arr)):
            if self._char_at(arr[i], d) < self._char_at(arr[i-1], d):
                return False
        return True
