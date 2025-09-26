from registros_ig import app
from flask import render_template,request,redirect,flash
from registros_ig.models import *
from datetime import date, datetime
from registros_ig.forms import MovementsForm, searchForm

def validarFormulario(datosFormulario):
    errores = []#se crea la lista para guardar errores
    hoy = str(date.today())
    if datosFormulario['date'] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede ir vacio")
    if datosFormulario['quantity'] == "" or float(datosFormulario['quantity']) == 0.0:
        errores.append("El monto debe ser distinto de 0 y de vacio")

    return errores


@app.route("/")
def index():
    diccionario = select_all()
    ing= select_ingreso()
    egr = select_egreso()
    sald= float(ing)+float(egr)

    return render_template("index.html",lista=diccionario,ingreso=ing,egreso=egr,saldo=sald)

@app.route("/new",methods=["GET","POST"])
def create():
    form = MovementsForm()
    if request.method == "GET":#GET
        return render_template("create.html",dataForm=form,dataURL="/new")
    else:#POST
        if form.validate_on_submit():
            insert( [ request.form['date'],request.form['concept'],request.form['quantity'] ])
            flash("Movimiento registrado correctamente !!!")
            return redirect("/")
        else:
            return render_template("create.html",dataForm=form)
        

        
    
@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method == "GET":#get
        resultado = select_by(id)
        return render_template("delete.html",data=resultado)
    else:#post
        delete_by(id)
        flash("Movimiento eliminado correctamente!!!")
        return redirect("/")
    
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    form = MovementsForm()
    if request.method == "GET": #get
        resultado = select_by(id)
        form.date.data= datetime.strptime( resultado[1], "%Y-%m-%d")
        form.concept.data=resultado[2]
        form.quantity.data= resultado[3]
        return render_template("update.html",dataForm=form,dataURL=f"/update/{id}")
    else:#post
        update_by( id,[
            form.date.data.isoformat(),
            form.concept.data,
            form.quantity.data] )
        flash("Movimiento actualizado correctamente !!!")
        
        return redirect("/")   

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    form = searchForm()
    if request.method == "GET":
        return render_template("buscar.html", dataForm=form )
    else:
        resultado = select_by_date(form.date)
        return render_template("search_result.html", resultado = select_by_date(form.date) )
