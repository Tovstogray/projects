import tkinter as tk


FONT = ('courier new', 24, 'bold')


def main():
    window_main = tk.Tk()
    window_main.title('Color Scheme')
    frame_main = tk.Frame(window_main)
    frame_main.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
    color_space = ColorCanvas(window_main)

    red_scale   = tk.Scale(frame_main, orient='horizontal', from_=0, to_=255,
                           relief=tk.RAISED, length=300, sliderlength=20, resolution=1, command=color_space.set_red)
    green_scale = tk.Scale(frame_main, orient='horizontal', from_=0, to_=255,
                           relief=tk.RAISED, length=300, sliderlength=20, resolution=1, command=color_space.set_green)
    blue_scale  = tk.Scale(frame_main, orient='horizontal', from_=0, to_=255,
                           relief=tk.RAISED, length=300, sliderlength=20, resolution=1, command=color_space.set_blue)

    red_label   = tk.Label(frame_main, text='Red')
    green_label = tk.Label(frame_main, text='Green')
    blue_label  = tk.Label(frame_main, text='Blue')

    color_space.add_scales(red_scale, green_scale, blue_scale)
    color_space.pack(side=tk.LEFT, fill=tk.BOTH)

    red_label.pack(side=tk.TOP)
    red_scale.pack(side=tk.TOP, expand=tk.YES, fill=tk.Y)
    green_label.pack(side=tk.TOP)
    green_scale.pack(side=tk.TOP, expand=tk.YES, fill=tk.Y)
    blue_label.pack(side=tk.TOP)
    blue_scale.pack(side=tk.TOP, expand=tk.YES, fill=tk.Y)

    window_main.protocol('WM_DELETE_WINDOW', window_main.destroy)
    window_main.mainloop()


class ColorCanvas(tk.Canvas):

    def __init__(self, master, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.__red_scale, self.__green_scale, self.__blue_scale = [False] * 3
        self.__t = self.create_text(10, 10, text='', anchor=tk.NW, font=FONT)
        try:
            self.__red = int(kwargs['background'][1:3], 16)
            self.__green = int(kwargs['background'][3:5], 16)
            self.__blue = int(kwargs['background'][5:], 16)
        except:
            self.__red, self.__green, self.__blue = [0] * 3

    def add_scales(self, red_scale, green_scale, blue_scale):
        self.__red_scale, self.__green_scale, self.__blue_scale = red_scale, green_scale, blue_scale

    def to_hex(self, integer):
        if integer < 16:
            return '0%s' % hex(integer)[2:]
        else:
            return '%s' % hex(integer)[2:]

    def show_hex_color(self, color_string):
        if (self.__red + self.__green + self.__blue) / 3 > 128:
            text_color = '#000000'
        else:
            text_color = '#ffffff'
        self.itemconfigure(self.__t, text=color_string, fill=text_color)

    def set_red(self, event=None):
        if self.__red_scale:
            self.__red = self.__red_scale.get()
            color_string = '#%s%s%s' % (self.to_hex(self.__red), self.to_hex(self.__green), self.to_hex(self.__blue))
            self.configure(background=color_string)
            self.show_hex_color(color_string)

    def set_green(self, event=None):
        if self.__green_scale:
            self.__green = self.__green_scale.get()
            color_string = '#%s%s%s' % (self.to_hex(self.__red), self.to_hex(self.__green), self.to_hex(self.__blue))
            self.configure(background=color_string)
            self.show_hex_color(color_string)

    def set_blue(self, event=None):
        if self.__blue_scale:
            self.__blue = self.__blue_scale.get()
            color_string = '#%s%s%s' % (self.to_hex(self.__red), self.to_hex(self.__green), self.to_hex(self.__blue))
            self.configure(background=color_string)
            self.show_hex_color(color_string)


main()
