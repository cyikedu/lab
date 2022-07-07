class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        #- Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        self.__tvc = Television.MIN_CHANNEL
        # - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        self.__tvv = Television.MIN_VOLUME
        #- Create a private variable to store the TV status. The TV should start when it is off.
        self.__tvs = False

    def power(self):
        # - This method should be used to turn the TV on/off.
        # - If called on a TV object that is off, the TV object should be turned on.
        if self.__tvs == False:
            self.__tvs = True
            return True
        # - If called on a TV object that is on, the TV object should be turned off.
        if self.__tvs == True:
            self.__tvs = False
            return False

    def channel_up(self):
        # - This method should be used to adjust the TV channel by incrementing its value.
        # - It should only work for a TV that is on.
        if self.__tvs == True:
            # - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
            if self.__tvc == Television.MAX_CHANNEL:
                self.__tvc = Television.MIN_CHANNEL
            else:
                self.__tvc += 1

        return self.__tvc

    def channel_down(self):
        # - This method should be used to adjust the TV channel by decrementing its value.
        # - It should only work for a TV that is on.
        if self.__tvs == True:
            # - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
            if self.__tvc == Television.MIN_CHANNEL:
                self.__tvc = Television.MAX_CHANNEL
            else:
                self.__tvc -= 1

        return self.__tvc

    def volume_up(self):
        # - This method should be used to adjust the TV volume by incrementing its value.
        # - It should only work for a TV that is on.
        if self.__tvs == True:
            # - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
            if self.__tvv == Television.MAX_VOLUME:
                self.__tvv = self.__tvv
            else:
                self.__tvv += 1

        return self.__tvv

    def volume_down(self):
        # - This method should be used to adjust the TV volume by decrementing its value.
        # - It should only work for a TV that is on.
        if self.__tvs == True:
        # - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
            if self.__tvv == Television.MIN_VOLUME:
                self.__tvv = self.__tvv
            else:
                self.__tvv -= 1

        return self.__tvv


    def __str__(self):
        # - This method should be used to return the TV status using the format shown in the comments of main.py.
       return f'TV status: Is on = {self.__tvs}, Channel = {self.__tvc}, Volume = {self.__tvv}'

