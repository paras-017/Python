import multiprocessing
import requests


def downloadingFile(url, name):
  print(f'started downloading {name}')
  response = requests.get(url)
  open(f'files/files{name}.jpg', 'wb').write(response.content)
  print(f"finishes downloading {name}")

if __name__ == '__main__':
    urls = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
    # downloadingFile(urls, i)
        p = multiprocessing.Process(target=downloadingFile, args=[urls,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()