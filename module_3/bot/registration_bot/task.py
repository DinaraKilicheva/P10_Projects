class Chat:
    def __init__(self, id, fullname, language_code):
        self.id = id
        self.fullname = fullname
        self.language_code = language_code

    def get_attrs_as_dict(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "language_code": self.language_code
        }


class Task:
    def __init__(self, chat_id, name, created_at):
        self.chat_id = chat_id
        self.name = name
        self.created_at = created_at

    def get_attrs_as_dict(self):
        return {
            "chat_id": self.chat_id,
            "name": self.name,
            "created_at": self.created_at
        }


class Student:
    def __init__(self, first_name, last_name, phone, age, language, course):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.age = age
        self.language = language
        self.course = course

    def get_attrs_as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "age": self.age,
            "language": self.language,
            "course": self.course
        }
