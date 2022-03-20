from .ServiceB import ServiceB

class ServiceA():
    def functionA(self):
        oServiceB = ServiceB()
        rt = oServiceB.functionB()
        return rt
