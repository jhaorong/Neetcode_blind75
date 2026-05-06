# Neetcode blind75 刷題記錄
| 日期 | 題型 | 題目名稱 | 解題思路 | TC | SC |
|------|------|----------|----------|----|----|
| 2026-04-28 | Bit Manipulation | Number of 1 Bits | n & 1 檢查 LSB + 右移逐位處理 | O(1) | O(1) |
| 2026-04-28 | Bit Manipulation | Counting Bits | dp[i]=dp[i>>1]+(i&1) 遞推 | O(n) | O(n) |
| 2026-04-28 | Bit Manipulation | Reverse Bits | bit-by-bit 或 mask 分治交換 | O(1) | O(1) |
| 2026-05-05 | Bit Manipulation | Missing Number | 兩個相同數做bitwise xor為0的特性解題 | O(n) | O(1) |
| 2026-05-05 | Bit Manipulation | Sum of Two Integers  | 利用 XOR 表示不含進位的加總，AND 左移表示進位，反覆更新直到收斂 | O(1) | O(1) |
| 2026-05-05 | Arrays & Hashing | Contains Duplicate  | 透過一次遍歷逐步建立已出現元素的集合，在過程中即時檢查是否有重複出現的值 | O(n) | O(n) |
| 2026-05-06 | Arrays & Hashing | Valid Anagram | 使用hash紀錄每個字出現的頻率，在比較兩個hash是否相等 | O(n) | O(1) 因為最多出現26個字母 |
| 2026-05-06 | Arrays & Hashing | Two Sum | 在單次遍歷中利用hash map記錄已出現的數字，並即時檢查當前元素的互補數是否已存在 | O(n) | O(n) |
| 2026-05-06 | Arrays & Hashing | Group Anagrams | 將每個字串轉換為字母出現頻率的序列，再序列化成字串作為hash key，以此將具有相同字母頻率分布(anagram)的字串分組 | O(m * n) | O(m) 額外空間，O(m * n)儲存輸出，其中m為字串數量，n為最常字串長度 |