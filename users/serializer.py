from rest_framework import serializers
from .models import AddBookModel, AddLibraryModel, CheckInModel, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','fname','lname','email','password','usertype','library_name','dob']
        # extra_kwargs = {
        #     'password':{'write_only':True}
        # }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class AddLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddLibraryModel
        fields = ['id','name','street','city','state','zip4']

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBookModel
        fields = ['id','name','description','author','publisher','department','price','quantity']

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckInModel
        fields = ['id','bookId', 'name','description','author','publisher', 'department','price','quantity',  'libraryname','userId','status']


        
   