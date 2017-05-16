import json
from datetime import datetime
import email.utils
import calendar

def parseTitle(title):
    parsed_title = ""
    for word in title.lower().split(" "):
        parsed_title += word[0]
    return parsed_title      
    
def parseDate(date):
    """date format is YYYY-MM-DD"""
    day = date[8:10]
    year = date[2:4]
    month = calendar.month_abbr[int(date[5:7])].lower()
    return day + month + year
    
def generateUrl(date, title):
    host_path = "http://koalacoder.com/cadasta-blog/#post_"
    parsed_date = parseDate(date)
    parsed_title = parseTitle(title)
    url_feed = host_path + parsed_date + parsed_title
    return url_feed
    
def applyXmlSyntax(item):
    """Item is a list. Each list entry is a xml item tag. The order of tags in list is: [title, date, description, topics, url_feed]"""
    
    return ("\n<item>\n" +
                "<title>%s</title>\n" % item[0] +
                "<pubDate>%s</pubDate>\n" % item[1] +
                "<description>%s</description>\n" % item[2]+
                "<category>%s</category>\n" % item[3] +
                "<link>%s</link>\n" % item[4] +
                "<guid>%s</guid>\n" % item[4] +
            "</item>\n")             

def generateXmlBody():
    blog_content = json.load(open("./data.json"))
    feeds_info = blog_content["content"]
    xml_body = ""
    for feed in feeds_info:
        dt = datetime.strptime(feed["date"], "%Y-%m-%d")
        date = email.utils.format_datetime(dt) # RFC 2822 datetime
        title = feed["title"]
        description = feed["summary"][0:150]+ "..."
        topics = ', '.join(feed["topics"])
        url_feed = generateUrl(feed["date"], title)
        xml_item = [title, date, description, topics, url_feed]
        xml_body += applyXmlSyntax(xml_item)
    return xml_body

xml = open("intro.xml", "r")
if xml.mode == "r":
    intro = xml.read().strip();
xml.close()

# write new xml file    
xmlFile = open("rss.xml", "w+")
body = generateXmlBody()
xmlFile.write("%s\n%s\n</channel>\n</rss>" % (intro, body))
xmlFile.close()
