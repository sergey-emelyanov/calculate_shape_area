### Тестовое задание вычисление площади геометрических фигур  
  
  
В данной программе представлены интерфейсы для вычисления площади геометрических фигур.   
Так как важными требованиями в  ТЗ были:  
- Легкость добавления других фигур  
- Вычисление площади фигуры без знания типа фигуры

Мною было принято решение использовать абстрактный класс (Shape) , c абстрактным методом (calculate_area), что позволит легко добавлять фигуры и делать расчет площади вне зависимости от типа фигуры.

### Использование 

### Круг (Circle) 

Необходимо создать экземпляр класса Circle, после чего вычислим его площадь при помощи метода calculate_area

```python
from calculate_area.calc_area import Circle
circle = Circle(10.0)
area = circle.calculate_area()
print(f"Площадь круга {area})
```

### Треугольник(Triangle)

Необходимо создать экземпляр класса Triangle, после чего вызовем методы для вычисления площади и проверки является ли треугольник прямоугольным 
```python
from calculate_area.calc_area import Triangle
triangle = Triangle(4.0, 3.0, 5.0)
area = circle.calculate_area()
rectangular = circle.is_rectangular()
print(f"Площадь треугольника {area}")
print(f"Является прямоугольным {rectangular} ")
```


Так же определена функция print_area которая принимает любую форму 
```python
def print_area(shape):  
    print(f"Area: {shape.calculate_area()}")


cr = Circle(10.0)
tr = Triangle(4.0, 3.0, 5.0)

print_area(cr)
print_area(tr)
```


### Тесты 

Реализованы unit-тесты для класса Circle и Triangle их можно запустить в терминале командами 
```bash
python -m unittest tests.test_circle
```

```bash
python -m unittest tests.test_triangle
```

