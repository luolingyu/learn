#-*- coding: utf-8 -*-


import random
import abc

#两种类型的课程
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


#两种类型的虚拟机
class LinuxVm(object):
    """
    Linux虚拟机
    """
    def start(self):
        return "Linux vm running"


class MacVm(object):
    """
    Mac osx 虚拟机
    """
    def start(self):
        return "Mac OSX vm running"


class Factory(metaclass=abc.ABCMeta):
    #抽象工厂类,现在工厂类不能创建课程，还能创建虚拟机了
    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass


class BasicCourseFactory(Factory):
    #基础课程工厂类
    def create_course(self):
        return BasicCourse()

    def create_vm(self):
        return LinuxVm()


class ProjectCourseFactory(Factory):
    #项目课程工厂类
    def create_course(self):
        return ProjectCourse()

    def create_vm(self):
        return MacVm()


def get_factory():
    #随机获取一个工厂类
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


#random.choice()返回一个列表，元组和字符串的随机项
if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    vm = factory.create_vm()
    print(course.get_labs())
    print(vm.start())
    print(course.get_labs())
