### Sample project working with restaurant menus and locations

# Creating Menu class and method for calculating customer bills
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

    self.start_time_string = ''
    self.end_time_string = ''


  def __repr__(self):
    if self.start_time > 12:
      self.start_time_string = str(self.start_time - 12) + ' PM'
    elif self.start_time == 12:
      self.start_time_string = str(self.start_time) + ' PM'
    else:
      self.start_time_string = str(self.start_time) + ' AM'

    if self.end_time > 12:
      self.end_time_string = str(self.end_time - 12) + ' PM'
    elif self.end_time == 12:
      self.end_time_string = str(self.end_time) + ' PM'
    else:
      self.end_time_string = str(self.end_time) + ' AM'

    return "You have chosen the {} menu.  This menu is available from {} to {}.".format(self.name, self.start_time_string, self.end_time_string)


  def calculate_bill(self, purchased_items):
    total_price = 0

    for i in range(len(purchased_items)):
      for menu_item, price in self.items.items():
        if purchased_items[i] == menu_item:
          total_price += price
      else:
        continue
    
    return "The total price of your {} items is {}.".format(self.name, total_price)


# Creating Franchise class and method for seeing menus available for given time of day
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address of this location is {}.".format(self.address)

  def available_menus(self, time):
    available_items = []

    time_string = ''
    if time > 12:
      time_string = str(time - 12) + ' PM'
    elif time == 12:
      time_string = str(time) + ' PM'
    else:
      time_string = str(time) + ' AM'
    
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_items.append(menu.name)
      else:
        continue

    return "The menus available for {} are {}.".format(time_string, available_items)


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return "You have chosen the {} business, which includes the {} franchise(s).".format(self.name, self.franchises.address)


brunch = Menu(
  'Brunch', 
  {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
  }, 
  11, 
  16
)

early_bird = Menu(
  'Early Bird',
  {
    'salumeria plate': 8.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 
    'espresso': 3.00
  },
  15,
  18
)

dinner = Menu(
  'Dinner',
  {
    'crostini with eggplant caponata': 13.00, 
    'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 
    'espresso': 3.00
  },
  17,
  23
)

kids = Menu(
  'Kids',
  {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
  },
  11,
  21
)

arepas_menu = Menu(
  "Arepas Menu",
  {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
  },
  10,
  20
)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))

first_business = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
print(arepas_place)

arepas_business = Business('Take a\' Arepa', arepas_place)
print(arepas_business)
