from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Question ,Choice
from django.utils import timezone 

# def question(request):
#     question = Question.objects.all()
#     data = { 'question' : question}
#     return render(request, 'polls/index.html', data)

# def get_queryset(self):
#     """
#     Return the last five published questions (not including those set to be
#     published in the future).
#     """
#     return Question.objects.filter(
#         pub_date__lte=timezone.localtime()
#     ).order_by('-pub_date')[:5]

# def choice(request, question_id):
#     question =get_object_or_404(Question, pk=question_id)
#     data ={'question': question}
#     return render(request, 'polls/detail.html', data)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
        pub_date__lte=timezone.localtime()
    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.localtime())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else :
        selected_choice.vote += 1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))