def isMatch(s: str, p: str) -> bool:
    if not s:
        if not p:
            return True
        elif len(p) > 1 and p[1] == '*':
            return isMatch(s, p[2:])
        else:
            return False

    if s and not p:
        return False

    if p[0] == '.' or s[0] == p[0]:
        if len(p) > 1 and p[1] == '*':
            return isMatch(s[1:], p) or isMatch(s[1:], p[2:]) or isMatch(s, p[2:])
        else:
            return isMatch(s[1:], p[1:])
    elif len(p) > 1 and p[1] == '*':
        return isMatch(s, p[2:])
    else:
        return False

isMatch("bbbba", ".*a*a")