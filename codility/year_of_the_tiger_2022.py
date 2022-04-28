
def solution(T):
    a_idx = ord('a')
    color = [0] * (26 ** 3)
    result = 0
    for tower in T:
        idx = ord(tower[0]) * 676 + ord(tower[1]) * 26 + ord(tower[2]) - 703 * a_idx
        color[idx] += 1
        result = max(color[idx], result)
        if tower[1] != tower[2]:
            swap_top_idx = ord(tower[0]) * 676 + ord(tower[2]) * 26 + ord(tower[1]) - 703 * a_idx
            color[swap_top_idx] += 1
            result = max(color[swap_top_idx], result)
        if tower[0] != tower[1]:
            swap_bottom_idx = ord(tower[1]) * 676 + ord(tower[0]) * 26 + ord(tower[2]) - 703 * a_idx
            color[swap_bottom_idx] += 1
            result = max(color[swap_bottom_idx], result)

    return result

# print(solution(['aab', 'cab', 'baa', 'baa']))

