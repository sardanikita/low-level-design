class board_entities:
    def __init__(self, start_pos=None,end_pos=None):
        self.end_pos = end_pos
        self.start_pos = start_pos
        self.desc = None

    def get_start_pos(self):
        if self.start_pos is None:
            raise Exception ("No Start Position defined")
        return self.start_pos

    def get_end_pos(self):
        if self.end_pos is None:
            raise Exception ("No End Position defined")
        return self.end_pos

    def set_desc(self, desc):
        self.desc = desc

    def get_desc(self):
        return self.desc

