def is_match(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return (is_match(text, pattern[2:]) or
                (first_match and is_match(text[1:], pattern)))
    return first_match and is_match(text[1:], pattern[1:])
