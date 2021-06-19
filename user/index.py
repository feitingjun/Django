from django.http import HttpResponse
from .models import Users
from django.views.decorators.http import require_POST, require_GET
import uuid

@require_POST
def create (req):
  username, password = req.GET.get('username'), req.GET.get('password')
  if username and password:
    info = { 
      'username': '张三',
      'password': '12345678',
      'role_id': uuid.uuid4()
    }
    user = Users.objects.create(**info)
    return HttpResponse(user)
  elif not username:
    return HttpResponse('请输入用户名')
  else:
    return HttpResponse('请输入密码')

@require_GET
def query (req):
  res = Users.objects.get(id='148821cf5c5b43d1aab8298d84f350c4')
  return HttpResponse(res)