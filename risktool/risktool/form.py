from django import forms

class mainform(forms.Form):
    risk=forms.CharField()#required=False
    riskdesc = forms.CharField()
    risksol = forms.CharField()
    consequence = forms.IntegerField()
    likelihood = forms.IntegerField()

    def changed_risk(self):
        pass