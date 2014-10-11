from django import forms


map_pyver = (
    ('2.7.8', 'Python 2.7.8'),
    ('3.4.2', 'Python 3.4.2'),
)

class PyVerForm(forms.Form):
    select_pyver = forms.ChoiceField(
        required=True,
        choices = map_pyver,
        label=""
    )
