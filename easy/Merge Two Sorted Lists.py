class Solution(object):
    def mergeTwoLists(self, list1, list2):
        vals = [] # создаем пустой список, чтобы два связных списка сделать в обычные
        for l in (list1, list2): # запускаем цикл для *выше*
            while l: # работает до тех л...
                vals.append(l.val) # берет число из узла(л.вал) и добавляет в массив валс
                l = l.next # как и + 1, тока для связных циклов
        vals.sort() # сортировка
        dummy = ListNode() # создает пустой узел, чтобы прикреплять новые отсортированные числа
        curr = dummy
        for v in vals: # цикл для массива валс
            curr.next = ListNode(v) # новый узел для связного списка с в внутри и прикрепляем через некст
            curr = curr.next #передвигает
        return dummy.next # дамми-некст идет как цепочка узлов
