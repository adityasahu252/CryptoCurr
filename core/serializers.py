from rest_framework import fields, serializers
from .models import Currency_Details

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Currency_Details
        fields=['name','price','change','percent_change']