# rubiks_solver.py
# Requires: pip install kociemba   (optional; script will tell you if missing)
# Usage: python rubiks_solver.py
# Example usage shown at bottom of this file.

try:
    import kociemba
    HAVE_KOCIEMBA = True
except Exception:
    HAVE_KOCIEMBA = False

def solve_with_kociemba(state_54):
    """
    Solve a 3x3 cube using kociemba package.
    state_54: 54-character string, faces in order:
      U (9) R (9) F (9) D (9) L (9) B (9)
    Each character is a letter representing facelet color:
      Use U, R, F, D, L, B to label facelet stickers by face (recommended).
    Returns: a move sequence string (e.g. "R U R' U'").
    """
    if not HAVE_KOCIEMBA:
        raise RuntimeError("kociemba not installed")
    # kociemba expects exactly 54 chars
    if not isinstance(state_54, str) or len(state_54) != 54:
        raise ValueError("state_54 must be a 54-character string (U,R,F,D,L,B letters)")
    return kociemba.solve(state_54)

def explain_format():
    msg = """
kociemba state format (54 chars):
  The faces must be concatenated in this order:
    U (9 facelets), R (9), F (9), D (9), L (9), B (9)

  Typical convention: use the face letter for each sticker's color.
  Example for a solved cube:
    UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB

  How to read your cube into the string:
    - For each face (U,R,F,D,L,B), read the 9 stickers row by row (top-left to bottom-right).
    - Concatenate faces in the exact order above.

  After you form the 54-char string, call:
    solve_with_kociemba(your_string)
"""
    print(msg)

def main_example():
    if not HAVE_KOCIEMBA:
        print("kociemba package not found.")
        print("Install it with:\n    pip install kociemba\n")
        print("See explanation of the 54-character format below:")
        explain_format()
        # show solved-cube example
        solved = "U"*9 + "R"*9 + "F"*9 + "D"*9 + "L"*9 + "B"*9
        print("Solved-cube example string (54 chars):")
        print(solved)
        print("\nIf you install kociemba and run again, this program will solve your cube.")
        return

    # Example: solved cube
    solved = "U"*9 + "R"*9 + "F"*9 + "D"*9 + "L"*9 + "B"*9
    print("Example solved-cube string (54 chars):")
    print(solved)
    print("Solving solved cube ->", solve_with_kociemba(solved))

    # Example: a sample scramble state (here we show how you would call it).
    # NOTE: Replace the following example with the 54-char string for your actual cube.
    example_scramble_state = solved  # replace with your 54-char state
    if example_scramble_state != solved:
        print("Solving provided scramble...")
        print(solve_with_kociemba(example_scramble_state))

if __name__ == "__main__":
    main_example()
