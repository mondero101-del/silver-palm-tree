// Lists every audio file in www/songs and writes www/songs/songs.json.
// The app reads that list to build its built-in playlist.
const fs = require("fs");
const path = require("path");
const dir = path.join(__dirname, "..", "www", "songs");
const exts = [".mp3", ".m4a", ".aac", ".ogg", ".opus", ".wav", ".flac"];
const files = fs.readdirSync(dir)
  .filter((f) => exts.includes(path.extname(f).toLowerCase()))
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
const list = files.map((f) => ({
  file: f,
  title: path.basename(f, path.extname(f)).replace(/_+/g, " ").trim(),
}));
fs.writeFileSync(path.join(dir, "songs.json"), JSON.stringify(list, null, 2) + "\n");
console.log("songs.json: " + list.length + " song(s)");
