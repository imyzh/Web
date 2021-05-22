# Django的安装
    pip install django

# 创建项目
    django-admin.py startproject project

# 创建APP
    django-admin.py startapp app

# 创建模型
    class Test(models.Model):
        name = models.CharField(max_length=20)

# 模型变更
    python manage.py makemigrations

# 创建表结构
    python manage.py migrate
    
# 创建超级用户
    python manage.py createsuperuser
