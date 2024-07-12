
import requests
from bs4 import BeautifulSoup
import csv

def sendmsg(message_text_url):
    bot_token = '7243297008:AAH_RWUZSxPlj94KvEybe6d1nSSIOXGgjV4'
    chat_id = '5673837951'
    urlbot = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message_text_url
        }
    response = requests.post(urlbot, json=params)
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send the message.')
    return None



def upload_file_to_gofile(file_path):
    url = 'https://store1.gofile.io/uploadFile'
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, files=files)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['data']

    return None



headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        'cache-control': "max-age=0",
        'sec-ch-ua': "\"Chromium\";v=\"118\", \"Brave\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'upgrade-insecure-requests': "1",
        'sec-gpc': "1",
        'accept-language': "en-GB,en;q=0.7",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'referer': "https://sinhalasub.lk",
        }
csv_file = "sinhalasublktvshowsall.csv"
namelast=''
endnumber= 2
endnumber2 =endnumber +1
rowdatax = []
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)

    for i in range(1, endnumber2):
        urlz = f"https://sinhalasub.lk/tvshows/page/{i}/"

        print(urlz)


        responsez = requests.get(urlz, headers=headers)
        html_contentz = responsez.text
        soupz = BeautifulSoup(html_contentz, 'html.parser')
        special_di = soupz.find("div", attrs={"id":"archive-content"})
        linksz = special_di.find_all('a')


        for linkz in linksz:
            hrefz = linkz.get('href')
            if hrefz and hrefz.startswith('https://sinhalasub.lk/tvshows/'):
                rowdata = []
                url = hrefz
                response = requests.get(url, headers=headers)
                name = hrefz[30:-19].replace('-', ' ')
                name4 = f"Name: '{name}',"
                rowdata.append(name4)
                if rowdatax and name4 == rowdatax[0]:
                    continue
                rowdatax = [name4]
                rowdata = [name4]
                html_contentz = response.text
                soupz = BeautifulSoup(html_contentz, 'html.parser')
                linksz = soupz.find_all('a')
                for linkz in linksz:
                    hrefz2 = linkz.get('href')
                    if hrefz2 and hrefz2.startswith('https://sinhalasub.lk/episodes/'):
                        url = hrefz2
                        response = requests.get(url, headers=headers)
                        namer = hrefz2[30:-1].replace('-', ' ')
                        name4r = f"| Name: '{namer}' "


                        if namelast != name4r:
                            namelast != name4r
                            rowdata.append(name4r)

                            response = requests.get(url, headers=headers)
                            from bs4 import BeautifulSoup
                            html_content = response.text
                            soup = BeautifulSoup(html_content, 'html.parser')
                            section_ids = ['download', 'download-02', 'download-03']
                            for section_id in section_ids:
                                section = soup.find(id=section_id)
                                if section:
                                    rows = section.select('tbody tr')
                                    if 'download-02' in section_id:
                                        sever = f"Severid:2"
                                        rowdata.append(sever)
                                    elif 'download-03' in section_id:
                                        sever = f"Severid:3"
                                        rowdata.append(sever)
                                    elif 'download' in section_id:
                                        sever = f"Severid:1"
                                        rowdata.append(sever)
                                    for row in rows:
                                        link = row.find('a', href=True)['href']
                                        quality = row.find('strong', class_='quality').get_text()
                                        size = row.find_all('td')[2].get_text()
                                        qualitydata =f"Quality:'{quality}'"
                                        sizedata =f"Size:'{size}'"
                                        if link and link.startswith('https://sinhalasub.lk/links/'):
                                            response0 = requests.request("GET", link, headers=headers)
                                            html_contenth = response0.text
                                            soupx = BeautifulSoup(html_contenth, 'html.parser')
                                            linkss = soupx.find_all('a')
                                            href_links = [linke['href'] for linke in linkss]
                                            for linke in href_links:
                                                if linke and linke.startswith('https://sinhalasub.lk/'):
                                                  continue
                                                elif linke and linke.startswith('https://kdj.lk/'):
                                                  continue
                                                elif linke and linke.startswith('https://t.me/gihanlakmal'):
                                                  continue
                                                else:
                                                  linkdata =(f"', Quality:'{quality}', Size:'{size}', '{linke}'")
                                                  rowdata.append(linkdata)

                print(rowdata)
                writer.writerow(rowdata)
                if i % endnumber == 0:
                  file_path = csv_file
                  upload_data = upload_file_to_gofile(file_path)
                  down = upload_data['downloadPage']
                  if upload_data:
                      print(f"data File uploaded successfully. Url:{down}")
                      message_text_url = f"data File uploaded successfully. Url:{down}"
                  else:
                      message_text_url = "data File upload failed."
                      print("data File upload failed.")
                  sendmsg(message_text_url)






