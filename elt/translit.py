import http.client


lang_maps = {
    "hindi": "hi-t-i0-und",
    "telegu": "te-t-i0-und",
    "bengali": "bn-t-i0-und",
    "tamil": "ta-t-i0-und",
    "malayalam": "ml-t-i0-und",
    "sanskrit": "sa-t-i0-und",
    "kannada": "kn-t-i0-und",
    "gujarati": "gu-t-i0-und",
    "marathi": "mr-t-i0-und",
    "odiya": "or-t-i0-und",
    "punjabi": "pu-t-i0-und",
    "urdu": "ur-t-i0-und",
}


class translit:
    def __init__(self, lang="hindi"):
        self.lang = lang_maps[lang]

    @staticmethod
    def request(q, lang):
        conn = http.client.HTTPSConnection("inputtools.google.com")
        conn.request(
            "GET",
            "/request?text="
            + q
            + "&itc="
            + lang
            + "&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test",
        )
        res = conn.getresponse()
        return res

    def get_lang(self, q):
        output = ""
        res = self.request(q, self.lang)
        res = res.read()
        output = str(res, encoding="utf=8")[14 + 4 + len(q) : -31]
        output = output.strip()
        return output

    def convert(self, stops):
        final_list = []
        special_chars = "/.,><?][}{)(|;:-+="
        for i in range(len(stops)):
            t_word = ""
            phrase_list = stops[i][:].split(" ")
            for word in phrase_list:
                if type(word) == int:
                    t_word += word
                elif word in special_chars:
                    t_word += word
                else:
                    t_word += self.get_lang(word)
                t_word += " "
            final_list.append(t_word[:-1])
        return final_list
