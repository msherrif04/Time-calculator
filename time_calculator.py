def extract_time(time):
  time_str_components = time.split()
  time_hour_minute_str = time_str_components[0].split(":")
  
  hour_str = time_hour_minute_str[0]
  minute_str = time_hour_minute_str[1]
  
  hour = int(hour_str)
  minute = int(minute_str)
  period_of_day = None
  if len(time_str_components) > 1:
    period_of_day = time_str_components[-1]
  return (hour, minute, period_of_day)

def days_elapsed(start_hour, duration_hour):
  days_elapsed = int((start_hour + duration_hour)/24)
  return days_elapsed

def time_to_minutes(hour, minutes):
  hours_in_minutes = hour * 60
  total_minutes = hours_in_minutes + minutes
  return total_minutes

def day_of_week(start, duration):
  days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

  total_minutes = time_to_minutes(start) + time_to_minutes(duration)
  days_gone = int(total_minutes/24)
  days_count = days_gone % 7
  day = days_of_week[days_count]
  return day
  
def add_time(start, duration, given_day = None):
  start_hour, start_minute, start_period_of_day = extract_time(start)
  duration_hour, duration_minute, duration_period_of_day = extract_time(duration)
  if start_period_of_day == "PM":
    start_hour = start_hour + 12

  minutes_in_day = 1440
  minutes_at_noon = 720
  
  new_hour = (start_hour + duration_hour)%12
  new_minute = start_minute + duration_minute

  if new_minute > 60:
    new_hour = new_hour + int(new_minute/60)
    new_minute = new_minute%60
  
  start_time_in_minutes = time_to_minutes(start_hour, start_minute)
  duration_in_minutes = time_to_minutes(duration_hour, duration_minute)
  total_minutes = start_time_in_minutes + duration_in_minutes
  effective_minutes = total_minutes%minutes_in_day

  days = int(total_minutes/minutes_in_day)
  
  if effective_minutes >= minutes_at_noon:
    period_of_day = "PM"
  else:
    period_of_day = "AM"
    
  days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

  days_gone = int(total_minutes/minutes_in_day)
  days_count = days_gone % 7
  
  day = days_of_week[days_count]
  
  print (f"{new_hour}:{new_minute:02d} {period_of_day}, {days} days later", {day})

  new_time = f"{new_hour}:{new_minute:02d} {period_of_day}"
  if days == 1:
    new_time = f"{new_hour}:{new_minute:02d} {period_of_day} (next day)"
  if days > 1:
    new_time = f"{new_hour}:{new_minute:02d} {period_of_day} ({days} days later)"
    
  if given_day:
    given_day = given_day.lower()
    index_of_start_day = days_of_week.index(given_day)
    days_gone_from_given_start = index_of_start_day + days_count
    index_end_day = days_gone_from_given_start % 7
    end_day = (days_of_week[index_end_day]).capitalize()
    new_time = f"{new_hour}:{new_minute:02d} {period_of_day}, {end_day}"
    if days == 1:
      new_time = f"{new_hour}:{new_minute:02d} {period_of_day}, {end_day} (next day)"
    if days > 1:
      new_time = f"{new_hour}:{new_minute:02d} {period_of_day}, {end_day} ({days} days later)"
    
  return new_time