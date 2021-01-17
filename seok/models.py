from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # 특정 사용자가 작성한 질문을 얻기 위해 some_user.author_question.all() 같은 코드를 사용할 수 있음
    # 특정 사용자가 추천한 질문을 얻기 위한 코드 some_user.voter_question.all()

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # null=True, blank=True 는 어떤 조건으로든 값을 비워둘수있음을 의미

    hit = models.ManyToManyField(User, related_name='hit_question') # 조회수 hit 필드 추가

    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 voter 필드 추가

    def __str__(self):  # 해당 메서드를 통해 해당 오브젝트가 아닌 제목으로 표시됨
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ** on_delete... Question의 상속을 받아 생성되므로 부모 삭제시 같이 삭제되도록 처리
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  # 추천인 voter 필드 추가


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 글쓴이
    content = models.TextField()  # 댓글 내용
    create_date = models.DateTimeField()  # 댓글 생성시간
    modify_date = models.DateTimeField(null=True, blank=True)  # 댓글 수정시간
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)  # 해당 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 해당 댓글이 달린 답변