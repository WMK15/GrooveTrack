from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DanceMoveViewSet, UserProgressViewSet, RecommendedExerciseViewSet


router = DefaultRouter()
router.register(r'dance-moves', DanceMoveViewSet)
router.register(r'user-progress', UserProgressViewSet)
router.register(r'recommended-exercises', RecommendedExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
        # Get all Dance Styles
    path('dance_styles/', views.DanceStyleList.as_view(), name='dance-style-list'),

    # Get moves for a specific dance style
    path('moves/<int:style_id>/', views.MoveListByStyle.as_view(), name='move-list-by-style'),

    # Update progress for a specific move and user
    path('progress/<int:user_id>/move/<int:move_id>/', views.ProgressUpdate.as_view(), name='progress-update'),

    # Get the user's progress on all moves
    path('progress/<int:user_id>/', views.UserProgress.as_view(), name='user-progress'),
]