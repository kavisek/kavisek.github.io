
# coding: utf-8

# # Update Website Notebook Content
# ### Find the Path to Specific File (First Match)

# In[5]:


# Import Modules
import os
import re
import time
from datetime import datetime
from numpy.random import randint
from shutil import copyfile
from tqdm import *


# Find file paths
def find_all_lists(list_of_files, path):
    '''
    Find the Paths to all the Files in a list within this list of filen names

    Parameteres:
    -----------
    list_of_paths (list of str): list of file names
    paths (str): abosolute path to the Directory, that we will search

    Examples:
    -----------
    find_all_lists(list_of_files,'/Users/Kavi/Documents/Science')


    '''
    result = []
    for name in list_of_files:
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))  # os.path.join(root, name) is a string
    return result


def desc_text(string):
    '''
    Fixing TQDM descrition text lenght
    '''
    # Remove Path
    string = re.sub(r'^(.*[\\\/])', '', string)

    # Fix File String
    target_length = 25
    if len(string) >= target_length:
        string = string[:target_length]
    else:
        additional_len = target_length - len(string)
        string = string+(' ')*additional_len
    return string


# ### Remove all "-meta" and ".ipynb' from the Content Directory

# In[30]:


# Find all file names within the content folder
files_for_deletion = []
for file in os.listdir("/Users/Kavi/Documents/Blog/content/"):
    if file.endswith("-meta"):
        files_for_deletion.append(os.path.join("/Users/Kavi/Documents/Blog/content/", file))
    elif file.endswith(".ipynb"):
        files_for_deletion.append(os.path.join("/Users/Kavi/Documents/Blog/content/", file))

# Delete all HTML files within the local contente folder
with trange(0, len(files_for_deletion))as pbar:
    for file in files_for_deletion:
        pbar.set_description("Removing Content Files: %s" % desc_text(file))
        pbar.update(1)
        os.remove(file)
        time.sleep(0.5)


# ### Find and Copy Files

# In[34]:


# Open Notebook Text File
with open('/Users/Kavi/Documents/Blog/notebooks.txt', 'r') as f:
    list_of_files = f.read().splitlines()

# locate the path to all the files in the notebook text file within the Science diretory
source_files = find_all_lists(list_of_files, '/Users/Kavi/Documents/Science')
source_files


meta_files = []
txt_files = []

# Copy all found files path 3 times under each file type and place them in the content folder
with trange(0, len(source_files))as pbar:
    for filepaths in source_files:
        pbar.set_description("Copying File: %s" % desc_text(filepaths))
        pbar.update(1)
        filename = re.findall(r'([^\/]+$)', filepaths)[0]
        copyfile(filepaths, '/Users/Kavi/Documents/Blog/content/'+filename)
        copyfile(filepaths, '/Users/Kavi/Documents/Blog/content/'+filename+'.txt')
        meta_files.append('/Users/Kavi/Documents/Blog/content/'+filename+'-meta')
        txt_files.append('/Users/Kavi/Documents/Blog/content/'+filename+'.txt')
        time.sleep(0.5)


# ### Writing Meta Files

# In[16]:


# For each text file in the directory, open its file and append HMTL meta tag information to the file
counter = 0
with trange(0, len(meta_files))as pbar:
    for txt_filepath, meta_filepath in tqdm(zip(txt_files, meta_files)):
        counter += 1
        pbar.set_description("Appending Meta-Tag: %s" % desc_text(meta_filepath))
        pbar.update(1)
        with open(txt_filepath, 'r', encoding='utf-8') as file:
            f_read = file.read()
            title = re.findall(r'"#(.*?)\\n"', f_read)[0]
            slug = re.findall(r'"#(.*?)\\n"', f_read)[0]

            # Locate Date Information
            date = txt_filepath.strip('/Users/Kavi/Documents/Blog/content/')
            date = re.findall(r'[0-9][0-9]-[0-9][0-9]-[0-9][0-9]', date, flags=0)
            date = date[0]
            year = date[0:2]
            month = date[3:5]
            month = month.lstrip('0')
            day = date[6:8]
            #day = day.lstrip('0')

            date = "20"+year+"-"+month+"-"+day+' 00:00'

        # Option Print Statements
        # print(txt_filepath)
        # print(meta_filepath)
        # print(date)
        # Append tag, title, category, date information to each file

        modified_date = str(datetime.now().year)+"-"+str(datetime.now().month) + \
            "-"+str(datetime.now().day)+' 00:00'
        category = 'Novice'
        tag = 'Python'
        author = 'Kavi Sekhon'
        summary = re.findall(r'(?=<span>)(.*\n?)(?=</span>)',
                             f_read)[0][0:150].strip('<span>') + '..'
        with open(meta_filepath, 'w', encoding='utf-8') as f2:
            f2.write(f'''Title:{title}
Date: {date}
Modified: {modified_date}
Category: {category}
Tags: {tag}
Slug:{title}
Author: {author}
Summary: {summary}
    ''')
            f2.write(f_read)
            f2.write(f'#{counter}')
        time.sleep(0.5)


# ### Removing Text Files

# In[ ]:


# Remove all the text files for the txt path
with trange(0, len(meta_files))as pbar:
    for txt_filepath in txt_files:
        pbar.set_description("Removing Content Text Files: %s" % desc_text(txt_filepath))
        pbar.update(1)
        os.remove(txt_filepath)
        time.sleep(0.5)


# Author: Kavi Sekhon
