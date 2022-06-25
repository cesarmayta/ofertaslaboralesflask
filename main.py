from flask import Flask,request,render_template
from OfertasLaborales import OfertasLaborales


app = Flask(__name__)

@app.route('/')
def index():
    habilidad = request.args.get('habilidad','python')
    listaMenu = ['Python','React','NodeJs']
    """listaOfertas = [
        {
            "titulo":"backend developer con python y flask",
            "empresa":"banco de credito",
            "url":"https://viabcp.com"
        },
         {
            "titulo":"frontend developer con react",
            "empresa":"ripley",
            "url":"https://www.ripley.com.pe"
        },
         {
            "titulo":"backend con NodeJs",
            "empresa":"Linio",
            "url":"https://www.linio.com.pe"
        }
    ]"""
    ofertas = OfertasLaborales()
    listaOfertas = ofertas.obtenerOfertas(habilidad)

    context = {
        "menus":listaMenu,
        "ofertas":listaOfertas
    }
    return render_template('index.html',**context)

app.run(debug=True)