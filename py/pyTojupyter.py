# -*- coding: utf-8 -*-
#Created by DU 
#Topic : python to jupyter
#%%%
#https://github.com/gatsoulis/py2ipynb/blob/master/examples/example_spyderlike.py
#%%%
#pip install ipynb-py-convert
#%%%
import jupytext
#notebook = jupytext.read('example.py')
#jupytext.write(notebook, 'example.ipynb', fmt='.ipynb')
#%%%
import os
os.listdir('.')
os.listdir('../py/')

#%%%
mtpy = jupytext.read('../py/mtcars1.py')
mtpy
jupytext.write(mtpy, 'mtpynb.ipynb', fmt='.ipynb')
#%%%

#%%%

#%%%
