# genshin-wish-tracker

Just a script that pulls wish data and exports to a text file. Might be useful if you wanted to back it up or look at it without going through the web interface.

## How it works

Normally, if you want to view your wish history, you would open the game menu, select "Wish", and then click on "History" at the bottom.
You can then select the wish type from the dropdown to look at different categories.

This script basically automates it for you and will create a comma-separated text file that you can open in excel or other spreadsheet tool

## Download

Press the "Code" button and then download the zip file. All you need is client.py and config.txt

## Usage 

In order to get the wish history, this script will need to make a request to the game servers using your current login session. Instead of using your username and password, we will assume you are already logged in to the game.

Open the game menu and select "Feedback". This will open your browser. Copy the entire URL, open "config.txt" in notepad, and replace whatever is inside with the URL.

Once this is done, you can then run the script, assuming you have python installed.

When the script finishes running, it will create a file called "log.csv". It will also create another file called "history.dat" which just holds all of the old data that the script uses to generate the log (in case it gets deleted from their history)

## Security

All of the code is contained inside client.py. You can take a look at it if you're curious if it's doing anything weird.
