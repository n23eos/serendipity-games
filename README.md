# Serendipity Games

A casual browser-game portfolio featuring playable, unreleased demos of Raindrops, Ricochet: Neon Drive, Bunny Runner, and Jelly Mix.

Published with GitHub Pages from the main branch root. No server or install required. The site and all game assets use relative paths.

## Update games

With the original projects and installed dependencies in sibling folders, run `python3 scripts/import-games.py`. It builds isolated temporary copies with standalone platform adapters and English defaults, then copies only production builds into `games/`. Original projects are not modified. Demo rewards may be simulated; this is not a Poki SDK integration.

## Local preview

Run `python3 -m http.server 8080` and open http://localhost:8080.

## Rights

All rights reserved. Game builds and artwork are provided for browser play and portfolio review. No redistribution license is granted.
