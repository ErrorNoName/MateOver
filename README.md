# Discord-VC-Exploit
Discord Region Swapping Exploit (VC Overload) ERROR VC Crasher

# How does this work?
Discord has multiple servers that lets people around the world connect from there region to one big huge connecting other people in the same voice call hub.

# How do I exploit it?
Changing the Region of an call is serversided as it changes not for only one person but the entire call including everyone else. \n
Making a simple loop that abuses the api functions that control the region of an vc will instantly take down the voice call

# Why
Discord uses threads for most api functions including region api, if we were to spam change the region at once it would overload discord as it attempts to connect to mltiple regions as once causing a loop of errors. Which results in a crash.

# Credits
Ezio
