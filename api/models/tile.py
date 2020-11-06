class Tile():

    def __init__(self, description="", gm_notes="", guid="", index=-1, 
    lua_script="", lua_script_state="", name="", nickname=""):
        self.description = description
        self.gm_notes = gm_notes
        self.guid = guid
        self.index = index
        self.lua_script = lua_script
        self.lua_script_state = lua_script_state
        self.name = name
        self.nickname = nickname

    def getJSON(self):
         return "method not implemented"
