from django import forms

from app.models import Usuario, Plan_Internet, Plan_Telefonia, Plan_Television, Comentario, Tipo_Plan


class FormEditarPerfil(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'numero', 'comuna', 'direccion', 'contrasena']

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class FormEditarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'correo', 'numero', 'comuna', 'direccion', 'contrasena','rol', 'fecha_ingreso']
        
class FormPlanInternet(forms.ModelForm):
    class Meta:
        model = Plan_Internet
        fields = '__all__'

class FormPlanTelevision(forms.ModelForm):
    class Meta:
        model = Plan_Television
        fields = '__all__'

class FormPlanTelefonia(forms.ModelForm):
    class Meta:
        model = Plan_Telefonia
        fields = '__all__'

class FormUsuarioUsername(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre']
        widgets = {
            'id': forms.HiddenInput(),
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class FiltroForm(forms.Form):
    fecha_inicio = forms.DateField(label='Fecha de inicio')
    fecha_fin = forms.DateField(label='Fecha de fin')
    tipo_servicio_choices = [('Todos', 'Todos')] + [(servicio, servicio) for servicio in ['Internet', 'Televisión', 'Telefonía']]
    tamano_plan_choices = [('Todos', 'Todos')] + [(plan.nombre, plan.nombre) for plan in Tipo_Plan.objects.all()]
    tipo_servicio = forms.ChoiceField(label='Tipo de Servicio', choices=tipo_servicio_choices)
    tamano_plan = forms.ChoiceField(label='Tamaño de Plan', choices=tamano_plan_choices)