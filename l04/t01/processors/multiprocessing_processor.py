import multiprocessing
import requests
import time

import os
from urllib.parse import urlparse


def download(url, i):
  start_at = time.time()

  response = requests.get(url)
  filename = os.path.basename(urlparse(url).path)

  with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)
  print(i, url, round(time.time() - start_at, 3))


def main(urls):
  processes = []
  for index, url in enumerate(urls):
    p = multiprocessing.Process(target=download, args=(url, index))
    processes.append(p)
    p.start()
  for p in processes:
    p.join()


def call(urls):
  start_at = time.time()
  main(urls)
  return round(time.time() - start_at, 3)
