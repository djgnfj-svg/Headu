from rest_framework import serializers

from ..ER_API_utils import get_ER_api_data

from ..models import ER_Base_Model

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = ER_Base_Model
		# fields = ('__all__')
		exclude = ("id",)

#todo postman으로 실험하기
class UserDataCreateSerializer(serializers.Serializer):
	nickname = serializers.CharField()
	remove_password = serializers.CharField()
	memo = serializers.CharField()

	def create(self, request, data, commit=True):
		instance = ER_Base_Model()
		instance.nickname = data.get("nickname", None)
		instance.remove_password = data.get("remove_password", None)
		instance.memo = data.get("memo", None)

		get_ER_api_data(instance)

		return instance
#전체적인과정

# -> 클라이언트에서 유저네임을 입력한다.
# -> 그데이터를 가지고 createsirializer에서 하나 생성한다 ()
# -> 그데이터를 리턴해준다.