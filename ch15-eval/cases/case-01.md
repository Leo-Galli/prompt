# case-01

Expected label: HIGH

Issue note:
todocount crashes with a traceback when I pass an empty path: `todocount --ext .py ""`. No count is printed. Repro every time on Windows.
