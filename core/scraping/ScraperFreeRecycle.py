from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# class for Scraping Website FreeRecycle
class ScraperFreeRecycle():
    # constants paths of files to write output information
    FILE_EMAILS = './output/emails.txt'
    FILE_URL_ALL = './output/url_all.txt'
    FILE_OTHER_URL = './output/other_url.txt'
    FILE_URL_VISITED = './output/url_visited.txt'
    FILE_SUBDOMAIN_ALL = './output/subdomain_all.txt'
    FILE_URL_FILES = './output/url_files.txt'
    
    # declarate the variable used on the class, to manage the data extracted
    main_url = ''
    html_text = ''
    url_all = []
    subDomain_all = []
    url_visited = []
    other_url = []
    emails = []
    files_url = []
    numRequest = 0

    # constructor
    def __init__(self, main_url):
        # add the main url to scrap into the array of URL ALL, to have initially 1 url to scan
        self.main_url = main_url
        self.url_all.append(main_url)
        
        # initialize a variable to count the number of the request done
        numRequest = 0

        # initialized empty files to output information extracted
        f = open(self.FILE_EMAILS, 'w+')
        f.close()
        f = open(self.FILE_URL_ALL, 'w+')
        f.close()
        f = open(self.FILE_OTHER_URL, 'w+')
        f.close()
        f = open(self.FILE_URL_VISITED, 'w+')
        f.close()
        f = open(self.FILE_SUBDOMAIN_ALL, 'w+')
        f.close()
        f = open(self.FILE_URL_FILES, 'w+')
        f.close()
        #self.html_text = self.extract_html_text(self.main_url)
    
    # get the text of the website in html format. Return a soup with html structure
    def extract_html_text(self, url):
        # read the url to get the data into html format but everything in one line
        raw_html = self.simpleGet(url)

        # counting the number of the requests adding 1, and printing the number of the request
        self.numRequest = self.numRequest + 1
        print("Request: ", self.numRequest)

        # structure the one line html text into html format for easy read
        html_soup = BeautifulSoup(raw_html, 'html.parser')
        return html_soup
    
    # attempts to get the content at 'url' by making and HTTP GET request.
    # if the content-type of response is some kind of HTML/XML, return the
    # text content, otherwise return None
    def simpleGet(self, url):
        # trying to execute a request from the url pass for scrap or scan
        try:
            with closing(get(url, stream=True)) as resp:
                if self.isGoodResponse(resp):
                    #return resp.content
                    return resp.text
                else:
                    return None
        # if it fail return a exception with the error ocurred
        except RequestException as exception:
            self.logError('Error during request to {0} : {1}'.format(url, str(exception)))
            return None
    
    # returns True if the response seems to be HTML, False otherwise
    def isGoodResponse(self, resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)
    
    # it is always a good idea to log errors this function just prints them, but you can make it do anything
    def logError(self, exception):
        print(exception)

    # print the data stored in the variables of the class
    def printData(self, dataType):
        # print the main url pass to scrap
        if dataType == "main_url":
            print(self.main_url)
        
        # print the HTML text scrapped from the url that is scraping on the moment
        elif dataType == "html_text":
            print(self.html_text)
        
        # print all the url indexed or scapper related to the website, this urls will be scraped or indicted
        elif dataType == "url_all":
            if self.url_all != None:
                self.url_all.sort()
                f = open(self.FILE_URL_ALL, 'w+')
                for url in self.url_all:
                    print(url)
                    f.write(url + '\n')
                f.close()
            else:
                print("URL ALL - EMPTY")
        
        # print all the other urls that initially are not interested to scrap
        # maybe they are ofuscated and it is for check how to filter
        elif dataType == "other_url":
            if self.other_url != None:
                self.other_url.sort()
                f = open(self.FILE_OTHER_URL, 'w+')
                for url in self.other_url:
                    print(url)
                    f.write(url + '\n')
                f.close()
            else:
                print("OTHER URL - EMPTY")
        
        # print all the url have been visited, indicted and scraped
        elif dataType == "url_visited":
            if self.url_visited != None:
                self.url_visited.sort()
                f = open(self.FILE_URL_VISITED, 'w+')
                for url in self.url_visited:
                    print(url)
                    f.write(url + '\n')
                f.close()
            else:
                print("URL VISITED - EMPTY")
        
        # print all the url with subdomain found that will not be visit, indict or scrap
        elif dataType == "subDomain_all":
            if self.subDomain_all != None:
                self.subDomain_all.sort()
                f = open(self.FILE_SUBDOMAIN_ALL, 'w+')
                for url in self.subDomain_all:
                    print(url)
                    f.write(url + '\n')
                f.close()
            else:
                print("SUBDOMAIN ALL - EMPTY")
        
        # print all the emails found belonging to the attacked web
        elif dataType == "emails":
            if self.emails != None:
                self.emails.sort()
                f = open(self.FILE_EMAILS, 'w+')
                for email in self.emails:
                    print(email)
                    f.write(email + '\n')
                f.close()
            else:
                print("EMAIL ALL - EMPTY")
        
        # print all the url realed to files, for don't be scraped
        elif dataType == "files_url":
            if self.files_url != None:
                self.files_url.sort()
                f = open(self.FILE_URL_FILES, 'w+')
                for file_url in self.files_url:
                    print(file_url)
                    f.write(file_url + '\n')
                f.close()
            else:
                print("FILES URL ALL - EMPTY")
    
    # check if the list of all url is empty
    def is_empty_url_all(self):
        if len(self.url_all) == 0:
            return True
        else:
            return False
    
    # get the first item from the list of all urls
    def getFirst_url_all(self):
        # if the list is not empty return the first item
        if len(self.url_all) != 0:
            urlTmp = self.url_all.pop(0)
            return urlTmp
        return None
    
    # get all the url realted to the domain of the main url
    def extract_valid_urls(self, urlExtraction):
        # add the url from "url_all" array into the array of the url visited
        # and open the file to save as temporal the url in the last line of the file
        self.url_visited.append(urlExtraction)
        f = open(self.FILE_URL_VISITED, 'a+')
        f.write(urlExtraction + '\n')
        f.close()

        # dump all the HTML text into a variable to examinate
        self.html_text = self.extract_html_text(urlExtraction)
        
        # go over all links <a></a> on the page extracted
        for link in self.html_text.find_all('a'):
            # get the url of the link
            url = link.get('href')
            url = self.clean_url(url)
            self.filter_url(url)
        
    # process all url obtained to clean a leave it ready
    def clean_url(self, url):
        cleanUrl = url
        # clean the url to remove the last / if it exist in the urlTemp
        # print(cleanUrl)
        if cleanUrl != None:
            if cleanUrl.endswith("/"):
                cleanUrl = cleanUrl[:-1]
        return cleanUrl

    # process all url obtained to clean a leave it ready
    def filter_url(self, url):
        filter_url = None
        if url != None:
            if 'freecycle.org' in url:
                # detect if the url start with //www.freecycle.org
                if url.startswith("//www.freecycle.org"):
                    url = 'https:' + url
                
                filter_url = url

                # check if the url start with http header to classifly them as valid for scrap
                if filter_url.startswith('http://www.freecycle.org') or filter_url.startswith('https://www.freecycle.org') or filter_url.startswith('http://groups.freecycle.org') or filter_url.startswith('https://groups.freecycle.org'):
                    # check if the url contains "/file/" string to classify as file, then not need to be processed
                    if '/files/' in filter_url:
                        # check if the url already exist in the list of all files_urls
                        if filter_url not in self.files_url:
                            f = open(self.FILE_URL_FILES, 'a+')
                            f.write(filter_url + '\n')
                            f.close()
                            self.files_url.append(filter_url)
                    else:
                        # check if the url already exist in the list of all urls and the visited urls
                        if filter_url not in self.url_visited:
                            if filter_url not in self.url_all:
                                #print(filter_url)
                                self.url_all.append(filter_url)
                
                # check if the url start with mailto to classifly as email
                elif filter_url.startswith('mailto'):
                    mail = url[7:]
                    # check if the url already exist in the list of all emails
                    if mail not in self.emails:
                        #print(filter_url)
                        f = open(self.FILE_EMAILS, 'a+')
                        f.write(mail + '\n')
                        f.close()
                        self.emails.append(mail)
                
                # then it will be classify as sub-domain
                else:
                    # check if the url with subdomain already exist in the list of all subdomain's url
                    if filter_url not in self.subDomain_all:
                        #print("SUBDOMAIN: ", filter_url)
                        f = open(self.FILE_SUBDOMAIN_ALL, 'a+')
                        f.write(filter_url + '\n')
                        f.close()
                        self.subDomain_all.append(filter_url)
            else:
                # check if the url IS NOT from www.freecycle.org and already exist in the list of all other's url
                if url not in self.other_url:
                    f = open(self.FILE_OTHER_URL, 'a+')
                    f.write(url + '\n')
                    f.close()
                    self.other_url.append(url)

    # extract and classify Countries and Cities that work the page
    # https://www.freecycle.org/browse?noautodetect=1'
    def extractCountriesInPage(self, url):
        self.html_text = self.extract_html_text(url)
        #items = html.select("#active_country_list")
        #print(items)
        items = self.html_text.select('#active_country_list > #country_column_1 > ul > li > a')
        print("--COUNTRIES--")
        
        countries = []
        for item in items:
            print(item.get_text())
            url_ad = item.get('href')
            print(url_ad)
            countries.append(item.get_text())
            self.extractRegionsCountryInPage(url_ad)
        
        items = self.html_text.select('#active_country_list > #country_column_2 > ul > li > a')
        for item in items:
            print(item.get_text())
            url_ad = item.get('href')
            print(url_ad)
            countries.append(item.get_text())
            self.extractRegionsCountryInPage(url_ad)
        
        items = self.html_text.select('#active_country_list > #country_column_3 > ul > li > a')
        for item in items:
            print(item.get_text())
            url_ad = item.get('href')
            print(url_ad)
            countries.append(item.get_text())
            self.extractRegionsCountryInPage(url_ad)
    
    def extractRegionsCountryInPage(self, url):
        raw_html = self.simpleGet(url)
        html = BeautifulSoup(raw_html, 'html.parser')
        items = html.select('#active_regions > #region_column_1 > ul > li > a')
        print("--REGIONS--")
        #print(items)
        regions = []
        for item in items:
            #print(item.get_text())
            print(item.get('href'))
            regions.append(item.get_text())
        
        items = html.select('#active_regions > #region_column_2 > ul > li > a')
        for item in items:
            #print(item.get_text())
            print(item.get('href'))
            regions.append(item.get_text())

    def extractAdInPage(self, url):
        Ad_id = ''
        Ad_title = ''
        Ad_location = ''
        Ad_date = ''
        Ad_description = ''
        Ad_link_image = ''
        Ad_type = ''

        raw_html = self.simpleGet(url)
        html = BeautifulSoup(raw_html, 'html.parser')
        
        # to dectect if the post has been deleted
        for item in html.select("#group_box"):
            #print(item.get_text())
            if "Message not found" in item.get_text():
                print("Message not found")
        
        count = 1
        for item in html.select("#group_post > header > h2"):
            if count == 1:
                # dump ad's id
                Ad_id = item.string
            elif count == 2:
                # dump ad's title
                Ad_title = item.string
            count = count + 1
        
        #filter the title to know if the ad is a OFFER or WANTED type
        if Ad_title.startswith("OFFER"):
            Ad_type = 'OFFER'
            Ad_title = Ad_title[7:]
        elif Ad_title.startswith("WANTED"):
            Ad_type = 'WANTED'
            Ad_title = Ad_title[8:]

        for item in html.select("#post_details"):
            # dump ad's location and date
            Ad_location = item.find_next("div").get_text()
            Ad_location = Ad_location[10:]
            Ad_date = item.div.find_next("div").get_text()
            Ad_date = Ad_date[7:]
            
            # dump description and image url
            string = item.find_next_sibling("div")
            Ad_description = string.p.get_text()
            Ad_link_image = string.a.get('href')
        
        print("###")
        print("-- Ad ID --")
        print(Ad_id)
        print("-- Ad Type --")
        print(Ad_type)
        print("-- Ad Title --")
        print(Ad_title)
        print("-- Location --")
        print(Ad_location)
        print("-- Date --")
        print(Ad_date)
        print("-- Description --")
        print(Ad_description)
        print("-- Image's Ad URL --")
        print(Ad_link_image)
        print("-- Link Ad --")
        print(url)
        
    # check if the url extracted exist on the list passed by of all url extracted
    def is_in_urlAll(self, urlTemp):
        for url in self.url_all:
            if url == urlTemp:
                return True
        return False

    # check if the url extracted exist on the list of all subDomains extracted
    def is_in_subDomainAll(self, urlTemp):
        for url in self.subDomain_all:
            if url == urlTemp:
                return True
        return False
