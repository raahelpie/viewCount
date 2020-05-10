# This video has <viewCount> views

Simple script that updates the YouTube video title every time the 
viewCount changes

The idea for this is the same as the famous Tom Scott's video:
You can check it here: https://www.youtube.com/watch?v=BxV14h0kFs0&t=5s

## Working

Following Tom Scott's lesson #1: dont pretend to be human
We are going to dodge the web scraping way of doing this and work with the APIs.

## Using the API

To able to use the YouTube API v3

Create a project in Google Developer Console and register your application inside the project to get the API_KEY and OAuth Client ID

We call 2 APIs in this script, one is to get the views and the other to update the title of the video.

As the views is public, API_KEY alone is enough for that, but because we are also trying to update the title whenever the viewCount and what the title says are different, we need to build the youtube resource using the OAuth client ID.

Download the client.json file from the project and put it in the same directory as your script, In the script, replace the client_page string with the name of the json file you downloaded.

Replace the videoID with your own video's ID which will be available in the url when you are watching the video.

When you run the file, you will be asked for a authentication key which will be displayed upon verifying your application. Because we didn't verify our app with Google in the GDC, you will prompted with a NOT SAFE page, ignore it, exit safe mode and give permissions to the application.

That's pretty much it. The title gets updated everytime the viewCount and count in title are not the same.
To keep it running, deploy this on a server!

