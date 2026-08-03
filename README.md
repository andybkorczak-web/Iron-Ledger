# Iron Ledger — Desktop App

A real desktop app (Electron) version of the Iron Ledger 6-week programme:
native window, taskbar/dock icon, no browser required. Your logged data is
saved locally on your computer.

## Quick start (run it without building anything)

```
npm install
npm start
```

This opens the app in a window immediately — good for trying it out or for
your own day-to-day use if you're comfortable running it from a terminal.

## Build a real installer (.exe / .dmg / .AppImage)

```
npm install
npm run dist          # builds for whatever OS you're running this on
npm run dist:win       # Windows .exe   (best run on Windows)
npm run dist:mac       # macOS .dmg     (must be run on a Mac)
npm run dist:linux     # Linux AppImage + .deb
```

Finished installers land in the `release/` folder.

**Important:** each platform's installer is best built *on that platform*.
Building a `.dmg` in particular really needs a real Mac — Apple's tooling
for that isn't available anywhere else. Building a Windows `.exe` from
Mac/Linux is technically possible with extra tools (Wine) but is fragile
and not recommended.

## Building all three automatically (recommended) — GitHub Actions

This project includes `.github/workflows/build.yml`, which builds the
Windows, macOS, *and* Linux installers automatically using GitHub's own
build machines — so you never need to own a Mac or fight with Wine.

1. Push this project to a new GitHub repository.
2. Go to the repo's **Actions** tab → select **"Build Iron Ledger"** →
   **"Run workflow"**.
3. Wait a few minutes. Three build jobs run in parallel (one per OS).
4. Open the finished run and download the artifacts — you'll get a `.exe`,
   a `.dmg`, and an `.AppImage`/`.deb`, ready to hand out or install.

## Project structure

```
main.js            Electron entry point — creates the app window
app/index.html      The app itself (same UI/logic as the browser version)
build/icon.png      Source icon (electron-builder auto-generates .ico/.icns from this)
package.json         Scripts + electron-builder configuration
.github/workflows/   CI that builds all 3 platforms
```

## Notes

- **No code signing is set up.** Unsigned installers will trigger an
  "Unknown publisher" (Windows) or "unidentified developer" (Mac) warning
  the first time someone runs them. This is normal and doesn't affect
  functionality — to remove the warning you'd need a paid code-signing
  certificate (Windows) or an Apple Developer account (Mac).
- **Your data** is stored in the app's local storage on whichever computer
  it's installed on. Use the in-app **Export**/**Import** buttons to move
  your logged data between installs or back it up.
- To change the app icon, replace `build/icon.png` with a new **1024×1024**
  PNG — electron-builder generates every platform's icon format from it
  automatically on the next build.
