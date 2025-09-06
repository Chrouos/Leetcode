from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        
        # 建立圖層
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
            
        
        def dfs(start, end, visited, acc):
            # 如果找不到路徑
            if start not in graph or end not in graph:
                return -1.0

            # 如果到達終點
            if start == end: return acc

            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited, acc * value)
                    if result != -1.0:
                        return result
            visited.remove(start)
            return -1.0

        results = []
        for a, b in queries:
            visited = set()
            results.append(dfs(a, b, visited, 1.0))
        return results


if __name__ == "__main__":
    s = Solution()
    question_list = [
        {"input": [[["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]], "output": [6.00000,0.50000,-1.00000,1.00000,-1.00000]},
        {"input": [[["a","b"],["b","c"],["bc","cd"]], [2.0,3.0,4.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]], "output": [6.00000,0.50000,-1.00000,1.00000,-1.00000]}
    ]

    for question in question_list:
        input_data = question["input"]
        expected_output = question["output"]

        output = s.calcEquation(*input_data)
        print(f"[{output == question['output']}] input: {question['input']}, output: {output}, expected: {question['output']}")