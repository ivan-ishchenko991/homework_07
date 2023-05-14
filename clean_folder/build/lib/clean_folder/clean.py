import sys, os, shutil
from pathlib import *

obj = Path(sys.argv[1])
# obj = Path(r'd:\Sorted')
if not Path(fr'{obj}\images').is_dir():
    os.mkdir(fr'{obj}\images')
img = Path(fr'{obj}\images')
if not Path(fr'{obj}\documents').is_dir():
    os.mkdir(fr'{obj}\documents')
doc = Path(fr'{obj}\documents')
if not Path(fr'{obj}\audio').is_dir():
    os.mkdir(fr'{obj}\audio')
muz = Path(fr'{obj}\audio')
if not Path(fr'{obj}\archives').is_dir():
    os.mkdir(fr'{obj}\archives')
arch = Path(fr'{obj}\archives')
if not Path(fr'{obj}\video').is_dir():
    os.mkdir(fr'{obj}\video')
vid = Path(fr'{obj}\video')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
map = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    map[ord(c)] = l
    map[ord(c.upper())] = l.upper()

def sorting(link):
    result = [[], [], [], [], []]
    file_ext = set()
    unknown_ext = set()
    for el in link.iterdir():
        if el.name in {'images', 'documents', 'audio', 'archives', 'video'}:
            continue
        if el.is_dir():
            sorting(el)
        if el.is_file():
            if el.suffix in {'.jpeg', '.png', '.jpg', '.svg'}:
                result[0].append(el.name)
                file_ext.add(el.suffix)
                shutil.move(el, img)
            elif el.suffix in {'.avi', '.mp4', '.mov', '.mkv'}:
                result[1].append(el.name)
                file_ext.add(el.suffix)
                shutil.move(el, vid)
            elif el.suffix in {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'}:
                result[2].append(el.name)
                file_ext.add(el.suffix)
                shutil.move(el, doc)
            elif el.suffix in {'.mp3', '.ogg', '.wav', '.amr'}:
                result[3].append(el.name)
                file_ext.add(el.suffix)
                shutil.move(el, muz)
            elif el.suffix in {'.zip', '.gz', '.tar'}:
                result[4].append(el.name)
                file_ext.add(el.suffix)
                shutil.unpack_archive(el, f'{arch}\{el.stem}')
                os.remove(el)
            else:
                unknown_ext.add(el.suffix)
    for i in result:
        print(i)
    print(file_ext)
    print(unknown_ext)
            
sorting(obj)

def remove_empty_dirs(path: str|Path) -> int:
     for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            remove_empty_dirs(os.path.join(root, dir))
        if not dirs and not files:
            os.rmdir(root)

remove_empty_dirs(obj)

def normalize(link):
    for el in link.iterdir():
        if el.is_dir():
            normalize(el)
        if el.is_file():
            new_file = (el.stem).translate(map) + el.suffix
            for i in new_file:
                if i == '\.':
                    continue
                if i == '\W':
                    a = str.maketrans(f'{i}', '_')
                    new_file = str.translate(i, a)
            el.rename(link / new_file)

normalize(obj)