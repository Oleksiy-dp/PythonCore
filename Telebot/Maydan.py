from datetime import date, datetime
import telebot;

#bot = telebot.TeleBot('2073824695:');



def str_to_date(v):
    return datetime.strptime(str(v), '%d.%m.%y').date()
    

def get_events():
    list_events = []
    with open('event.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = str_to_date(current_event[1])
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events


def days_between_dates(date1, date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]


events = get_events()
today = date.today()
for event in events:
    event_name = event[0]
    event_date = event[1]
    days_until = days_between_dates(event_date, today)
    print('It is {} days until {}'.format(days_until, event_name))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      for event in events:
        event_name = event[0]
        event_date = event[1]
        days_until = days_between_dates(event_date, today)
        bot.send_message(message.from_user.id, 'It is {} days until {}'.format(days_until, event_name))
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши Привет")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        

bot.polling(none_stop=True, interval=0)
