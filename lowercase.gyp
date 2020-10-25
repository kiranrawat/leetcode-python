def toLowerCase(self, str):
    for c in str:
        if "A" <= c <= "Z":
            return "".join(chr(ord(c) + 32)
        else:
            return c  