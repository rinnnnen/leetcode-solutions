class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = ""
        for chars in zip(*strs): # зип группирует символы всех строк по индексам (как в списке)
            if len(set(chars)) == 1: # если все символы на этой позиции одинаковы
                prefix += chars[0] # добавляет в префикс
            else:
                break # если нашел различие - брейк
        return prefix
