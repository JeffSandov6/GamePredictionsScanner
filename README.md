# GamePredictionsScanner

Built this project to work on my web parsing and to try out python 3.8. It's a simple project that, for the time being, scans 3 of the top sports betting prediction sites. I may add more websites in the future, not quite sure yet. You put in a game whose predictions you may be interested in seeing, on any given day, and you are returned all the available predictions.

This particular crawler is interesting because it bypasses any member registrations that those sites require to get their predictions. What this means is, some of these websites sometimes charge for you to see their predictions, but by going straight to, and manipulating their HTML, you can get the predictions for free instead.

For anybody interested, using it is really simple. Once you clone the repository, just bring up your terminal and run either:
python App.py (if you have anything below python 3.x) 
python3 App.py (if you have python 3.x)

You are then asked to put the name of the 2 teams that are playing, and their sport. As of now, this project only supports NBA games, college basketball games, and NFL games.
