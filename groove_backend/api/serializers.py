from rest_framework import serializers
from .models import DanceMove, UserProgress, RecommendedExercise, DanceStyle, Move, Progress

class DanceMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceMove
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'

class RecommendedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedExercise
        fields = '__all__'

# Serializer for DanceStyle
class DanceStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanceStyle
        fields = '__all__'

# Serializer for Move
class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'name', 'description', 'media_url', 'style']

# Serializer for Progress
class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['user_id', 'move', 'progress_status']