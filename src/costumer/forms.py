from store.models import Address
from django.forms import ModelForm


class AddAddressForm(ModelForm):
    class Meta:
        model=Address
        fields = "__all__"