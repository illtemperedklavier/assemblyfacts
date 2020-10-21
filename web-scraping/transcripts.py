
import requests
from bs4 import BeautifulSoup

def scrape_transcript(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    p = soup.find('p')
    text_by_speaker = {}

    name = ''
    for p in paragraphs:
        text = p.getText()
        attributes = p.attrs
        #print(text)
        if attributes.get('class'):
            #print(attributes)
            if 'speakerStart' in attributes.get('class'):
                #print('speaker Start')
                name = text.split(':')[0]

                para = ''.join(text.split(':')[1:])
                #print (name)
                #print(para)
                #print("\n")
            else:
                para = text
        else:
            para = text

        if text_by_speaker.get(name, None) == None:
            text_by_speaker[name] = [para]

        else:
            text_by_speaker.get(name).append([para])
    
    return text_by_speaker