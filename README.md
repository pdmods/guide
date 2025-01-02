# Pandanda Modding Guide

This guide provides detailed instructions on how to mod Pandanda. You might not need all the steps, so read through the entire guide first and pick the parts relevant to your needs.

---

## Prerequisites

Before starting, ensure you have the following tools installed:

1. **Python**
   - Download from [python.org](https://www.python.org/).
   - When installing, **make sure to check** "Add python.exe to PATH" to avoid potential issues.

2. **JPEXS Free Flash Decompiler**
   - Download from [GitHub](https://github.com/jindrapetrik/jpexs-decompiler/releases).
   - This tool is required to decompile SWF files.

3. **XAMPP**
   - Download from [Apache Friends](https://www.apachefriends.org/).
   - It provides a simple local web server.

---

## Step 1: Configure the Client

1. **Obtain the Client**
   - Download the `Project Pandanda Windows Client.zip` from Project Pandanda.
   - Inside, you'll find an installer and an archive. You can delete the installer as it's unnecessary.
   - Extract the archive to access `pdc-app.exe`. This file runs the client without installation.

2. **Modify the Client**
   - Navigate to `\resources\app\src\main.js` inside the client folder.
   - Locate the `const CreateWindow` function and modify it as follows:
     ```javascript
     const createWindow = () => {
       mainWindow = new BrowserWindow({
         width: 1280,
         height: 720,
         autoHideMenuBar: false,
         useContentSize: true,
         webPreferences: {
           devTools: true,
           plugins: true
         }
       });

       mainWindow.webContents.on('new-window', function(e, url) {
         e.preventDefault();
         require('electron').shell.openExternal(url);
       });
       mainWindow.loadURL(mainURL);
     };
     ```
   - Save the changes.

3. **Use Developer Tools**
   - Start the client and enable developer tools:
     - Click `View > Toggle Developer Tools > Network`.
   - Reload the page (`View > Reload`) to see all the files being requested.
   - Navigate through all Pandanda locations to identify and download all files used.

4. **Organize the Files**
   - Create a folder that mimics the server's structure.
   - Ensure you have at least `index.html` and `pandanda.swf`.
   - **Shortcut Option:** Use the provided `scrapper.py` script:
     - The script reads `folder_structure.txt` and downloads the files, creating a `base` folder with all necessary files.

---

## Step 2: Configure the Local Web Server

1. **Set Up XAMPP**
   - Open XAMPP and start Apache.
   - Navigate to `C:\xampp\htdocs` and delete everything in that folder.
   - Replace the contents with your base game files (either self-collected or collected by the script).

2. **Point the Client to Localhost**
   - Navigate to `\resources\app\src\main.js`.
   - Replace the following line:
     ```javascript
     const mainURL = "https://play.projectpandanda.com/";
     ```
     with:
     ```javascript
     const mainURL = "https://localhost/";
     ```
   - Start the client again.

   Alternatively, use a Flash browser like [Flash Browser](https://github.com/radubirsan/FlashBrowser/releases). Note: This browser may retain cache, requiring manual clearing for updates to appear.

3. **Verify Setup**
   - If configured correctly, you should see the Pandanda loading screen saying: "Please visit default to play."

---

## Step 3: Configure the Game

1. **Edit `pandanda.swf`**
   - Open `pandanda.swf` with JPEXS.
   - Use the text search tool (top bar) to search for the original domain (e.g., `play.projectpandanda.com`).
   - Edit the domain string to `localhost`:
     - Because this file contains obfuscated code, use the **right editor**. The right editor is only needed for this file!.
     - Click "Edit P code" to make the change.
   - Save the file, and on the top toolbar click save again, than close JPEXS.

2. **Test the Configuration**
   - Open the client again. You should now be able to log in.
   - Use network developer tools to troubleshoot any missing files.

---

## Step 4: Modding the Game

1. **Decrypt SWF Files**
   - All files are encrypted with XOR and the key is `d02adaa4cf8fe4859fda09ae936aadbf138001925203340fa89d6c99b546d97e`. (see scripts/<default package>/override inside pandanda.swf for reference)
   - Use the `dectool.py` script to decrypt them:
     - Place the SWF file (e.g., `UI/game_ui.swf`) in the same folder as `dectool.py`.
     - Run the script to generate a decrypted file ending in `.dec.swf`.

2. **Edit SWF Files**
   - Open the decrypted SWF file with JPEXS.
   - For example, to change the "Friends" string to "Enemies":
     - Use the global search tool to locate "Friends".
     - Edit the string in the appropriate file (e.g., `PlayerCard`).
     - Save the changes and close JPEXS.

3. **Re-Encrypt the File**
   - Run the `dectool.py` script again to re-encrypt the file.
   - Replace the old SWF file in your base game with the newly modified version.

---

## Final Notes

- [GitHub Repository for mpandanda](https://github.com/mpandanda/mpandanda.github.io) contains many interesting game files, including maps.
- Can these files create a private server? No, nobody has made the server-side source code publicly available yet. This guide covers only the client-side modding process.
