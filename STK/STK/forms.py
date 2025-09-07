from django import forms
from STK.models import Users

Rol_Choises=[
   
    ("user","Usuario"),          
    ("admin","Administrador"),         
]
Status_Choises=[
    ("Activo","Activo"),
    ("Inactivo","Inactivo")
]

class UsersForm(forms.ModelForm):
    rol=forms.ChoiceField(choices=Rol_Choises,required=True,initial='user')
    status=forms.ChoiceField(choices=Status_Choises,required=True,initial='Activo')

    class Meta:
        model= Users
        fields=["name","plan_mensual","email","password","rol","status"]
        widgats={
            "password":forms.PasswordInput(render_value=True),
        }

