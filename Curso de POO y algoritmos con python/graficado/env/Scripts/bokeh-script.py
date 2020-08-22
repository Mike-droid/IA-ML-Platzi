#!"c:\users\migue\desktop\cursos\cursosplatzi\inteligencia artificial y machine learning\curso de poo y algoritmos con python\graficado\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==2.1.1','console_scripts','bokeh'
__requires__ = 'bokeh==2.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==2.1.1', 'console_scripts', 'bokeh')()
    )
