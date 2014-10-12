from django import forms


map_pyver = (
    ('2.7.8', 'Python 2.7.8'),
    ('3.4.2', 'Python 3.4.2'),
)

map_rubyver = (
    ('1', 'Ruby dummy 1'),
    ('2', 'Ruby dummy 2'),
)

class ProjectEnvForm(forms.Form):

    team_name = forms.CharField(
            max_length = 20,
            required=True,
            label="Team Name",
            )

    project_name = forms.CharField(
            max_length = 20,
            required=True,
            label="Project Name",
            )

    lang = forms.CharField(
            max_length = 20,
            required=True,
            label="Language"
            )

    ver = forms.CharField(
            max_length = 20,
            required=True,
            label="Language Version"
            )


   

