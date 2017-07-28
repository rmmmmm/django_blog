from django.contrib import admin

# Register your models here.
from blog.models import Article

# class 继承自admin.ModelAdmin是为了增强admin功能


class ArticleAdmain(admin.ModelAdmin):
    # admin中默认显示一个字段title，设置list_display是为了显示其他字段
    list_display = ('title', 'content', 'date')
    # 因为是tuple所以后面加‘，’ 设置list_filter是用来根据date删选admin中的数据内容的
    list_filter = ('title', )


admin.site.register(Article, ArticleAdmain)
