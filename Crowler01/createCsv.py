import pandas as pd

file = 'data/konkatsu.csv' #取得したいファイルのPATH
df = pd.read_csv(file, encoding = "utf-8") #encodingは案件によって変えてください

df.dropna(subset=['custamer'], inplace=True)#カスタマーがからの行を削除
print(df)
df['domain'] = df['url'].apply(lambda x: x.split('/')[2] if len(x.split('/')) > 2 else '')
print(df)
df.drop_duplicates(subset='domain', keep='first', inplace=True)
df.drop_duplicates(subset='domain', keep='first', inplace=True)


df.to_csv('data/outPut.csv', mode='a', header=False, index=False, encoding='utf-8')



