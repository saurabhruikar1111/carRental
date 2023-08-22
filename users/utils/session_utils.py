class session_data:
    def __init__(self,id,username,role="reg"):
        self.id = id
        self.username = username
        self.role = role

    def serialise(self):
        data_dict = {}
        for field in self.__dict__.keys():  # Replace with the appropriate way to access fields
            field_name = field
            data_dict[field_name] = getattr(self, field_name)
        return data_dict
    
    @classmethod
    def deserialise(cls,data_dic):
        return cls(**data_dic)
