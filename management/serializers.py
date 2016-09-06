from rest_framework import serializers

from management.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
        	'id', 'email', 'username',
        	'first_name', 'last_name',
        	# 'date_joined',
        	# 'is_staff',
        	'user_type', 'user_status'
        )

