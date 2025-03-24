from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Step 1: Sort meetings by start day
        meetings.sort()

        # Step 2: Merge overlapping meetings
        merged = []
        for start, end in meetings:
            if merged and merged[-1][1] >= start - 1:  
                merged[-1][1] = max(merged[-1][1], end)  # Merge intervals
            else:
                merged.append([start, end])  # Add new interval

        # Step 3: Count available days
        occupied_days = sum(end - start + 1 for start, end in merged)
        return days - occupied_days
