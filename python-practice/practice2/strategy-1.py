#-*- coding: utf-8 -*-
#行为型模式之策略模式
#策略模式将各种操作（算法）进行封装，并使他们之间可以互换：
#互换：可以动态的改变对象的操作方式
class Question(object):
    """
    问题对象，没有使用策略模式之前的作法
    """

    def __init__(self, admin=True):
        self._admin = admin


    def show(self):
        """
        根据是否是管理员显示不同的信息
        """
        if self._admin is True:
            return "show page with admin"
        else:
            return "show page with user"


if __name__=='__main__':
    q1 = Question(admin=False)
    q2 = Question(admin=True)
    print(q1.show()) 
    print(q2.show())
