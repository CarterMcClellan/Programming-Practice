def sum_digits(n: int) -> int:
    digs = list(str(n))
    digs = list(map(int, digs))
    return sum(digs)

def digit_prefix(n: int) -> str:
    as_s = str(n)
    if len(as_s) == 1:
        return ""
    return as_s[:-1]

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_cnt = {}
        prev_digit_sum, prev_digit_prefix = 0, ""
        for i in range(1, n+1):
            curr_prefix = digit_prefix(i)
            # Optimization: think about all the computations
            # we are making in the naive implementation.
            # (summing over all the digits). the only thing
            # actually changing is the very last digit, meaning
            # that most of the time we should be able to reuse the
            # sum we have already computed!
            if curr_prefix == prev_digit_prefix:
                idx = prev_digit_sum + 1
            else:
                idx = sum_digits(i)

            group_cnt[idx] = group_cnt.get(idx, 0) + 1
            prev_digit_sum, prev_digit_prefix = idx, curr_prefix
        
        cnts = list(group_cnt.values())
        max_cnt = max(cnts)
        ans = list(filter(lambda x: x == max_cnt, cnts))
        return len(ans)