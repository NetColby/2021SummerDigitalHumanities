# Ruize Li
# Jun 2, 2021
# converts html files to plain texts

# dependencies
from bs4 import BeautifulSoup
import os


# read file names in directory
def read(dir):
    f_names = []
    # list of files in data
    for item in os.listdir(dir):
        if not item.startswith('.') and os.path.isfile(os.path.join(dir, item)):
            f_names.append(item)
    return sorted(f_names)

# convert one html file to txt
def convert(dir, f_names, year):
    os.chdir(dir)
    # i = 0
    output = dir + f"/{year}.txt"
    with open(output, 'w+') as fp:
        pass
    for f in f_names:
        with open(f) as fp:
            
            soup = BeautifulSoup(fp, 'html.parser')
            
            with open(output, 'a') as fp:
                fp.write(soup.get_text())
                # print(i)
            # i += 1



if __name__ == '__main__':
    yrs = [i for i in range(2012,2022,1)]
    print("years: ", yrs)
    for y in yrs:
        dir = f"/Users/ruizeli/Documents/Colby18-21/Colby/Summer21/data/content/{y}"
        f_names = read(dir)
        # print(f_names)
        convert(dir, f_names, y)