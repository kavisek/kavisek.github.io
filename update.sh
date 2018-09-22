
# -- Pelican Blog Update Script --

# Remove files from output directory
echo Removing Files from Output
rm -rf /Users/kavi/Documents/Blog/output/* #recursive removal (Down every subfolder)

# Sleep 5 Seconds
sleep 5

# Use Main Conda Enviroment (named main)
source activate main

# Regenerating Pelican Content
echo Regenerating Content
cd /Users/kavi/Documents/Blog/ && pelican content
echo Content Updated

# Copy Blog README file to output directory
cp /Users/kavi/Documents/Blog/README.md /Users/kavi/Documents/Blog/output/README.md

# Sleep 5 Seconds
sleep 5

# Push to Github Commands
# source activate main
# ghp-import output -b master
# git push origin master
