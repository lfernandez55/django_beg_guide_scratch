from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
         #If the request is a post process the submitted form data using the class NewTopicForm in forms.py
         #then redirect to the topics list for that board
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            # return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
         #If the request is NOT a post create a form instance using the class NewTopicForm in forms.py
        form = NewTopicForm()
    #render the page but notice that it does so passing the board object instantiated in the line above
    #also notice that this render only happens on a GET on a POST we never get here
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    print('debug')
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

def widget_tinker(request):
    board = get_object_or_404(Board, pk=2)
    form = NewTopicForm()
    return render(request, 'widget_tinker.html', {'form': form})

# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#
#     if request.method == 'POST':
#         subject = request.POST['subject']
#         message = request.POST['message']
#
#         user = User.objects.first()  # TODO: get the currently logged in user
#
#         topic = Topic.objects.create(
#             subject=subject,
#             board=board,
#             starter=user
#         )
#
#         post = Post.objects.create(
#             message=message,
#             topic=topic,
#             created_by=user
#         )
#
#         return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic p
#
#     return render(request, 'new_topic.html', {'board': board})
