class Solution:
    def frequencySort(self, s: str) -> str:
        alpha = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        for i in s:
            if i in alpha:
                alpha[i] = alpha[i] + 1
            else:
                alpha[i] = 1
        alpha = dict(sorted(alpha.items(), key=lambda item: item[1], reverse = True))
        final = str()
        for i in alpha:
            final+=alpha[i]*i
        return final