# it convert mongo db dictionary to pythonic dictionary
# convert single item into dixtionary
def noteEntity(item)->dict:
    return{
        "id" : str(item["_id"]),
        "title":  item["title"],
        "desc":item["desc"],
        "important":item["important"]
    }
# convert items in noteEntity form as above function ans return list
def notesEntity(items)->list:
    return [noteEntity(item) for item in items]
