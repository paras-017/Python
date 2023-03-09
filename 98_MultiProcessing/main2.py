import concurrent.futures
import requests


def downloadingFile(url, name):
  print(f'started downloading {name}')
  response = requests.get(url)
  open(f'files/files{name}.jpg', 'wb').write(response.content)
  print(f"finishes downloading {name}")

urls = "https://picsum.photos/2000/3000"


with concurrent.futures.ProcessPoolExecutor() as executor:
    l1= [urls for i in range(60)]
    l2= [i for i in range(60)]
    results = executor.map(downloadingFile, l1,l2)
    for r in results:
        print(r)
        
        