from bs4 import BeautifulSoup
import urllib3
import requests

request = requests.get('http://www.example.com')
if request.status_code == 404:
    print('does not exist')

url = 'https://musescore.com/user/2146376/scores/2184946'
url = 'https://musescore.com/torbybrand/scores/1463381'

# instrument 0 : piano
# TODO: pass song as argument get first result page
search_url_begin = 'https://musescore.com/sheetmusic?text='
search_url_end = '&sort=relevance&instruments=0'

http = urllib3.PoolManager()

response = http.request('GET', url)
soup = BeautifulSoup(response.data, 'html.parser')
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(response.data)


score = 'score_'
count = 0
max_scores = 0
found = True

sheets = []

# find first score
score_count = score + str(count)
img = soup.findAll("img", {"id": score_count})

score_url = ''

if len(img) > 0:
    sheets.append(img[0]['src'])
    score_url = img[0]['src']
    count += 1
else:
    print('error')

while score_url:
    tmp_score = score + str(count)
    score_url = score_url.replace(score_count, tmp_score, 1)
    score_count = tmp_score
    request = requests.get(score_url)
    if request.status_code == 404:
        score_url = ''
    count += 1
    sheets.append(score_url)

# TODO: store pngs to pdf
for sheet in sheets:
    print(sheet)

