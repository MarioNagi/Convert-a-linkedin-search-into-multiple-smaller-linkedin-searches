import pandas as pd

def url_seperator(url:str):
    delim = '%2Cfilters%3AList'
    prefix_index = url.find(delim)+len(delim)
    prefix = url[:prefix_index]
    #print('prefix:\n',prefix)
    delim = '%2C(type%3AREGION'
    suffix_index = url.find(delim)
    suffix = url[suffix_index:]
    content = url [prefix_index:suffix_index]
    #print('content:\n',content)
    #print('suffix:\n',suffix)
    start = content.find('List((') +len('List(')
    end =  content.find(')))')
    items = content[start:end]
    elements = items.split('))%2C')
    
    for i in range(len(elements)):
        elements[i]+='))'
    #print('\n\n\n',elements)

    #print(len(elements))
    with open('output.csv','a') as f:
        for i in range(len(elements)):
            f.write(f'{i},{prefix}{content[:start]}{elements[i]}{content[end+2:]}{suffix}\n')


fname = input('input the excel file name containing the links: ')
df = pd.read_excel(fname,header=None,names=['link'])
for index in df.index:
    url_seperator(df['link'][index])

#url = f.read()

#url_seperator(url)
    