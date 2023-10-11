class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def fast_modular_exponentiation(base, exponent):
            result = 1
            while exponent > 0:
                if exponent % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exponent //= 2
            return result
        
        even_count = fast_modular_exponentiation(5, (n + 1) // 2)  # Count of even digits
        odd_count = fast_modular_exponentiation(4, n // 2)  # Count of odd digits
        
        total_count = (even_count * odd_count) % MOD
        
        return total_count