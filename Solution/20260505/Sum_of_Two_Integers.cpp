// method 1 Bit-by-Bit Binary Addition
class Solution {
public:
    int getSum(int a, int b) {
        int a_lsb, b_lsb;
        int carry_bit = 0;
        int sum = 0;
        for(int i=0;i<32;i++)
        {
            a_lsb = a & 1;
            b_lsb = b & 1;
            sum |= (a_lsb ^ b_lsb ^ carry_bit) << i;
            carry_bit = (a_lsb & b_lsb) | (b_lsb & carry_bit) | (a_lsb & carry_bit);
            a >>= 1;
            b >>= 1;
        }
        return sum;
    }
};

// method 2 Separate Sum and Carry Addition
class Solution {
public:
    int getSum(int a, int b) {
        int carry;
        while(b != 0)
        {
            carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
};