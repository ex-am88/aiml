
def minimax(level, max_turn):
    if level == 3:
        return values.pop(0)

    first = minimax(level + 1, not max_turn)
    second = minimax(level + 1, not max_turn)

    if max_turn:
        best = max(first, second)
        print("Level", level, "MAX:", first, second, "->", best)
    else:
        best = min(first, second)
        print("Level", level, "MIN:", first, second, "->", best)

    return best


values = [3, 5, 2, 9, 12, 5, 23, 23]

print("Game Tree:")
print("             MAX (Level 0)")
print("            /             \\")
print("       MIN (Level 1)    MIN (Level 1)")
print("        /       \\         /       \\")
print("     MAX       MAX      MAX       MAX")
print("     / \\       / \\      / \\       / \\")
print("    3   5     2   9    12   5     23  23")

print("\nWorking:")
answer = minimax(0, True)
print("\nFinal Best Value:", answer)
