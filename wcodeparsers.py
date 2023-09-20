def parse_direction(dir):
    if (45 <= dir < 135):
        return 'east'
    if (135 <= dir < 225):
        return 'south'
    if (225 <= dir < 315):
        return 'west'
    return 'north'

def parse_weathercode(wc):
    match(wc):
        case 0:
            return 'The sky is clear'
        case 1:
            return 'The sky is mainly clear'
        case 2:
            return 'The sky is partly cloudy'
        case 3:
            return 'The weather is overcast'
        case 45 | 48:
            return 'It\'s foggy outside. Perfect time for a walk!'
        case 51 | 53 | 55 | 56 | 57:
            return 'It\'s drizzling out there'
        case 61 | 63 | 65 | 80 | 81 | 82:
            return 'The weather is rainy'
        case 71 | 73 | 75 | 77 | 85 | 86:
            return 'The weather is snowy'
        case 95 | 96 | 99:
            return 'It\'s thunderstorm'

