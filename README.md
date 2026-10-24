# Particles HP (Android app)

A glowing particle heart that reacts to your music. Tap to burst, hold to scatter, let go and it re-forms.
The first touch starts the music. The folder button at the top left opens the playlist.

## Get the APK (about 10 minutes, once)

1. Make a free account at github.com and create a new repository named `particles-hp`. Choose **Public**.
2. On a computer, unzip this folder. In your new repository choose **Add file > Upload files** and drag in everything inside the folder, including the hidden `.github` folder. Press **Commit changes**.
   If the `.github` folder does not upload, choose **Add file > Create new file**, type `.github/workflows/build-apk.yml` as the name and paste in the contents of that file.
3. Open the **Actions** tab. The **Build APK** job starts by itself and takes about 5 to 8 minutes. A green tick means it worked.
4. Download the APK from **Releases** (right side of the repository page): `Particles-HP.apk`.
5. Open the APK on your Android phone. Allow installing from this source when Android asks, then install.

If the job shows a red cross, open it, copy the error text and send it to Claude.

## Built-in songs

The songs in `www/songs` are built into the APK, so anyone you send the APK to gets them too.
To add more, upload audio files to `www/songs` in the repository (**Add file > Upload files**). The app rebuilds by itself.
Only share music you have the right to share.

## Songs from your phone

In the app, tap the folder button, then **Add songs**. These stay on that phone only and are not part of the APK.

## No pictures needed

The app icon and splash screen are drawn during the build by `scripts/make-icons.py`, so the repository holds no image files.
