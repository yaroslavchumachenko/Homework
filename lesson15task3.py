# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channel_list: list):
        self.channel_list = channel_list
        self.channel = 1
    

    def first_channel(self):
        self.channel = 1
        return self.channel_list[0]
    
    def last_channel(self):
        self.channel = len(self.channel_list)
        return self.channel_list[-1]

    def turn_channel(self, your_channel: int):
        self.channel = your_channel
        return self.channel_list[your_channel-1]
    
    def next_channel(self):
        self.channel += 1
        return self.channel_list[self.channel-1]


    def previous_channel(self):
        self.channel -= 1
        return self.channel_list[self.channel-1]
    
    def current_channel(self):
        return self.channel_list[self.channel-1]
    
    def exists(self, arg):
        if type(arg) == int:
            if arg > len(self.channel_list) or arg <= 0:
                return "No"  
            else:
                return "Yes"
        elif type(arg) == str:
            for i in self.channel_list:
                if arg in self.channel_list:
                    return "Yes"
                else:
                    return "No"

    

    



controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.exists(4) == "No"

assert controller.exists("BBC") == "Yes"
