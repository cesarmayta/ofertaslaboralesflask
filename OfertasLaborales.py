import requests
from bs4 import BeautifulSoup

class OfertasLaborales:

    def __init__(self):
        self.url_principal = "https://www.computrabajo.com.pe/"

    def obtenerOfertas(self,habilidad):
        urlOfertas = self.url_principal + "trabajo-de-" + habilidad
        url = requests.get(urlOfertas)
        resultado = []
        if(url.status_code == 200):
            html = BeautifulSoup(url.text,'html.parser')
            ofertas = html.find_all('article',{'class':'box_offer'})
            listaOfertas = []
            for oferta in ofertas:
                titulo = oferta.find('a',{'class':'js-o-link fc_base'})
                empresa = oferta.find('a',{'class':'fc_base hover it-blank'})
                enlace = self.url_principal + titulo['href']
            
                dicOferta = {
                    'titulo':titulo.get_text(),
                    'empresa':empresa.get_text(),
                    'url':enlace
                }
                listaOfertas.append(dicOferta)
                
            resultado = listaOfertas
        else:
            print('error : ' + str(url.status_code))
        return resultado