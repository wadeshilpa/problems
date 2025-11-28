# You're given a list of (category, points) pairs. A student may pick up to three books, but no two can be from the same category. 
# The goal is to choose the combination that yields the highest total points.

# [("Math", 10), ("Science", 8), ("History", 7), ("Math", 6)]
# Best choice: Math(10) + Science(8) + History(7) = 25

# [("Fiction", 5), ("Fiction", 9), ("Art", 4)]
# Best choice: Fiction(9) + Art(4) = 13
#######################################################################################

# Rearrange the digits of a number to form the largest possible odd number. 
# You may use all digits, but the final number must end with an odd digit.
# Input: 54831 → Output: 85431
# Input: 7204 → No odd digit → No valid odd number
# Input: 1324 -> Output 4321

#######################################################################################

# Extract the digits from a number and form the smallest possible non-negative odd number using those odd digits. 
# If no odd digit exists, return none.
# Input: 32491 → Odd digits: 3, 9, 1 → Smallest odd number: 139
# Input: -3 → Odd digit: 3 → Output: 3
# Input: -2 → No odd digits → Output: none

#######################################################################################

# Rearrange the digits of a given integer (positive or negative) to create the smallest possible value, while ensuring no leading zeros. 
# For negative numbers, you still reorder digits, but aim for the most negative result.

# Input: 310 → Digits: 0,1,3 → Minimum valid: 103
# Input: 9070 → Minimum valid: 7009
# Input: -431 →  -431

#######################################################################################

# Construct a number using only the odd digits from a given integer or string, and return the smallest non-negative number that can be formed. 
# Digits must be used in sorted order, and if no odd digit exists, return 0 or indicate no valid number.

# Input: 57241 → Odd digits: 5,7,1 → Smallest number: 157
# Input: 8086 → No odd digits → 0
# Input: "93152" → Odd digits: 9,3,1,5 → Smallest: 1359

#######################################################################################

# You're given a dictionary where each key is a location and each value is a list of cities visited there. 
# Return the city name that occurs most frequently across all lists.

# Input: {"US": ["NYC", "LA"], "EU": ["Paris", "NYC"]}   Output: "NYC"
# Input: {"A": ["Tokyo"], "B": ["Delhi", "Tokyo"], "C": ["Delhi"]}       Delhi / Tokyo

#######################################################################################

# You’re given a dictionary where each bookstore location maps to a list of review strings. 
# First remove duplicate reviews within each location, then find the review that appears most often across all locations.

# Input:  {"NY": ["Good", "Good", "Nice"], "LA": ["Nice", "Great", "Nice"]}       Output: "Nice"
# Input:  {"A": ["Ok"], "B": ["Ok", "Ok"], "C": ["Bad"]}          Output: "Ok"

#######################################################################################

# You’re given a dictionary where each key is a book and each value is a list of review strings. 
# Your task is to find the review that appears most often across all books.

# Input:{"a": ["bal", "bla"], "b": ["bla", "tla", "dla"], "c": ["bla", "tra", "ura"]}       Output: "bla"
# Input:{"X": ["good"], "Y": ["good", "ok"], "Z": ["ok"]}           Output: "good"

#######################################################################################

# Find the customer comment that appears most often across all bookstore locations, but treat repeated comments within the same location as one. 
# If several comments tie for the top spot, returning any of them is acceptable.

# {"NY": ["Good", "Good", "Nice"], "LA": ["Nice", "Great", "Nice"]}. → Nice
# {"A": ["Ok"], "B": ["Ok", "Ok"], "C": ["Bad"]}.  → Ok

#######################################################################################

# You’re given a list of workshops, each tagged with the year it was held. 
# Find the maximum total number of workshops hosted across any two consecutive years, considering only year pairs where both years had at least one workshop.

# Input: [(2020), (2020), (2021), (2022), (2022), (2022)]
# Pairs → 2020–2021 = 3, 2021–2022 = 4 → Output: 4

# Input: [2018, 2020, 2020, 2021]
# Pairs → 2020–2021 = 3 → Output: 3

#######################################################################################

# Determine if a binary tree is a full binary tree, meaning each internal node must have exactly two children, and leaf nodes have none.

#######################################################################################

# Given an unsorted list of numbers, determine whether a target value exists in the list by scanning each element until a match is found.
# Input: list = [7, 3, 9, 1], target = 9          Output: True
# Input: list = [4, 8, 2], target = 5             Output: False

#######################################################################################

# Find all elements that appear in exactly one of the two lists — not in both. 
# These are the values unique to each list when compared to the other.

# List1 = [1, 2, 3]
# List2 = [3, 4, 5]
# Uncommon → [1, 2, 4, 5]

# List1 = ["a", "b"]
# List2 = ["b", "c", "d"]
# Uncommon → ["a", "c", "d"]

#######################################################################################

# Reformat a dictionary by joining each key with its value list into a single string using a consistent pattern.

# Input: {"A": ["x", "y"], "B": ["p"]}                    Output format: "A-x,y", "B-p"
# Input: {"item": ["red", "blue"], "code": ["123"]}       Output: "item-red,blue", "code-123"

#######################################################################################

# Given a dictionary with two keys whose values are lists, generate all possible pairwise concatenations between the elements of the first list and the second list.

# Input: {"A": ["x", "y"], "B": ["1", "2"]}           Output: ["x1", "x2", "y1", "y2"]
# Input: {"L1": ["ab"], "L2": ["p", "q"]}             Output: ["abp", "abq"]

#######################################################################################

# Compute the average price of a book given a list of individual book prices.
# Input: [10, 20, 30]             Average → (10 + 20 + 30) / 3 = 20
# Input: [5.5, 7.5]               Average → 6.5

#######################################################################################

# Find how many different books you can buy with a fixed budget, given a list of book prices. Each book can be purchased only once, so choose the cheapest books first to maximize the total count.

# Prices: [4, 2, 6, 1]    Budget: 7           Buy: 1, 2, 4 → 3 books
# Prices: [10, 5, 8]      Budget: 9           Buy: 5 → 1 book

#######################################################################################

# Given a list of book or movie titles, identify which ones are sequels—titles that clearly reference a previous installment (e.g., by containing additional words or numbering while sharing the same base title).

# Input: ["GOT", "Troy", "Batman", "Batman Returns"]          Output: ["Batman Returns"]
# Input: ["Dune", "Dune Messiah", "Halo", "Halo 2"]           Output: ["Dune Messiah", "Halo 2"]

#######################################################################################

# Given a list of lists, calculate the average number of elements per list.

# Input:[[1, 2, 3], [10], [5, 6]]
# Lengths → 3, 1, 2       Average → (3 + 1 + 2) / 3 = 2       Output:2

#######################################################################################

# Given a collection of sorted lists, write a function that uses binary search to determine whether a target value exists in each list.
# Return a list of booleans indicating the result for every list.

# Input:  Lists = [[1, 4, 6], [2, 3, 9, 12], []]      Target = 3
# Output: [False, True, False]

#######################################################################################

# Array
# String 
# Dictionary 
# Tuple
# Sets 
# Hashmap 
# Heap
# stratrascratch 
