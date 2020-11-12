s = "How are you doing today?"

for c in sorted(set(s)):
    print(f"{c} occurs {s.count(c)} times")
