# SMART PANDAS COLUMN

Do you find it frustrating when exploring a new dataset that you make a spelling mistake when typing a column name and you have to go back to the code, fix it and rerun that block of code? 
Wouldn't it be better if the code could just be a bit smarter and understand that when you said "Column 1" you actually meant "Column1" and instead of breaking to .. <i>just run</i>?


<b>Smart Pandas Column</b> is a simple yet useful pandas extension that does exactly that.

## Installing
You can install this package straight from this repo

## Usage
Usage is very simple. Just wrap your dataframe with the <i>SmartColumnDataFrame</i> class and you are good to go.

```python 
import pandas as pd
import smart_pandas_column as spd

df = pd.DataFrame(columns=['Alpha','Beta'], data=[[1,2],[3,4]])
df = spd.SmartColumnDataFrame(df)
```

Alternatively, you can do the following

```python 
import smart_pandas_column as spd

df = spd.SmartColumnDataFrame(columns=['Alpha','Beta'], data=[[1,2],[3,4]])
```

Or even, if reading a dataset from a csv file

```python 
import smart_pandas_column as spd
file_location='path/to/your/file.csv'

df = spd.read_csv(file_location)
```

There is nothing more for you to do. Keep coding and don't worry about small spelling mistakes...

Given the above example dataframe, you can run 

```python 
df['gamma'] = df['alpha'] + df['beta']
```
and you will only see a warning regarding your spelling mistake without breaking your code


In might be the case that the default tolerance for errors is not fit for you. Don't worry, you can override the default allowed of wrong characters in a column name.
```python
from smart_pandas_column import SmartColumnDataFrame

SmartColumnDataFrame.maximum_allowed_wrong_characters = 5 # your preferred character limit

```