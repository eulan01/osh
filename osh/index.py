import requests
import img2pdf
def get_img():
    header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.3.954 (beta) Yowser/2.5 Safari/537.36'
    }
    img_list = []
    for i in range(1,49):
        url = f'https://recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url, headers=header)
        response = req.content
        with open(f'osh{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'osh{i}.jpg')

    with open('osh/name.pdf','wb') as f:
        f.write(img2pdf.convert(img_list))
get_img()