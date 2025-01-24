# Images_Organiser
Organise your photos and videos with metadata

This is a script in PYTHON to aoganise files with metadata read with exiftool (photos and videos from digital camera/smartPhone)

1. Group all pictures and videos you want to organise in a folder (SOURCE). You can use CommanderOne or similar to import files from smartphone.
2. Get Exiftool from official page https://exiftool.org/ and copy location of .exe file. Example "C:\exiftool\exiftool.exe" (need to be exact as appear in your folder, not as the example)
3. Get Python installed in your machine. https://www.python.org/downloads/
4. Copy the script ExifOrganiser.py in a location to be executed (will execute in command line)
5. run CMD or command line app in your machine
6. Run the script with the command [python c:\LocationOfTheScript\ExifOrganiser.py
7. It will pront the SOURCE FOLDER. Insert it and hit enter Example C:\SOURCE
8. Now will pront with DESTINATION FOLDER. Insert it and hit enter Example C:\DESTINATION
9. It will COPY and RENAME files in Organised Folders with structure [YYYY/YYYYMMDD/YYYYMMDD_hhmmss_ORIGINALFILENAME.*]
10. Check if it is all correct and delete source folder 

