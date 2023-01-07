import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **all_item):
        self.contents = []
        for key, value in all_item.items():
            for itr in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        draw_list = []
        if num_balls >= len(self.contents):
            return self.contents
        for i in range(num_balls):
          name=self.contents.pop(random.randrange(
            len(self.contents)))
          draw_list.append(name)
        return draw_list
            

          
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count = 0
    for _ in range(num_experiments):
        copied = copy.deepcopy(hat)
        temp_list = copied.draw(num_balls_drawn)
        success = True
        for key, value in expected_balls.items():
            if temp_list.count(key) < value:
                success = False
                break
        if success:
            final_count += 1
    return final_count/num_experiments
