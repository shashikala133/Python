#!C:\Users\admin\PycharmProjects\pythonProject\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 's3-image-optimizer==0.1.0','console_scripts','s3-optimize'
__requires__ = 's3-image-optimizer==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('s3-image-optimizer==0.1.0', 'console_scripts', 's3-optimize')()
    )
