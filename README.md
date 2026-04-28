# Neetcode blind75 刷題記錄
| 日期 | 題型 | 題目名稱 | 解題思路 | TC | SC |
|------|------|----------|----------|----|----|
| 2026-04-28 | Bit Manipulation | Number of 1 Bits | n & 1 檢查 LSB + 右移逐位處理 | O(32)=O(1) | O(1) |
| 2026-04-28 | Bit Manipulation | Counting Bits | dp[i]=dp[i>>1]+(i&1) 遞推 | O(n) | O(n) |
| 2026-04-28 | Bit Manipulation | Reverse Bits | bit-by-bit 或 mask 分治交換 | O(1) | O(1) |