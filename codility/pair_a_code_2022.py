def solution(S):
    a_idx = ord('a')
    last_appear = [-1] * 26
    curr_matched = []
    curr_unmatched = []
    for i in range(len(S)):
        letter_idx = ord(S[i]) - a_idx
        if i > 0:
            unmatched = min(curr_unmatched[i-1], curr_matched[i-1]) + 1
            curr_unmatched.append(unmatched)
            if last_appear[letter_idx] >= 0:
                curr_matched.append(min(curr_matched[last_appear[letter_idx]], curr_unmatched[last_appear[letter_idx]] - 1))
            else:
                curr_matched.append(unmatched)
        else:
            curr_matched.append(1)
            curr_unmatched.append(1)
        last_appear[letter_idx] = i

    return min(curr_matched[-1], curr_unmatched[-1])


# print(solution('youaremysunshine')

