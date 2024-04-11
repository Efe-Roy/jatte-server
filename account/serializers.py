from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=User
        fields= ['id', 'name', 'email', 'is_vendor', 'is_rider', 'is_client', 'is_admin', 'is_active', 'acc_balance', 'image']
        
class SignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['name','email','password', 'password2', 'is_vendor', 'is_rider', 'is_client', 'is_admin']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            name=self.validated_data['name'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_vendor=self.validated_data['is_vendor']
        user.is_rider=self.validated_data['is_rider']
        user.is_client=self.validated_data['is_client']
        user.is_admin=self.validated_data['is_admin']
        user.is_staff= True
        user.save()
        return user
