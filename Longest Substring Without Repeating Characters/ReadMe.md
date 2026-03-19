# 📝 LeetCode #3: Longest Substring Without Repeating Characters

**Difficulty:** 🟡 Medium  
**Topics:** `Sliding Window`, `Hash Map`, `Two Pointers`, `String`

## 🎯 Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1:**
* **Input:** `s = "abcabcbb"`
* **Output:** `3`
* **Explanation:** The answer is "abc", with the length of 3.

## 💡 Algorithmic Approach: The Sliding Window
A brute-force approach (checking every possible substring) would result in a massive $O(N^3)$ time complexity, which is far too slow. 

Instead, this solution utilizes the **Sliding Window** technique combined with a Hash Map (Dictionary):
1. Use two pointers (`left` and `right`) to represent the boundaries of the current "window" (substring).
2. As the `right` pointer expands the window character by character, store the characters and their indices in a dictionary.
3. If a duplicate character is found inside the current window, instantly slide the `left` pointer to the right of the previous occurrence. 
4. Keep track of the maximum window size encountered during this single pass.

## ⏱️ Complexity Analysis
* **Time Complexity:** $O(N)$ 
  * We traverse the string exactly once with the `right` pointer. Dictionary lookups take $O(1)$ constant time.
* **Space Complexity:** $O(K)$ 
  * Where $K$ is the size of the character set (e.g., 26 for English letters, or up to 128 for ASCII). The dictionary will store at most $K$ elements.

## 🛠️ Python Implementation
*(Note: I prioritize readable variable names and clear state-tracking to ensure the logic is easy to follow during technical interviews).*

