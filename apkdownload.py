from bs4  import BeautifulSoup
import urllib.request
import requests
import sys

if len(sys.argv) == 2:

    package_name = sys.argv[1]

    r = requests.get('https://apkpure.com/tw/search?q='+package_name)

    if r.status_code == requests.codes.ok:

        soup = BeautifulSoup(r.text, 'html.parser')

        url_apk = soup.find('dl',class_='search-dl').find('dt').find('a')['href']

        url_apk = "https://apkpure.com"+url_apk+"/download?from=details"

        download_page = requests.get(url_apk)

        if download_page.status_code == requests.codes.ok:

            soup = BeautifulSoup(download_page.text,'html.parser')

            token_download = soup.find("a", {"id": "download_link"})['href']

            print("---Start to download "+package_name+".apk---")

            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(token_download,package_name+".apk")

            print("Download complete.")
else:
    print("python3 apkdownload.py jp.naver.line.android")

