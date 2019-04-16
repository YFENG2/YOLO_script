# -*- coding: utf-8 -*-
"""
script: 比如我们要对a.txt文件进行分割，按照(limit)行一分割，分割成多个txt文件。

"""
limit = 1
file_count = 1
url_list = []
file_path = 'nn.txt'
with open(file_path) as f :
    for line in f:
        url_list.append(line)
        if len(url_list)<limit:
            continue
        file_c= str(file_count).zfill(6)
        file_name = file_c+".txt"
        with open(file_name, 'w') as file:
            for url in url_list[:-1]:
                file.write(url)
            file.write(url_list[-1].strip())
            url_list=[]
            file_count+=1

if url_list:
    file_name = str(file_count)+".txt"
    with open(file_name, 'w') as file:
        for url in url_list:
            file.write(url)
print('done')
