Kilimo360 - Ready project for Buildozer (improved)

What is included:
- Multi-screen Kivy/KivyMD app
- Dynamic simple JSON form renderer
- Map screen with touch polygon drawing, save/export GeoJSON
- Simple analytics (area, perimeter) using a local projection approximation
- buildozer.spec tuned for Android build (API 33, NDK 25b)

Important compatibility notes:
- Avoids compiled GIS libs (shapely/pyproj) to reduce Android build failures.
- Uses pure-Python geometry and a simple equirectangular projection approximation.
- Uses plyer for camera/GPS on device. On desktop these are stubs.

Dev setup (desktop test):
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python main.py

Build on WSL + Buildozer:
- Use the setup script buildozer_setup.sh (included) in WSL Ubuntu as guided.
- After SDK/NDK install, run: buildozer android debug

If you want I will:
- Attempt a full Buildozer build log analysis and tweak spec further.
- Add more form widgets (media, repeats) and map editing (vertex drag).
