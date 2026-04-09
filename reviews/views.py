from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Reply
from .forms import ReviewForm, ReplyForm


def review_list(request):
    reviews = Review.objects.order_by('-created_at')
    reply_form = ReplyForm()
    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'reply_form': reply_form
    })


@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.name = request.user.username
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_create.html', {'form': form})


@login_required
def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.user = request.user
            updated_review.name = request.user.username
            updated_review.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_edit.html', {
        'form': form,
        'review': review
    })


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)

    if request.method == 'POST':
        review.delete()
        return redirect('review_list')

    return render(request, 'reviews/review_delete.html', {'review': review})


@login_required
def reply_create(request, pk):
    review = get_object_or_404(Review, pk=pk)
    reviews = Review.objects.order_by('-created_at')

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.review = review
            reply.user = request.user
            reply.save()
            return redirect('review_list')
    else:
        form = ReplyForm()

    return render(request, 'reviews/review_list.html', {
        'reviews': reviews,
        'reply_form': form,
        'reply_error_review_id': review.pk
    })


@login_required
def reply_edit(request, pk):
    reply = get_object_or_404(Reply, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReplyForm(instance=reply)

    return render(request, 'reviews/reply_edit.html', {
        'form': form,
        'reply': reply
    })


@login_required
def reply_delete(request, pk):
    reply = get_object_or_404(Reply, pk=pk, user=request.user)

    if request.method == 'POST':
        reply.delete()
        return redirect('review_list')

    return render(request, 'reviews/reply_delete.html', {'reply': reply})