# python imports
import math

# project imports
from pycraft.objects.character import Character
from pycraft.objects.storage import Storage


class Player(Character):
    def __init__(self, config):
        super(Player, self).__init__(config)
        # Velocity in the y (upward) direction.
        self.dy = 0
        # A dict of player blocks with their respective quantities
        self.inventory = Storage()
        self.inventory.store_item(0, 'Brick', 5)
        self.inventory.store_item(1, 'Grass', 7)
        self.inventory.store_item(2, 'WeakStone', 10)
        self.inventory.store_item(3, 'Sand', 5)

        self.current_item = 'Brick'
        self.current_item_index = 0

    def get_block(self):
        item = self.inventory.retrieve_item(self.current_item)
        self.switch_inventory(self.current_item_index)
        if isinstance(item, dict):
            return item['item']
        return None

    def switch_inventory(self, index):
        """
        Change selected element in the inventory
        :param index:integer
        :return:None
        """
        self.current_item_index = index
        self.current_item = self.inventory.get_item_name(self.current_item_index)

    def get_sight_vector(self):
        """Returns the current line of sight vector indicating the direction the
        player is looking.
        """
        x, y = self.rotation
        # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
        # is 1 when looking ahead parallel to the ground and 0 when looking
        # straight up or down.
        m = math.cos(math.radians(y))
        # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
        # looking straight up.
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return dx, dy, dz
