from pathlib import Path

tmp_folders = []
folders = []
files = []
result = []

lines = 0

import os

rootdir = '.'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d) and d != './.git':
        tmp_folders.append(d)
        d = d[2:]
        folders.append(str(f"| {d} | "))


for a in tmp_folders:
    a = a[2:]

    a = str(a)
    folder_name = a
    folder = Path(folder_name)
    if folder.is_dir():
        folder_count = len([1 for asa in folder.iterdir()])
        files.append(str(f"{folder_count} |"))


result = map(sum, zip(str(folders),str(files)))
result = [x+y for x, y in zip(folders, files)]

readme = open('README.md', 'r+')
file_lines = readme.readlines()
for line in file_lines:
    lines += 1

readme.seek(0)
readme.truncate()

readme.writelines(file_lines[:6])

for listitem in result:
    readme.write('%s\n' % listitem)
readme.write('\n</div>')
