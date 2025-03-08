from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import DanceMove, UserProgress, RecommendedExercise, DanceStyle, Move, Progress
from .serializers import DanceMoveSerializer, UserProgressSerializer, RecommendedExerciseSerializer, DanceStyleSerializer, MoveSerializer, ProgressSerializer
from rest_framework import status

class DanceMoveViewSet(viewsets.ModelViewSet):
    queryset = DanceMove.objects.all()
    serializer_class = DanceMoveSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

class RecommendedExerciseViewSet(viewsets.ModelViewSet):
    queryset = RecommendedExercise.objects.all()
    serializer_class = RecommendedExerciseSerializer

# Endpoint to get all Dance Styles
class DanceStyleList(APIView):
    def get(self, request):
        dance_styles = DanceStyle.objects.all()
        serializer = DanceStyleSerializer(dance_styles, many=True)
        return Response(serializer.data)

# Endpoint to get moves by Dance Style ID
class MoveListByStyle(APIView):
    def get(self, request, style_id):
        try:
            dance_style = DanceStyle.objects.get(id=style_id)
        except DanceStyle.DoesNotExist:
            return Response({"error": "Dance style not found"}, status=status.HTTP_404_NOT_FOUND)
        
        moves = dance_style.moves.all()
        serializer = MoveSerializer(moves, many=True)
        return Response(serializer.data)

# Endpoint to update progress for a specific move and user
class ProgressUpdate(APIView):
    def post(self, request, user_id, move_id):
        try:
            move = Move.objects.get(id=move_id)
        except Move.DoesNotExist:
            return Response({"error": "Move not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Get or create a progress record for this user and move
        progress, created = Progress.objects.get_or_create(user_id=user_id, move=move)
        progress_status = request.data.get("progress_status")

        # Validate progress status
        if progress_status not in ['In Progress', 'Mastered']:
            return Response({"error": "Invalid progress status. Must be 'In Progress' or 'Mastered'."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Update progress status
        progress.progress_status = progress_status
        progress.save()

        return Response({"message": f"Progress for move '{move.name}' updated to {progress_status}."}, status=status.HTTP_200_OK)

# Endpoint to get user's progress on all moves
class UserProgress(APIView):
    def get(self, request, user_id):
        progress = Progress.objects.filter(user_id=user_id)
        progress_data = []

        for prog in progress:
            move = prog.move
            progress_data.append({
                "move": move.name,
                "style": move.style.name,
                "progress_status": prog.progress_status
            })

        return Response(progress_data)
