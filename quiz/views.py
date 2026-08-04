"""
==============================================================================
QUIZ VIEWS
Handles quiz catalogs, interactive questions, and score calculations.
==============================================================================
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice, QuizAttempt

def quiz_list_view(request):
    """Catalog listing of available privacy quizzes."""
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})

@login_required
def quiz_detail_view(request, quiz_id):
    """Interactive quiz view processing user choices."""
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                try:
                    choice = Choice.objects.get(id=selected_choice_id)
                    if choice.is_correct:
                        score += question.points
                except Choice.DoesNotExist:
                    pass
        
        QuizAttempt.objects.create(user=request.user, quiz=quiz, score=score)
        return render(request, 'quiz/result.html', {'quiz': quiz, 'score': score})

    return render(request, 'quiz/detail.html', {'quiz': quiz, 'questions': questions})
