class solution:
    def jump(self, l):
        max_i = 0
        for i, n in enumerate(l):
            if max_i >= i and i + n > max_i:
                max_i = i + n  # 更新最远能到达的位置

        return max_i > i








nums = [2, 3, 1, 1, 4]

s = solution.jump(solution, nums)
print(s)

