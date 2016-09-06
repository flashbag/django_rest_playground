from rest_framework import serializers

from management.models import User, UserType, UserStatus

class UserSerializer(serializers.ModelSerializer):

	user_type = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=UserType.objects.all())
	user_status = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=UserStatus.objects.all())

	class Meta:
		model = User
		fields = (
			'id', 'email', 'username',
			'first_name', 'last_name',
			# 'date_joined',
			# 'is_staff',
			'user_type', 'user_status'
		)

