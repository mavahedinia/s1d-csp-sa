class Case:
    def __init__(self, name, L, req, ans) -> None:
        self.name = name
        self.L = L
        self.req = req
        self.ans = ans


Debugger1 = Case("D1", 30, [13, 16, 24, 16, 11, 14], 4)
Debugger2 = Case("D2", 100, [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30], 4)
Debugger3 = Case("D3", 100, [16, 34, 49, 12, 43, 44, 34, 23, 33, 40, 55, 51], 5)
