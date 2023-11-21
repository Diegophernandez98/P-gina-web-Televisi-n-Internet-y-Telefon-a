from django import forms

from app.models import Usuario, Plan_Internet, Plan_Telefonia, Plan_Television

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
        fields = ['id', 'username']
        widgets = {
            'id': forms.HiddenInput(),
        }