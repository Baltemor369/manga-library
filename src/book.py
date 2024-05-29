class Book:
    def __init__(self, ref:str, name:str="", author:str="", tome:str="", read_status:bool=False, family:list[str]=[]) -> None:
        self.ref = ref
        self.name = name
        self.author = author
        self.tome = tome
        self.read_status = bool(read_status)
        self.family = family

    def info(self):
        return self.ref + " " + self.name + " " + self.author + " " + self.tome + " " + self.family