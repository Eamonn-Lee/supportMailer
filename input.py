import pandas as pd

excel_clipboard = pd.read_clipboard(header=None)
excel_clipboard.to_csv('raw_data.txt', index=False, header=False, sep='\t')