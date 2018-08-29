#-*- coding: utf-8 -*-


import random
import abc


class BasicCourse(object):
    #基础课程
    def get_labs(self):
        return "basic_course: labs"

    def __str__(self):
        return "BasicCourse"


class ProjectCourse(object):
    #项目课

    def get_labs(self):
        return "Project_course: labs"

    def __str__(self):
        return "ProjectCourse"


class Factory(metaclass=abc.ABCMeta):
    #抽象工厂类
    @abc.abstractmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    #基础课程工厂类
    def create_course(self):
        return BasicCourse()


class ProjectCourseFactory(Factory):
    #项目课程工厂类
    def create_course(self):
        return ProjectCourse()


def get_factory():
    #随机获取一个工厂类
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


#random.choice()返回一个列表，元组和字符串的随机项
if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_labs())
