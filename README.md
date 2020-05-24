# web-scraping-challenge
Web Scraping assignment from Rutgers Data Science Bootcamp

Mission to Mars
Flask web application that scrapes various websites for data related to the Mars Mission and displays the information in a single HTML page.

Scrapping
NASA Mars News :
Web URL visited : https://mars.nasa.gov/news/
Beautiful Soup script collects the latest News Title and Paragraph Text.

JPL Mars Space Images - Featured Image :
Web URL visited : https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
Beautiful Soup script finds the image url for the current Featured Mars Image and assigns the url string of the full size image.

Mars Weather :
Web URL visited : https://twitter.com/marswxreport?lang=en
Beautiful Soup script visits the Mars Weather twitter account and scrapes the latest Mars weather tweet.

Mars Facts :
Web URL visited: https://space-facts.com/mars/
Beautiful Soup script visit the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Mars Hemispheres:
Web URL visited: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
Beautiful Soup script visits the USGS Astrogeology site and obtains the full resolution images for each of Mar's hemispheres by traversing through individual pages of each result.

MongoDB and Flask Application
The MongoDB is currently hosted locally when development was done. It assumes that the grader will have a local instance running as well to run the application. All the code has been provided in the Flask folder.

Final Screenshots:
![Screen 1](/Screenshots/Mission%20to%20Mars_Page_1.png)

![Screen 1](/Screenshots/Mission%20to%20Mars_Page_2.png)

