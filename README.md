# JamendoDownloader
### Depends on
python3

### Usage
Create a file with one link to the jamendo page of each artist of whom you want to download his albums. Create the downloadlinks with

    python jamendo.py -i inputfile outputfile
or

    python jamendo.py linktojamendopageofartist outputfile
If your distro doesn't use python3 as the default python interpreter you maybe have to replace python with python3

Download everything using wget or any other downloadmanager of your choice

    wget -i outputfile
