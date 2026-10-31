import math

def check_math_results(user_eq1, user_eq2, user_eq3):
        
    # Compute the exact reference values based on the prompt's inputs (a=101, b=7, c=12.34)
    expected_1 = 151.844
    expected_2 = -504162.451
    expected_3 = 1112.146

    passed = True

    try:
        assert abs(user_eq1 - expected_1) < 0.01, f"Equation 1 mismatch. Expected ~{expected_1}, got {user_eq1}"
        print("Equation 1: Correct!")
    except AssertionError as e:
        print(f"Equation 1: {e}")
        passed = False

    try:
        assert abs(user_eq2 - expected_2) < 0.1, f"Equation 2 mismatch. Expected ~{expected_2}, got {user_eq2}"
        print("Equation 2: Correct!")
    except AssertionError as e:
        print(f"Equation 2: {e}")
        passed = False

    try:
        assert abs(user_eq3 - expected_3) < 0.1, f"Equation 3 mismatch. Expected ~{expected_3}, got {user_eq3}"
        print("Equation 3: Correct!")
    except AssertionError as e:
        print(f"Equation 3: {e}")
        passed = False

    if passed:
        print("\nAll checks passed! You're ready to f-string formatting.")
    else:
        print("\nMake sure to re-run your script so the new values are calcuated before running the check again!")
    return


import sys
import io

def check_formatting(main_func):
    print("\nChecking String formatting with expected results:\n")
    """Step 2: Executes main() and validates exact print labels and f-string rounding."""
    new_out = io.StringIO()
    old_out = sys.stdout
    sys.stdout = new_out
    
    try:
        main_func()
        captured_output = new_out.getvalue()
    except Exception as e:
        sys.stdout = old_out
        print(f"Your code raised an error when executing main(): {e}")
        return False
    finally:
        sys.stdout = old_out
        
    exp1, exp2, exp3 = 151.844, -504162.451, 1112.146
    expected_lines = [
        f"equation 1: {exp1:.3f}",
        f"equation 2: {exp2:.3f}",
        f"equation 3: {exp3:.3f}"
    ]
    
    student_lines = [line.strip() for line in captured_output.strip().split('\n') if line.strip()]
    
    passed = True
    if len(student_lines) < 3:
        print(f"Expected 3 print output lines, but got {len(student_lines)}. Make sure you print all three equations inside main().")
        print("\nMake sure to re-run your script so the new values are calcuated before running the check again!")

        return

    for i, (student_line, expected_line) in enumerate(zip(student_lines, expected_lines), start=1):
        if student_line == expected_line:
            print(f"Equation {i} Output: '{student_line}' (Correct!)\n")
        else:
            print(f"Equation {i} Output:\n   Got:      '{student_line}'\n   Expected: '{expected_line}'\n")
            passed = False

    if passed:
        print("\nPrint formatting matches the sample output perfectly! Ready for Gradescope.")
    else:
        print("\nMake sure to re-run your script so the new values are calcuated before running the check again!")
    return