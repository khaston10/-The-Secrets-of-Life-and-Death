
from MapSettings import *
from Materials import *
from ItemTypes import *
from Functions import *

picks = Picks(assigned=True, item_type="picks", material="steel", condition="new")

print(picks.get_description())
check_to_see_if_item_should_age(picks, probability_that_item_will_age, item_condition)
print(picks.get_description())
check_to_see_if_item_should_age(picks, probability_that_item_will_age, item_condition)
print(picks.get_description())
check_to_see_if_item_should_age(picks, probability_that_item_will_age, item_condition)
print(picks.get_description())