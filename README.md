# Neetcode blind75 刷題記錄
| 日期 | 題型 | 題目名稱 | 解題思路 | TC | SC |
|------|------|----------|----------|----|----|
| 2026-04-28 | Bit Manipulation | Number of 1 Bits | n & 1 檢查 LSB + 右移逐位處理 | O(1) | O(1) |
| 2026-04-28 | Bit Manipulation | Counting Bits | dp[i]=dp[i>>1]+(i&1) 遞推 | O(n) | O(n) |
| 2026-04-28 | Bit Manipulation | Reverse Bits | bit-by-bit 或 mask 分治交換 | O(1) | O(1) |
| 2026-05-05 | Bit Manipulation | Missing Number | 兩個相同數做bitwise xor為0的特性解題 | O(n) | O(1) |
| 2026-05-05 | Bit Manipulation | Sum of Two Integers  | 利用 XOR 表示不含進位的加總，AND 左移表示進位，反覆更新直到收斂 | O(1) | O(1) |
| 2026-05-05 | Arrays & Hashing | Contains Duplicate  | 透過一次遍歷逐步建立已出現元素的集合，在過程中即時檢查是否有重複出現的值 | O(n) | O(n) |