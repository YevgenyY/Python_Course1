from solution_cars import *

cars = get_car_list('coursera_week3_cars.csv')
for car in cars:
    if car.car_type == 'truck':
        print(car.body_length)
    print(car.get_photo_file_ext())

cars = get_car_list('coursera_week3_cars_1.csv')
print(cars)
