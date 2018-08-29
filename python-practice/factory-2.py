#-*- coding: utf-8 -*-


import random
import abc


class BasicCourse(object):
    #�����γ�
    def get_labs(self):
        return "basic_course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    #��Ŀ��

    def get_labs(self):
        return "Project_course: labs"

    def __str__(self):
        return "ProjectCourse"


class Factory(metaclass=abc.ABCMeta):
    #���󹤳���
    @abc.abstractmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    #�����γ̹�����
    def create_course(self):
        return BasicCourse()


class ProjectCourseFactory(Factory):
    #��Ŀ�γ̹�����
    def create_course(self):
        return ProjectCourse()


def get_factory():
    #�����ȡһ��������
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


#random.choice()����һ���б�Ԫ����ַ����������
if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_labs())
