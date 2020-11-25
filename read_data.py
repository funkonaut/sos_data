import pandas as pd
from itertools import accumulate
import numpy as np
import meta_data


#Read im the file get rid of newlines
def read_data(fn):
    with open(fn,"r") as fh:
        data = fh.read()
    data = data.replace("\n","")
    return data


#Split into discrete records 560 characters record length
def split_fw(data,n=560):
    records = [data[i:i+n] for i in range(0, len(data), n)]
    return records


#Read sub fwf according to specified fw from layout_code 
def read_multi_fwf(records):
    #Read in that data
    dfs = []
    for record in records:
        #compute index
        layout_code = int(record[0:2])
        if layout_code == 99: continue#layout_code = 13
    
        #Split according to widths spec just makes it easier instead of typing in all start and end pos
        width = meta_data.WIDTHS[layout_code-1]
        bounds = list(accumulate(width, lambda a,b: a+b))
        col_widths = list(zip(bounds[0::1],bounds[1::1]))
        data_type = meta_data.DTYPES[layout_code-1]
       
        #Read all the entries according to fw
        entry = []
        for w,dt in zip(col_widths,data_type): 
            data = record[w[0]:w[1]]
            if dt == "C": data = data.rstrip()
           # else: data = float(data) #FIX THIS TO GET CLEANER ENTRIES...
           #     if data == 0: data = np.nan
            entry.append(data)
        d = dict(zip(meta_data.NAMES[layout_code-1],entry)) 
        #Build data frame for entry
        dfs.append(d)
    
    df = pd.DataFrame(dfs)
    return df

#TO DO: 
#Clean up "N" entries to display cleaner
#Link up df_meta and replace entries from each table as specified
if __name__ == "__main__":
    fn = "CW070106.txt"
    df = read_multi_fwf(split_fw(read_data(fn)))
    
