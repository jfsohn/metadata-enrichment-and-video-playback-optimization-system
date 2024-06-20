# Metadata Enrichment and Video Playback Optimization System

An intelligent system that enhances IMDB media content and will eventually optimize video playback quality.

1. Install mySQL and Python 3
2. Sign up for an [OMDB API Access Key](https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0oCxKYG7xaZwy2ktIrVmWGdWzxj%2FDhHQaAqqFYTiRTDE%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU%2BO86JjTqdg0yhuGR2tBukmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulHLL4j%2B3qCcW3ReXhfb4KKsSs3zlQ%2B48KY6Qzm7wzZbR&at=freeAcct&Email=) Then, use it for the API_KEY variable in extract_metadata.py.
3. Start a mySQL server
4. Open the extract_metadata.py file in this repo's metadata subfolder
5. Modify the extract_metadata.py file for the host, user, and password variables with the appropriated values from your mySQL server
6. Modify the "movie_titles" variable in the extract_metadata.py file with the movies you would like to get metadata for
7. Open cmd line and change dir to the main directory of the repo. Next, run the following command:
<code> source main.sql </code>
8. Open cmd line and change dir to the metadata subfolder. Next, run the following command:
<code> python extract_metadata.py </code>
9. You should now have a db titled movie_metadata with a movies table that contains metadata for all of the movies you chose
10. Open cmd line and change dir to the main directory of the repo. Next, run the following command:
<code> python application.py </code>
12. Optional: Create an RDS instance in AWS with a database and an Elastic Beanstalk environment. After that, init, create, and deploy the EB application.

TODO:

1) Commit History Squashing
2) Set up an AWS Lambda function to transcode video to different formats
3) Use AWS S3 for storing the transcoded videos
4) Implement a service to package video and metadata for different platforms
5) Install and configure Kafka
6) Create topics for communication between services
7) Develop producers and consumers for Kafka topics to handle event-driven communication
8) Create a Java service to monitor and optimize video playback quality
9) Integrate with AWS CloudWatch for metrics collection
10) Implement adaptive bitrate streaming logic
11) Implement a collaborative filtering model for content recommendations
12) Integrate the recommendation system with the metadata service
13) Use OpenCV to detect key scenes in the video for generating thumbnails
