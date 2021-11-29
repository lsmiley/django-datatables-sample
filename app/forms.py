from django import forms

from app.models import Transaction, Acctcust


class TransactionForm(forms.ModelForm):
    bill_for = forms.CharField(label="Bill For", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    issue_date = forms.DateField(label="Issue Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    due_date = forms.DateField(label="Due Date", widget=forms.DateInput(
        attrs={'class': 'form-control datepicker_input transaction', 'placeholder': 'yyyy-mm-dd'}))

    total = forms.DecimalField(label="Total", max_digits=10, decimal_places=2,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control transaction', 'placeholder': '...'}))

    status = forms.CharField(label="Status", widget=forms.TextInput(attrs={'class': 'form-control transaction'}))

    class Meta:
        model = Transaction
        fields = ['bill_for', 'issue_date', 'due_date', 'total', 'status']


class AcctcustForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['acctname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['businesssec'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['regulatory'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['created'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['address1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['address2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['city'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['state'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['country'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['wbsiteurl'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['createdby'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['modifydate'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Acctcust
        fields = '__all__'
