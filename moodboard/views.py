from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from actions.utils import create_action
import redis
import os
from django.conf import settings

# # connect to redis
r = redis.from_url(os.environ.get("REDIS_URL"))
# r = redis.StrictRedis(host=settings.REDIS_HOST,
#                       port=settings.REDIS_PORT,
#                       db=settings.REDIS_DB)


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            create_action(request.user, 'added', new_item)
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'moodboard/image/create.html',
                  {'section': 'moodboard',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    # increment total image views by 1
    total_views = r.incr('image:{}:views'.format(image.id))
    # increment image ranking by 1
    r.zincrby('image_ranking', 1, image.id)
    return render(request,
                  'moodboard/image/detail.html',
                  {'section': 'moodboard',
                   'image': image,
                   'total_views': total_views})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})



@login_required
def image_list(request):
    moodboard = Image.objects.filter(user=request.user)
    paginator = Paginator(moodboard, 18)
    page = request.GET.get('page')
    try:
        moodboard = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        moodboard = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        moodboard = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'moodboard/image/list_ajax.html',
                      {'section': 'moodboard', 'moodboard': moodboard})
    return render(request,
                  'moodboard/image/list.html',
                   {'section': 'moodboard', 'moodboard': moodboard})


@login_required
def image_ranking(request):
    # get image ranking dictionary
    image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[:100]
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most viewed images
    most_viewed = list(Image.objects.filter(
                           id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    return render(request,
                  'moodboard/image/ranking.html',
                  {'section': 'moodboard',
                   'most_viewed': most_viewed})
