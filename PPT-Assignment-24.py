#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer1:

def romanToInt(s):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)):
        if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i-1]]:
            # If the current symbol is greater than the previous one, subtract the previous value twice
            total += roman_to_int[s[i]] - 2 * roman_to_int[s[i-1]]
        else:
            total += roman_to_int[s[i]]

    return total

s = "III"
result = romanToInt(s)
print(result)


# In[2]:


s = "LVIII"
result = romanToInt(s)
print(result)


# In[3]:


#Answer2:

def lengthOfLongestSubstring(s):
    char_set = set()  # Set to store unique characters
    left = 0  # Left pointer
    max_length = 0  # Maximum length of substring without repeating characters

    for right in range(len(s)):
        while s[right] in char_set:
            # If the right character is already in the set, remove the left character from the set
            char_set.remove(s[left])
            left += 1

        # Add the right character to the set
        char_set.add(s[right])

        # Update the maximum length if necessary
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)


# In[4]:


s = "bbbbb"
result = lengthOfLongestSubstring(s)
print(result)


# In[5]:


s = "pwwkew"
result = lengthOfLongestSubstring(s)
print(result)


# In[6]:


#Answer 3:

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 2, 3]
result = majorityElement(nums)
print(result)


# In[8]:


nums = [2, 2, 1, 1, 1, 2, 2]
result = majorityElement(nums)
print(result)


# In[9]:


#Answer4:

def groupAnagrams(strs):
    anagram_dict = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    return list(anagram_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)


# In[10]:


strs = ["a"]
result = groupAnagrams(strs)
print(result)


# In[11]:


#Answer5:

def nthUglyNumber(n):
    ugly = [1]
    p2 = p3 = p5 = 0

    for _ in range(1, n):
        next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        ugly.append(next_ugly)

        if next_ugly == ugly[p2] * 2:
            p2 += 1
        if next_ugly == ugly[p3] * 3:
            p3 += 1
        if next_ugly == ugly[p5] * 5:
            p5 += 1

    return ugly[-1]


n = 10
result = nthUglyNumber(n)
print(result)


# In[12]:


n = 1
result = nthUglyNumber(n)
print(result)


# In[13]:


#Answer 6:

import heapq
from collections import Counter

def topKFrequent(words, k):
    count = Counter(words)  # Count the frequency of each word
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]


words = ["i","love","leetcode","i","love","coding"]
k = 2
result = topKFrequent(words, k)
print(result)


# In[14]:


words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
result = topKFrequent(words, k)
print(result)


# In[15]:


#Answer7:

from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove elements that are out of the current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove elements smaller than the current element from the right of the window
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add the current element's index to the window
        window.append(i)

        # If the window has reached its size, add the maximum element to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = maxSlidingWindow(nums, k)
print(result)


# In[16]:


nums = [1]
k = 1
result = maxSlidingWindow(nums, k)
print(result)


# In[17]:


#Answer8:

def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
result = findClosestElements(arr, k, x)
print(result)


# In[18]:


arr = [1, 2, 3, 4, 5]
k = 4
x = -1
result = findClosestElements(arr, k, x)
print(result)


# In[ ]:




