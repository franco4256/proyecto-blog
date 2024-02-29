from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'comment_detail.html', {'comment': comment})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request, 'comment_confirm_delete.html', {'comment': comment})
