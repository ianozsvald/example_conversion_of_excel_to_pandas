Example of converting an Excel XLS sheet via Pandas, outputting a XLSX (to show writer capabilities). We'll include some string handling to show Python's additional power over simpler string tools in Python.

This is a demo to give a first steer to someone trying this conversion.

Follow:
* `demo_load_show_sheet.py` - loads `sheet_1_with_simple_logic.xls` and prints some details (to show how a script does this)
* `Demo Load and Show Sheet as Notebook.ipynb` - Jupyter Notebook to load `sheet_1_with_simple_logic.xls` and show some more info (to show how we can prototype code using Notebooks)
* `Load and Manipulate Sheet by Adding Logic.ipynb` - Notebook to load `sheet_1_without_simple_logic.xls` that *lacks* logic, we add the logic with Pandas, we use `fuzzywuzzy` for fuzzy string matching (to go beyond the simple Excel string logic`, then write out `sheet_1_with_added_logic_generated_via_pandas.xlsx`
