from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

class MovementsForm(FlaskForm):
    date = DateField('Fecha',validators=[ DataRequired("La fecha es requerida") ])
    concept = StringField('Concepto',validators=[ DataRequired(),Length(min=4,message="Más de 4 caracteres por favor") ])
    quantity = FloatField('Monto', validators=[DataRequired("El monto es requerido y debe ser mayor a 0") ])

    submit = SubmitField('Guardar')


    def validate_date(form,field):
        if field.data > date.today():
            raise ValidationError("Fecha invalida: La fecha debe ser igual o menor a la actual")
        


class searchForm(FlaskForm):
    date = DateField("Fecha")  
    concept = StringField("Concepto") 

    submit = SubmitField("Buscar")     