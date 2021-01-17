from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question

import logging
logger = logging.getLogger('seok')

def index(request):
    logger.info("INFO 레벨로 출력")
    """
    seok 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    sh = request.GET.get('sh', 'ac')  # 검색기준

    # 정렬
    if so == 'recommend':  # 추천순 ( 추천이 제일 많은 순서 )
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':  # 인기순 ( 댓글이 제일 많은 순서 )
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    elif so == 'comm':  # 인기순 ( 댓글이 제일 많은 순서 )
        question_list = Question.objects.annotate(num_answer=Count('comment')).order_by('-num_answer', '-create_date')
    else:  # recent 최신순 ( 최근 수정, 등록한 순서 )
        question_list = Question.objects.order_by('-create_date')

    # 조회
    # Q 함수에 사용한 subject__icontains 제목에 kw 문자열이 포함되었는지를 의미
    # filter 함수에서 모델 필드에 접근하려면 __ 를 이용하면 됨
    if kw:
        if sh == 'sj':
            question_list = question_list.filter(
                Q(subject__icontains=kw)    # 제목 검색
            ).distinct()
        elif sh == 'ct':
            question_list = question_list.filter(
                Q(content__icontains=kw)    # 내용 검색
            ).distinct()
        elif sh == 'at':
            question_list = question_list.filter(
                Q(author__username__icontains=kw)   # 글쓴이 검색
            ).distinct()
        elif sh == 'aw':
            question_list = question_list.filter(
                Q(answer__content__icontains=kw)  # 댓글 내용 검색
            ).distinct()
        else :
            question_list = question_list.filter(
                Q(subject__icontains=kw) |          # 제목 검색
                Q(content__icontains=kw) |          # 내용 검색
                Q(author__username__icontains=kw) | # 글쓴이 검색
                Q(answer__content__icontains=kw)    # 댓글 내용 검색
                # Q(answer__author__username__icontains=kw)  # 댓글 글쓴이 검색
            ).distinct()  # 중복값 제거


    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주는거
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'sh':sh}

    return render(request, 'seok/question_list.html', context)

@login_required(login_url='common:login')
def detail(request, question_id):
    """
    seok 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    if bool(request.user):
        question.hit.add(request.user)  # 조회수 증가 처리
    context = {'question': question}
    return render(request, 'seok/question_detail.html', context)