# case-03

Expected label: MED

Issue note:
When a nested folder mixes `.py` and `.md` files, `todocount --ext .py ./src` under-counts TODO markers in deeper `.py` files. No crash. Counts look low compared to a manual search.
