
# -- Pelican Blog Update Script --

# Remove files from output directory
echo Removing Files from Output
rm -rf output/* #recursive removal (Down every subfolder)

# Sleep 5 Seconds
sleep 5

# Use Main Conda Enviroment (named main)
source activate main

# Regenerating Pelican Content
echo Regenerating Content
pelican content
echo Content Updated

# Push New  Content to Master Branch on Github Pages
echo Pushing Content to Master
ghp-import output -b master
echo Implementing Git Push
git push origin master
echo Content Pushed to Master

# Start Staging Server
echo Starting Staging Server
cd output/
python -m http.server
echo Done
