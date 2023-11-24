from django import forms

from app.models import Usuario, Plan_Internet, Plan_Telefonia, Plan_Television, Comentario


class FormEditarPerfil(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'numero', 'comuna', 'direccion', 'contrasena']

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
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
