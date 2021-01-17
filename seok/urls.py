from django.urls import path
from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'seok' # namespace 앱이 관리하는 독립된 공간

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),            # localhost:8000/pybo/ <- 기본 URL
    path('<int:question_id>/', base_views.detail, name='detail'),                                    # 글 상세 보기

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),                    # 글 생성
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),  # 글 수정
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),  # 글 삭제

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),  # 답변 생성
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),    # 답변 수정
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),    # 답변 삭제

    # comment_views.py
    path('comment/create/question/<int:question_id>/',
         comment_views.comment_create_question, name='comment_create_question'),    # 답변-질문 생성
    path('comment/modify/question/<int:comment_id>/',
         comment_views.comment_modify_question, name='comment_modify_question'),    # 답변-질문 수정
    path('comment/delete/question/<int:comment_id>/',
         comment_views.comment_delete_question, name='comment_delete_question'),    # 답변-질문 삭제
    path('comment/create/answer/<int:answer_id>/',
         comment_views.comment_create_answer, name='comment_create_answer'),        # 답변-질문-답변 생성
    path('comment/modify/answer/<int:comment_id>/',
         comment_views.comment_modify_answer, name='comment_modify_answer'),        # 답변-질문-답변 수정
    path('comment/delete/answer/<int:comment_id>/',
         comment_views.comment_delete_answer, name='comment_delete_answer'),        # 답변-질문-답변 삭제

    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),

]