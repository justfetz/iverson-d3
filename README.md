# The Answer, Every Game — an Allen Iverson career dashboard in d3.js

One page, no build step. Live: https://justfetz.github.io/iverson-d3/. Every one of Iverson's 985 NBA games (914 regular season + 71 playoff) is drawn as a basketball: seasons run left to right, months top to bottom, the balls climb with the calendar inside each month, size is points scored, filled is a win and hollow is a loss. Hover any ball for the full box score. Below that: comparison bars against other greats (pick your own set, regular season or playoffs), season-by-season trends, the fourteen 50-point nights, and his all-time leaderboard spots.

## Files

| Path | What it is |
|---|---|
| `index.html` | The whole dashboard (HTML + CSS + d3 code). Loads d3 v7.9.0 from cdnjs and Google Fonts (Anton, Barlow). |
| `data.js` | All the data as one `window.AI_DATA` object. Generated, don't hand-edit. |
| `data/gamelog_YYYY.csv` | One file per season (year = season end), every game he played, with the full box score. |
| `data/comps.csv` | Career per-game lines (regular season + playoffs) for the 18 comparison players. |
| `data/iverson_ranks.csv`, `data/iverson_50pt.csv` | All-time ranks and 50-point games. |
| `scripts/build_data.py` | Rebuilds `data.js` from the CSVs. |

## Run it locally

Open `index.html` in a browser. That's it (the page reads `data.js` with a plain `<script>` tag, so it works from `file://`). If you prefer a server: `python3 -m http.server 8000` and visit http://localhost:8000.

## Put it on GitHub Pages

1. Create a new repository on GitHub (public, so Pages is free), e.g. `iverson-d3`.
2. Push these files to the `main` branch:
   ```bash
   git init
   git add .
   git commit -m "Allen Iverson career dashboard"
   git branch -M main
   git remote add origin https://github.com/justfetz/iverson-d3.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch"**, branch `main`, folder `/ (root)`. Save.
4. After a minute the site is live at `https://justfetz.github.io/iverson-d3/`. The URL shows up on that same Pages settings screen.

Nothing else is needed: Pages serves static files, `index.html` is the entry point, and there is no framework or bundler to configure.

## Add his photo

The card's circular badge shows an "AI" monogram by default. Drop a square image named `photo.jpg` next to `index.html` and it fills the circle automatically (the page tries to load it and quietly falls back to the monogram if it isn't there). Use an image you have the rights to post.

## Change or extend the data

- The CSVs are the source of truth. Edit them (keep the headers) and run `python3 scripts/build_data.py` to regenerate `data.js`.
- To add a comparison player, add two rows to `data/comps.csv` (one `RS`, one `PO`) and rebuild; the chips and charts pick the player up automatically.
- The dashboard sanity-checks: the game logs sum to the official career line (24,368 points, 5,624 assists, 1,983 steals, 3,394 rebounds in 914 regular-season games), and every row satisfies `pts = 2*fgm + tpm + ftm` and `reb = oreb + dreb`.

## Sources and credits

- Game-by-game box scores, career averages and all-time rankings: [landofbasketball.com](https://www.landofbasketball.com/nba_players/allen_iverson.htm) (fetched October 14, 2026). The earlier Tableau version of this idea used ESPN and Basketball-Reference; those numbers reconcile.
- Team colors: 76ers 1997–2009 (black `#040204`, red `#D50032`, gold `#BB9754`), Nuggets 2003–17 (powder blue `#418FDE`), Pistons 2005–17 (blue `#003DA5`), Grizzlies (Beale Street Blue `#5D76A9`), via teamcolorcodes.com / brandcolorcode.com.
- Charts: [d3.js](https://d3js.org/) v7.
