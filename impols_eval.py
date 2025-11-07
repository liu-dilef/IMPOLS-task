import pandas as pd
from sklearn.metrics import f1_score

fgold = "GOLD_FILE_PATH.csv" # gold annotation in the "tag" column
fpred = "PRED_FILE_PATH.csv" # predicted values in the "tag" column

dgold = pd.read_csv(fgold, sep='\t')
dpred = pd.read_csv(fpred, sep='\t')
F1 = f1_score(dgold['tag'],dpred['tag'], average='macro')
print("F1 score:",F1)
