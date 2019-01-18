# Foregrounds
import numpy as np
import astropy.io as astro
import h5py
from astropy.io import fits as pyfits
#####################################################################################################################
#####################################################################################################################
###                                       Summing up hdf5 files                                                #####
###                                                                                                             ##### 
### Authors E. Guimaraes and K. Fornazier                                                                       #####
#####################################################################################################################

from astropy.table import Table
import os

def consolidar(arquivo):
 print("Iniciando")
 pathCons=arquivo
 arquivoHd5 = pyfits.open(arquivo)
 arquivoHd5.info()
 tabela=arquivoHd5[0].data;
 arquivoRaw=arquivo.split(".")[0]
 pathHd5="Con"+".hdf5"
 h5f = h5py.File(pathHd5, 'a')
 h5f.create_dataset(arquivoRaw, data=tabela)
 h5f.flush()
 h5f.close()

for root, dirs, files in os.walk("."):
    for filename in files:
	if ".fits" in filename:
	    consolidar(filename)

print(filename)



