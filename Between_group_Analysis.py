import pandas as pd

# Acquire count quality for each participant and separate into "G" and "B" dataframes
df = pd.read_csv("eeg-during-mental-arithmetic-tasks-1.0.0/subject-info.csv")
df_good = df[df["Count quality"] == 1]
df_bad = df[df["Count quality"] == 0]

print(f"Good Counter Group: {df_good.shape[0]} participants")
print(f"Bad Counter Group: {df_bad.shape[0]} participants")