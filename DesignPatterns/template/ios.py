
from abc import ABCMeta, abstractclassmethod


class Compiler(metaclass=ABCMeta):
    @abstractclassmethod
    def collect_source(self):
        pass

    @abstractclassmethod
    def compile_to_object(self):
        pass

    @abstractclassmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()


class iOSCompiler(Compiler):
    def collect_source(self):
        print('Collecting swift source code')

    def compile_to_object(self):
        print('Compiling swift code to LLVM bitcode')

    def run(self):
        print('Program running on runtime environment')


if __name__ == '__main__':
    ios = iOSCompiler()
    ios.compile_and_run()
