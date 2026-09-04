time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0
parts = time_str.split(',')

for part in parts:
    part = part.strip()
    hours = 0
    minutes = 0
    seconds = 0

    if 'h' in part:
        h_idx = part.index('h')
        start = h_idx - 1
        while start >= 0 and part[start].isdigit():
            start -= 1
        start += 1  
        hours = int(part[start:h_idx])

    if 'm' in part:
        m_idx = part.index('m')
        start = m_idx - 1
        while start >= 0 and part[start].isdigit():
            start -= 1
        start += 1
        minutes = int(part[start:m_idx])

    if 's' in part:
        s_idx = part.index('s')
        start = s_idx - 1
        while start >= 0 and part[start].isdigit():
            start -= 1
        start += 1
        seconds = int(part[start:s_idx])

    total_minutes += hours * 60 + minutes + seconds // 60

print(total_minutes)
