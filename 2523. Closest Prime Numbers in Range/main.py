
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        # Sieve of Eratosthenes
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 和 1 不是質數

            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:  # 如果 i 是質數
                    for j in range(i * i, n + 1, i):  # 把 i 的倍數都標記為合數
                        is_prime[j] = False

            return is_prime
        
        # 取得範圍內的所有質數
        is_prime = sieve(right)
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        if len(primes) < 2: return [-1, -1]
        
        min_diff = float('inf') # num_2 - num_1
        ans = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]

        return ans
        
        
if __name__ == "__main__":
    
    s = Solution()
    question_list = [
        {"input": [10, 19], "output": [11, 13]},
        {"input": [4, 6], "output": [-1, -1]},
        {"input": [19, 31], "output": [29, 31]},
    ]
    
    for question in question_list:
        output = s.closestPrimes(question['input'][0], question['input'][1])
        print(f"[{question['output'] == output}], input: {question['input']}, output: {output}")