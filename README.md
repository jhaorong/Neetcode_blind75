# Neetcode blind75 刷題記錄
| 日期 | 題型 | 題目名稱 | 解題思路 | 時間複雜度 | 空間複雜度 |
|------|------|----------|----------|------|------|
| 2026-04-28 | Bit Manipulation | Number of 1 Bits | 使用bitwise AND(n & 1)檢查最低位bit是否為1，並透過將n右移1個bit，使下一個bit移動至LSB位置進行逐位檢查。
 | O(32) ≈ O(1)，因為 uint32_t 為固定長度。
 | O(1) |
| 2026-04-28 | Bit Manipulation | Counting Bits | 利用二進位特性，i的1-bit數量等於i/2(右移一位)去掉最低位後的結果，再加上i的最低位是否為1，因此可直接利用已計算的dp值遞推。
 | O(n)
 | O(n) for the output array |
 | 2026-04-28 | Bit Manipulation | Reverse Bits | 方法一：逐位反轉(Bit-by-bit)逐一讀取n的每個bit，並將其放到結果的對稱位置(第i位 → 第31-i位)，透過位移與OR操作重建反轉後的數值。
方法二：分治交換(Optimal)利用分治概念，透過bit mask將位元分組，並逐層交換區塊(16→8→4→2→1 bits)，最終在常數時間內完成整體bit反轉。
 | O(1)
 | O(1) |