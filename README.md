# JamendoDownloader
### Depends on
python3

### Usage
Create a file with one link to the jamendo page of each artist of whom you want to download his albums. Create the downloadlinks with

    python3 jamendo.py -i inputfile outputfile
or

    python3 jamendo.py linktojamendopageofartist outputfile

Download everything using wget or any other downloadmanager of your choice

    wget -i outputfile
