import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number=input ("Enter your number +__: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone, "en")
req=geocoder.description_for_number(phone, "en")
print(time)
print(phone)
print(car)
print(req)