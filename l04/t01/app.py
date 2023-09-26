from argparse import ArgumentParser


urls = [
  'https://hips.hearstapps.com/hmg-prod/images/russian-blue-royalty-free-image-1658451809.jpg',
  'https://as2.ftcdn.net/v2/jpg/03/15/65/77/1000_F_315657738_vX1BZfaZ5w3bU7QGnKsWmvnsYSSiG6L1.jpg',
  'https://preview.redd.it/starry-night-v0-sajy0xckvjqb1.jpg',
  'https://4kwallpapers.com/images/walls/thumbs_3t/12910.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/RedCat_8727.jpg/1200px-RedCat_8727.jpg',
]


if __name__ == '__main__':
  parser = ArgumentParser(description='Параллельная загрузка изображений')

  parser.add_argument(
    '-processor',
    metavar='processor',
    type=str,
    help='Процессоры: asyncio, multiprocessing, threading',
    default='asyncio'
  )

  args = parser.parse_args()

  print(f'{args.processor} run ...')

  if args.processor == 'threading':
    from processors.threading_processor import call
  elif args.processor == 'multiprocessing':
    from processors.multiprocessing_processor import call
  else:
    from processors.asyncio_processor import call

  print(f'{args.processor} total time:', call(urls))
