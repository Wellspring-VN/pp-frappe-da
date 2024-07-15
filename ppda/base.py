from db_service import DBService
from utils import to_snake_case, to_camel_case, output_form


class Base:
    """
    Base class to implemend every other related field
    Attributes:
      ATTRIBUTES: list of key/attribute that a given object have
      doctype: name of the doctype in Frappe server
    """

    ATTRIBUTES = ["name"]
    doctype = ""
    conn = DBService()

    def __init__(self, data):
        """
        Parameter
          data: a dictionary or equivilant data type with key,value organisation of that can be
           used to create the object
        """
        self.set_attributes(data)

    def set_attributes(self, data):
        """
        Set attribute for the object; implemend the __init__
        """
        if not data:
            return
        for key in data.keys():
            snake_key = to_snake_case(key)
            if snake_key in self.ATTRIBUTES:
                setattr(self, snake_key, data[key])

    def __repr__(self):
        string = f"\n{self.__class__.__name__}:\n"
        for each_k in self.ATTRIBUTES:
            val = getattr(self, each_k, "")
            string += str(each_k) + ": " + str(val) + "; "
        return string

    def to_json(self):
        """
        Convert the current object to json format, return the json format
        """
        result = {
            to_snake_case(key): getattr(self, key)
            for key in self.ATTRIBUTES
            if getattr(self, key, None) != None
        }
        result["doctype"] = self.doctype
        return result

    def save(self):
        """
        Update data of the object in server, if the object has not in server yet,
        create a new instance and put the object on
        """
        if not getattr(self, "name", ""):
            new_data = self.conn.insert(self.to_json())
            if new_data and new_data.get("name", ""):
                self.name = new_data["name"]
        else:
            self.conn.update(self.to_json())

    @classmethod
    def create(cls, data):
        """
        Create a new instance of the object with given data
        """
        new_doc = cls(data)
        new_doc.save()
        return new_doc

    @classmethod
    def find(
        cls,
        fields=["*"],
        filters=None,
        limit_start=0,
        limit_page_length=20,
        order_by=None,
        output="DataFrame",
    ):
        """
        Find a list of documents from the server
        """
        rows = cls.conn.get_list(
            cls.doctype, fields, filters, limit_start, limit_page_length, order_by
        )
        return output_form(cls, rows, output)

    @classmethod
    def find_all(cls, fields=["*"], output="DataFrame"):
        """
        Find all documents from the server
        """
        limit = 1000
        rows = cls.conn.get_list(cls.doctype, fields=fields, limit_page_length=limit)
        return output_form(cls, rows, output)

    @classmethod
    def find_by_id(cls, name):
        """
        Find a document by its name
        """
        return cls(cls.conn.get_doc(cls.doctype, name))

    @classmethod
    def delete_by_id(cls, name):
        """
        Delete a document by its name
        """
        cls.conn.delete(cls.doctype, name)
