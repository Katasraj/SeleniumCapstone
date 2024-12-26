import pandas as pd

def getCSVData(fileName):
    df = pd.read_csv(fileName)
    rows = []

    courseName = df['courseName'].values.tolist()
    for row in courseName:
        rows.extend(row)

    return rows


