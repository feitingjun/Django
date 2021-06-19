import uuid
from django.db import models

# 自定义模型管理类，通过他可以给模型自定义方法
class UserManage(models.Manager):
  def all(self):
    return super().all()
  def create_user(self, username):
    user = self.model()
    user.username = username
    user.save()
    return user

# 用户模型
class Users(models.Model):
  id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  sex = models.IntegerField(null=True)
  age = models.IntegerField(null=True)
  email = models.CharField(max_length=355, null=True)
  headpic = models.TextField(null=True)
  role_id = models.UUIDField()
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  create_by = models.CharField(max_length=255)
  update_by = models.CharField(max_length=255)

  # 自定义模型管理类，
  objects = UserManage()

  def save(self, *args, **kwargs):
    self.create_by = self.id
    super().save(*args, **kwargs)

  # class Meta:
    # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
    # db_table = "users"

  # 定义模型返回的数据内容，需要返回字符串
  def __str__(self):
    res =  {
      'username': self.username,
      'id': self.id,
      'sex': self.sex,
      'age': self.age,
      'email': self.email,
      'headpic': self.headpic,
      'create_at': self.create_at,
      'update_at': self.update_at,
      'create_by': self.create_by,
      'update_by': self.update_by
    }
    return str(res)