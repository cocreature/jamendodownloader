# JamendoDownloader
### Depends on
python3

### Usage
Create a file with one link to the jamendo page of each artist of whom you want to download his albums. Create the downloadlinks with
    python jamendo.py inputfile outputfile
Download everything using wget
    wget -i outputfile
