class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand.lower()
        self.photo_file_name = photo_file_name

        try:
            self.carrying = float(carrying)
        except:
            self.carrying = float(0)

    def get_photo_file_ext(self):
        extension = None

        #print('Filename: {}'.format(self.photo_file_name))
        
        try:
            tmp = self.photo_file_name.split('.')
            extension = tmp[1] if len(tmp) > 1 else ''
        except:
            extension = ''

        #print('EXT: {}'.format(extension))
        return extension

class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except:
            self.passenger_seats_count = int(0)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        whl = body_whl.split('x')
        #print('WHL: {}'.format(whl))
        try:
            self.body_width = float(whl[0])
            self.body_height = float(whl[1])
            self.body_length = float(whl[2])
        except:
            self.body_width = self.body_height = self.body_length = float(0)

        #print('W: {} H: {} L: {}'.format(self.body_width, self.body_height, self.body_length))


    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def generate_vehicle(car_type, brand='', photo_file_name='', carrying=float(0), passenger_seats_count=0, body_whl='', extra=''):
    cartypes = ('car', 'truck', 'spec_machine')
    vehicle = None

    if car_type in cartypes:
        if car_type == 'car':
            vehicle = Car(brand, photo_file_name, carrying, passenger_seats_count)
        if car_type == 'truck':
            vehicle = Truck(brand, photo_file_name, carrying, body_whl)
        if car_type == 'spec_machine':
            vehicle = SpecMachine(brand, photo_file_name, carrying, extra)
    else:
        #print('Wrong vehicle type {}'.format(cat_type))
        pass

    return vehicle

import csv
def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car_type, brand, seats_count_str, photo_file_name, body_whl, carrying_str, extra = ('', '', '', '', '', '', '') 
                car_type, brand, seats_count_str, photo_file_name, body_whl, carrying_str, extra = row


                passenger_seats_count = 0 if (seats_count_str  == '') else int(seats_count_str)
                carrying = 0 if (carrying_str == '') else float(carrying_str)

                vehicle = generate_vehicle(car_type.lower(), brand, photo_file_name, carrying, passenger_seats_count, body_whl, extra)

                if vehicle != None:
                    car_list.append(vehicle)
                #else:
                #    print('Oops {}'.format(car_type))

            except ValueError as err:
                #print("ValueError: {}\n{}".format(err, row))
                pass

    return car_list

'''
cars = get_car_list('coursera_week3_cars.csv')

print(len(cars))
print(cars[0].passenger_seats_count)
print(cars[1].get_body_volume())
for car in cars:
    #print('Type: {}, extension: {}'.format(type(car)), car.get_photo_file_ext())
    car.get_photo_file_ext()
'''
