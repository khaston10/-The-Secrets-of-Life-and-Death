from Container import Container
from Item import Item
from ItemTypes import *
import random
from Functions import *

list_of_containers = create_containers_with_random_items(5)

for container in list_of_containers:
    print(container.get_description())