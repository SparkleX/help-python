from unittest.mock import MagicMock
from src.unit_test_service.ServiceA import ServiceA
from src.unit_test_service.ServiceB import ServiceB

thing = ServiceB
thing.functionB = MagicMock(return_value=3)

oServiceA = ServiceA()
rt = oServiceA.functionA()
print(rt)

#thing.method.assert_called_with(3, 4, 5, key='value')