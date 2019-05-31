# from django.shortcuts import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from boards.models import Board,Topic,Post
from django.http import Http404
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.

def home(request):
    board_ob=Board.objects.all()

    return render(request,'boards/BOARDS.html',{'boardk':board_ob})

def board_topics(request,pk):
    board = Board.objects.get(pk=pk)    # get(pk=pk): shows specific board chosen when{{ done boardk.name }} in topic.html

    # try:    #this will raise Http404 error if the requested url's instance isnt available in Board
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404

    topic_sub= Topic.objects.all()
    return render(request,'boards/topic.html',{'boardk':board,'topicK':topic_sub})

# def new_topic(self):
    # return render(request,'boards/new_topic.html')

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        # subject = request.POST['subject']
        # message = request.POST['message']
        form = NewTopicForm(request.POST)
        # user = User.objects.first()  # TODO: get the currently logged in user

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
        )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    else:
        form = NewTopicForm()


    return render(request, 'boards/new_topic.html', {'board': board,'form':form})
