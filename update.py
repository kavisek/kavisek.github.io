
# coding: utf-8

# # Update Website Notebook Content
# ### Find the Path to Specific File (First Match)

# In[6]:


# Import Modules
import os
import re
import time
from numpy.random import randint
from shutil import copyfile
from tqdm import *



# Find file paths
def find_all_lists(list_of_files, path):
    time.sleep(0.05)
    result = []
    for name in list_of_files:
      for root, dirs, files in os.walk(path):
          if name in files:
              result.append(os.path.join(root, name)) # os.path.join(root, name) is a string
    return result


# ### Remove all "-meta" and ".ipynb' from the Content Directory

# In[7]:


# Final all file names within the content folder
files_for_deletion = []
for file in os.listdir("/Users/Kavi/Documents/Blog/content/"):
  if file.endswith("-meta"):
    files_for_deletion.append(os.path.join("/Users/Kavi/Documents/Blog/content/", file))
  elif file.endswith(".ipynb"):
    files_for_deletion.append(os.path.join("/Users/Kavi/Documents/Blog/content/", file))

# Delete all HTML files within the local contente folder
for file in files_for_deletion:
  print(file)
  os.remove(file)
  time.sleep(0.05)


# ### Find and Copy Files

# In[9]:


# Open Notebook Text File
with open('/Users/Kavi/Documents/Blog/notebooks.txt','r') as f:
  list_of_files = f.read().splitlines()

# locate the path to all the files in the notebook text file within the DataScience diretory
source_files = find_all_lists(list_of_files,'/Users/Kavi/Documents/DataScience')
source_files


meta_files = []
txt_files = []

# Copy all found files path 3 times under each file type and place them in the content folder 
for filepaths in tqdm(source_files):
  filename = re.findall(r'([^\/]+$)',filepaths)[0]
  copyfile(filepaths, '/Users/Kavi/Documents/Blog/content/'+filename)
  copyfile(filepaths, '/Users/Kavi/Documents/Blog/content/'+filename+'.txt')
  meta_files.append('/Users/Kavi/Documents/Blog/content/'+filename+'-meta')
  txt_files.append('/Users/Kavi/Documents/Blog/content/'+filename+'.txt')
  time.sleep(0.05)


# ### Writing Meta Files

# In[10]:


counter = 0

# For each text file in the directory, open its file and append HMTL meta tag information to the file
for txt_filepath, meta_filepath in zip(txt_files,meta_files):
  counter += 1
  print(txt_filepath)
  print(meta_filepath)
  with open(txt_filepath,'r',encoding='utf-8') as file:
    f_read = file.read()
    title = re.findall(r'"#(.*?)\\n"', f_read)[0]
    slug = re.findall(r'"#(.*?)\\n"', f_read)[0]
    author ='Kavi Sekhon'
    
    # Locate Date Information
    date = txt_filepath.strip('/Users/Kavi/Documents/Blog/content/')
    date = re.findall(r'[0-9][0-9]-[0-9][0-9]-[0-9][0-9]',date,flags=0)
    date = date[0]
    year = date[0:2]
    month = date[3:5]
    month = month.lstrip('0')
    day = date[6:8]
    #day = day.lstrip('0')
    print(date, year, month, day)
    date = "20"+year+"-"+month+"-"+day+' 00:00'
    print(date)
    
    
    # Append tag, title, category, date information to each file 
    category = 'Novice'
    tag = 'Python'
    summary = re.findall(r'(?=<span>)(.*\n?)(?=</span>)',f_read)[0][0:150].strip('<span>') + '..'
    with open(meta_filepath,'w',encoding='utf-8') as f2: 
        f2.write(f'''Title:{title}
Slug:{title}
Date: {date}
Category: {category}
Tags: {tag}
Author: {author}
Summary: {summary}

''')
        f2.write(f_read)
        f2.write(f'#{counter}')
    time.sleep(0.05)


# ### Removing Text Files

# In[11]:


# Remove all the text files for the txt path
for txt_filepath in txt_files:
  print('Removed:',txt_filepath)
  os.remove(txt_filepath)
  time.sleep(0.05)


# Author: Kavi Sekhon
