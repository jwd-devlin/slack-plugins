

class CreateMovieMessage:

    def __init__(self):
        self._linebreak = "\n>"
        self._list = "- "
        self._generic_message = " Films this week at -> :"

    def create_message(self, theater_films_dic):
        new_message = ""
        for theater in theater_films_dic.keys():
            title = self._generic_message + theater + self._linebreak
            new_message = title
            for film in theater_films_dic[theater]:
                new_message = new_message + self._list + film + self._linebreak
        return new_message