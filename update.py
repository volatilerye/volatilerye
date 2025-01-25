import glob
import tqdm
import shutil
from converter.converter import generate_html_file

markdowns = glob.glob("markdown/**/*.md", recursive=True)
files = glob.glob("markdown/**/*.*", recursive=True)

for md in tqdm.tqdm(markdowns):
    generate_html_file(md)

for file in set(files) - set(markdowns):
    shutil.copy(file, file.replace("markdown", "."))