# class Solution:
#     def trap(self, height: List[int]) -> int:
#         i = 0 
#         j = 1
#         running_sum = 0
#         max_area = 0
#         total_area = 0
#         curr_max = 0
#         max_index = j
#         while i<j and j<len(height):
#             breadth = j - i - 1
#             length = min(height[i], height[j])
#             area = length * breadth 
#             print(height[i], height[j])
#             print("running_sum", running_sum, "area", area)
#             if j-i>1:
#                 running_sum = sum(height[i+1:j])
#             if height[j] >= curr_max:
#                 curr_max = height[j]
#                 max_index = j
#             print("total_area", total_area)
#             if height[j] >= height[i]:
#                 if area > 0:
#                     print("running_sum 2", running_sum, "area", area)
#                     total_area = total_area + area - running_sum
#                     running_sum = 0
#                     area = 0
#                 curr_max = 0
#                 i = j
#                 j += 1
#             else:
#                 while i<max_index and max_index<len(height):
#                     if j == len(height)-1:
#                         breadth = max_index - i - 1
#                         length = min(height[i], curr_max)
#                         area = length * breadth 
#                         if max_index-i>1:
#                             left_over_sum = sum(height[i+1:max_index])
#                             total_area = total_area + area - left_over_sum
#                         curr_max = 0
#                         i = max_index
#                 j += 1
#         return total_area


# copied solution, need to revisit again.
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 3:
            return 0

        i = 0
        total_area = 0

        while i < n - 1:
            j = i + 1

            # Best right boundary candidate if we never find height[j] >= height[i]
            max_index = j
            curr_max = height[j] if j < n else 0

            found_equal_or_taller = False

            # Scan right side from current left wall i
            while j < n:
                # Keep latest tallest right wall candidate
                # >= is important because for equal heights, later index is better
                if height[j] >= curr_max:
                    curr_max = height[j]
                    max_index = j

                # Case 1: found a right wall tall enough to close immediately
                if height[j] >= height[i]:
                    right = j
                    found_equal_or_taller = True
                    break

                j += 1

            # Case 2: no taller/equal right wall found
            # Use best smaller right wall seen so far
            if not found_equal_or_taller:
                right = max_index

            # Calculate trapped water between i and right
            breadth = right - i - 1

            if breadth > 0:
                boundary_height = min(height[i], height[right])
                middle_sum = sum(height[i + 1:right])
                water = boundary_height * breadth - middle_sum

                if water > 0:
                    total_area += water

            # Move left boundary to the right boundary we just used
            i = right

        return total_area
            
