import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
'''
** 템플릿 필터 함수를 만드는 방법
sub 함수에 @register.filter라는 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다
템플릿 필터 함수 sub는 기존값 value에서 입력으로 받은 값 arg를 빼서 반환함
** 템플릿 파일에서 템플릿 필터 파일 로드 예
{% load seok_filter %}
'''


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"] # nl2br 줄바꿈 문자를 <br>태그로 <Enter>를 한번만 눌러도
    return mark_safe(markdown.markdown(value, extensions=extensions))
'''
mark 함수는 markdown 모듈과 mark_safe 함수를 이용하여 문자열을 HTML 코드로 변환하여 반환
이 과정을 거치면 마크다운 문법에 맞도록 HTML이 만들어진다
그리고 markdown 모듈에 "nl2br", "fenced_code" 확장 도구를 설정
"nl2br"은 줄바꿈 문자를 <br> 태그로 바꿔 주므로 <Enter>를 한 번만 눌러도 줄바꿈으로 인식하고 외에
스페이스바 두번으로 줄바꿈 처리가능, "fenced_code"는 마크다운의 소스 코드 표현을 위해 적용
'''