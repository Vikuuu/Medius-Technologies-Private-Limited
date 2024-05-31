import pandas as pd


def process_file(file):
    if file.name.endswith(".xlsx"):
        data = pd.read_excel(file)
    else:
        data = pd.read_csv(file)
    summary = data.groupby(["Cust State", "DPD"]).size().reset_index(name="Count")
    return summary.to_html(index=False)
