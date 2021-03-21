from greeter import GreeterJames
from greeter import GreeterMark

first_greeter = GreeterJames()
second_greeter = GreeterMark()

first_greeter.change_time("Morning")
first_greeter.enters("Taisei")
first_greeter.enters("Takeshi")
first_greeter.greet()

first_greeter.change_time("Afternoon")
first_greeter.enters("Haruku")
first_greeter.greet()

first_greeter.change_time("Evening")
first_greeter.enters("Sara")
first_greeter.greet()

second_greeter.enters("Fira")
second_greeter.greet()