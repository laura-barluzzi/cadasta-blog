from datetime import datetime
import codecs
import email.utils
import json
import markdown


def parse_url_title(title):
    parsed_title = ''.join(word[0] for word in title.lower().split(' '))
    return parsed_title


def parse_url_date(date):
    """date format is YYYY-MM-DD"""
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    parsed_date = date_obj.strftime("%d%b%y").lower()
    return parsed_date


def generate_url(date, title):
    url_date = parse_url_date(date)
    url_title = parse_url_title(title)
    url_feed = ("http://koalacoder.com/cadasta-blog"
                "/#post_{date}{title}".format(date=url_date, title=url_title))
    return url_feed


def apply_xml_syntax(item):
    """Item is a list. Each list entry is a xml item tag. The order of tags in list is: [title, date, description, topics, url_feed]"""

    return ("\n<item>\n"
            "<title>{title}</title>\n"
            "<pubDate>{date}</pubDate>\n"
            "<description>{description}</description>\n"
            "<category>{topics}</category>\n"
            "<link>{link}</link>\n"
            "<guid>{guid}</guid>\n"
            "</item>\n".format(title=item[0], date=item[1], description=item[2],
                               topics=item[3], link=item[4], guid=item[4]))


def parse_to_rfc_2822_format(date):
    dt = datetime.strptime(date, "%Y-%m-%d")
    date = email.utils.format_datetime(dt)  # RFC 2822 datetime
    return date


def convert_markdown_to_html(post_text):
    html_text = markdown.markdown(post_text)
    html = "<![CDATA[{post}]]>".format(post=html_text)
    return html


def generate_xml_body():
    with codecs.open("./data.json", "r", "utf-8") as file_object:
        blog_content = json.load(file_object)
        feeds_info = blog_content["content"]
    xml_body = ""
    for feed in feeds_info:
        date = parse_to_rfc_2822_format(feed["date"])
        title = feed["title"]
        description = convert_markdown_to_html(feed["summary"])
        topics = ', '.join(feed["topics"])
        url_feed = generate_url(feed["date"], title)
        xml_item = [title, date, description, topics, url_feed]
        xml_body += apply_xml_syntax(xml_item)
    return xml_body


if __name__ == '__main__':

    with codecs.open("intro.xml", "r", "utf-8") as intro_xml:
        intro = intro_xml.read().strip()

    with codecs.open("rss.xml", "w", "utf-8") as rss_xml:
        body = generate_xml_body()
        rss_xml.write("%s\n%s\n</channel>\n</rss>" % (intro, body))