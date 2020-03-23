from solution_cars import *

#cars = get_car_list('coursera_week3_cars.csv')
cars = get_car_list('test.csv')
for car in cars:
    if car.car_type == 'car':
        print('Brand: {} Ext: {}, seats: {}'.format(car.brand, car.get_photo_file_ext(), car.passenger_seats_count))
    if car.car_type == 'spec_machine':
        print('Brand: {} Ext: {}, extra: {}'.format(car.brand, car.get_photo_file_ext(), car.extra))
    if car.car_type == 'truck':
        print('Brand: {} Ext: {}, carrying: {} w: {}, h: {}, l:{}'.format(car.brand, car.get_photo_file_ext(), car.carrying, car.body_width, car.body_height, car.body_length))

print(len(cars))
