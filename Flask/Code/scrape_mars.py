import time
import re
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    # need to write alternate code for macbooks
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    #initialize a dictionary to create a collection of important key value pairs about mars as a planet
    marsinfo_dict = {}
    browser = init_browser()

    # Section 1-Scraping
    # Task 1-NASA Mars News
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    # # Example:
    # news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
    #
    # news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
    # Visit the following URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(3)

    # Scrape page into Soup
    # getting the html content from the browser instance launched using splinter
    html = browser.html

    # scrape the web page using beautiful soup and lxml parser
    soup = bs(html, 'lxml')
    # getting title for latest article
    article = soup.find('article')
    article_list = article.find_all('ul', class_='item_list')
    article_latest = article_list[0].find_all('li', class_='slide')[0]
    article_header = article_latest.find('div', class_='content_title').text
    # add this to the dictionary
    marsinfo_dict.update({'article_header_key':article_header})
    # getting summary for latest news title
    article_para = article_latest.find('div', class_='article_teaser_body').text
    marsinfo_dict.update({'article_para_key': article_para})
    # Task 2- JPL Mars Space Images - Featured Image
    # Visit the url for JPL Featured Space Image here.
    #
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    #
    # Make sure to find the image url to the full size .jpg image.
    #
    # Make sure to save a complete url string for this image.
    #
    # # Example:
    # featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    # Visit the following URL
    url_nasa = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_nasa)
    time.sleep(3)
    # getting the html content from the browser instance launched using splinter
    html = browser.html

    # scrape the web page using beautiful soup and html parser
    soup = bs(html, 'lxml')
    data = soup.find('div', id='main_container')
    # extracting the image url from data
    image_data = data.find('footer')
    image_data
    mars_image = image_data.find('a').get('data-fancybox-href')
    mars_image
    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url + mars_image
    marsinfo_dict.update({'feature_image_key': featured_image_url})
    #Task 3-Mars Weather
    # Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.
    # Note: Be sure you are not signed in to twitter, or scraping may become more difficult.
    # Note: Twitter frequently changes how information is presented on their website. If you are having difficulty getting the correct html tag data, consider researching Regular Expression Patterns and how they can be used in combination with the .find() method.
    # # Example:
    # mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
    # visit the twitter url
    url_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_twitter)
    time.sleep(3)
    # parse the html
    html_twitter = browser.html
    soup = bs(html_twitter, 'lxml')
    # scraping mars weather tweet for latest tweet and weather data
    mars_tweet = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-5f2r5o r-1mi0q7o')
    # type(mars_tweet)
    # print(mars_tweet[0].prettify())
    mars_weather_list = mars_tweet[0].find_all('span',
                                               class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    mars_weather = mars_weather_list[4].text
    #add the weather informatio to the dictionary
    marsinfo_dict.update({'weather_tweet_key': mars_weather})
    #Task 4 - Mars Facts
    # Task 4- Mars Facts
    # Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.
    # space-facts url
    url_space = 'https://space-facts.com/mars/'

    # using pandas to scrape the table containing facts about the planet
    mars_data = pd.read_html(url_space)
    # converting the table to a dataframe
    mars_df = mars_data[0]
    mars_df.columns = ['Attribute', 'Value']
    # converting the data to an HTML table string
    mars_html = mars_df.to_html(index=False)
    #store it in the dictionary
    marsinfo_dict.update({'mars_spacefacts_key': mars_html})
    # Task 5-Mars Hemispheres
    # Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    #
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    #
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    #
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    # visit the url
    url_hemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemisphere)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'lxml')
    img_list = soup.find('div', class_='collapsible results')
    # find all the images(hyperlink for pages) within the image list and use that info to launch it
    # base url for this assignment was 'https://astrogeology.usgs.gov'
    base_url = 'https://astrogeology.usgs.gov'
    url_coll = []
    image_info_coll = soup.findAll('div', class_='item')
    for image_info in image_info_coll:
        # get the anchor tag value and append it to base url
        url_coll.append(base_url + image_info.find('a')['href'])
    # for all the above links , use splinter to open each one of them and then save both the image url string for the full resolution hemisphere
    # image, and the Hemisphere title containing the hemisphere name.
    # Use a Python dictionary to store the data using the keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list.
    # This list will contain one dictionary for each hemisphere.
    lst_fullimageinfo = []
    text_pattern = re.compile('Sample')
    title = ''
    fullimage_url = ''
    for url in url_coll:
        browser.visit(url)
        time.sleep(3)
        time.sleep(3)
        html = browser.html
        soup = bs(html, 'lxml')
        # upon inspection the image url is under the download section of the webpage
        # find the div tag with class = downloads and within that find the anchor tag where text=original
        fullimage_url = soup.find('div', class_='downloads').find('a', text=text_pattern)['href']
        # The title is in h2 class=title
        title = soup.find('h2', class_='title').text
        # Now that you have the url and title , append it to the dict and then append the dictionary to the list
        dict_mars_hemispheres = {'title': title, 'img_url': fullimage_url}
        lst_fullimageinfo.append(dict_mars_hemispheres)
        # reset
        dict_mars_hemispheres = {}
    # Now append the information of all the full images into a dictionary
    marsinfo_dict.update({'image_list_key': lst_fullimageinfo})
    # Close the browser after scraping
    browser.quit()

    # Return results
    return marsinfo_dict
