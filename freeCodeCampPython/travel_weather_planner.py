distance_mi = 0
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if not distance_mi or isinstance(distance_mi, str):
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike:
        print(True)
    else:
        print(False)
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
