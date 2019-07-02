from django import template

# 固定写法，生成一个注册实例对象
register = template.Library()


@register.filter()  # 告诉Django的模板语言我现在注册一个自定义的filter
def add_sb(value):
    """
    给任意指定的变量添加sb
    :param value: |左边被修饰的那个变量
    :return: 修饰后的变量内容
    """
    return value + 'sb'


@register.filter()
def add_str(value, arg):
    return value + arg
