from concurrent.futures import ThreadPoolExecutor   
from googletrans import Translator                      # !pip install googletrans==3.1.0a0
import pandas as pd
import sys
import time


translator=Translator()

file_path =sys.argv[1]          # give file path

df=pd.read_excel(file_path)


translate_value = lambda x: translator.translate(x, target='en').text   # translates given text

def translate_column(column):
  translated_values = [translate_value(value) for value in column]      # translates whole column
  return translated_values

start = time.time()


new_df = df.fillna('Null')  

trans_headers = [translate_value(x) for x in new_df.columns] # translating headers
new_df.columns = trans_headers

chunks = [new_df[col].astype(str) for col in new_df.columns] # converting dtype for ease of translation

translated_df = pd.DataFrame()

with ThreadPoolExecutor(max_workers=2) as executor:   # parallel execution
  translated_columns = list(executor.map(translate_column,chunks))

for col, translated_column in zip(new_df.columns, translated_columns):
  new_df.loc[:,col] = translated_column                                 # updating columns

# print(new_df.head(3))
  
end =time.time()
print(f'Translation done in {end-start} secs')


# in commad line type
#python xl_translation.py <xl file path>