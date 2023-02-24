def get_wind_class(speed):
    result = ""
    if 1 <= speed <=4:
        result = "weak [1]"
    elif 5<= speed <=10:
        result = "moderate [2]"
    elif 11<= speed <=18:
        result = "strong [3]"
    else:
        result = "hurricane [4]"
    return result