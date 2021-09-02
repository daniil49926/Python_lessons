import vk_api
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
from vk_api.longpoll import VkLongPoll
from vk_api.longpoll import VkEventType
from vk_api import VkUpload


token = ''

 
vk = vk_api.VkApi(token = token)
vk._auth_token()

print("Server ok...")

i = 0 #%Counter%#
a = ["привет", "Привет", "Хай", "хай", "ку", "Ку", "Здарова", "здарова", "дарова", "Дарова",
         "Здравствуйте", "здравствуйте", "здрасти", "Здрасти", "Доброе утро", "доброе утро", 
    "Добрый день", "добрый день", "Доброго времени суток", "доброго времени суток", "Салам",
            "салам", "Ну привет", "ну привет", "Приветствую", "приветствую", "Добрый вечер", 
    "добрый вечер", "Прив", "прив"]


j = 0 #%Counter2.0%#
b = ["Кинь ссылки на преподавателей", "кинь ссылки на преподавателей", "Ссылки на преподавателей",
    "ссылки на преподавателей", "преподаватели", "Преподаватели", "Кинь ссылки на учителей", 
    "кинь ссылки на учителей", "Ссылки на учителей", "ссылки на учителей", "учителя", "Учителя", 
    "Дай ссылку на преподавателей", "дай ссылку на преподавателей", "Дай ссылку на учителей", 
    "дай ссылку на учителей", "Дай ссылки на преподавателей", "дай ссылки на преподавателей", 
    "Дай ссылки на учителей", "дай ссылки на учителей", "ссылку на преподавателей", 
    "Ссылку на преподавателей", "ссылку на учителей", "Ссылку на учителей", "ссылки на преподавателей", 
    "Ссылки на преподавателей", "ссылки на учителей", "Ссылки на учителей"]


k = 0 #%Counter3.0%#
c = ["Ссылки на деканат", "ссылки на деканат", "Дай ссылки на деканат", "дай ссылки на деканат",
    "Кинь ссылки на деканат", "кинь ссылки на деканат", "деканат", "Деканат"]


l = 0 #%Counter4.0%#
d = ["Ссылки на группы", "ссылки на группы", "Дай ссылки на группы", 
     "дай ссылки на группы", "Кинь ссылки на группы", "кинь ссылки на группы", 
     "группы", "Группы", "Сообщества", "сообщества", "Ссылки на сообщества", 
     "ссылки на сообщества", "Дай ссылки на сообщества", "дай ссылки на сообщества",
    "Кинь ссылки на сообщества", "кинь ссылки на сообщества"]


h = 0 #%Counter5.0%#
f = ["фото КФУ", "Фото КФУ", "скинь фото КФУ", "Скинь фото КФУ", "Отправь фото кфу",
    "отправь фото КФУ", "фото кфу", "Фото кфу", "скинь фото кфу", "Скинь фото кфу", 
    "Отправь фото кфу","отправь фото кфу", "фото института", "Фото института", 
    "скинь фото института", "Скинь фото института", "Отправь фото института",
   "отправь фото института", "Кинь фото института", "кинь фото института"]


q = 0
w = ["\help", "помощь", "Помощь"]


e = 0
r = ["Скинь расписание", "скинь расписание", "Кинь расписание", "кинь расписание", "расписание", "Расписание"]


t = 0
y = ["Новости КФУ", "новости КФУ", "Новости института", "новости института", "Новости кфу", "новости кфу",
    "Новости", "новости", "Последние новости", "последние новости", "Последние новости КФУ",
   "последние новости КФУ","Последние новости кфу", "последние новости кфу", "Последние новости кфу",
   "последние новости кфу"]


while True:
                                               # {"ts":"4","updates":[{"type":"wall_post_new","object":
                                               #{"id":28,"from_id":-123456,"owner_id":-123456,"date":1519631591,
                                               #"marked_as_ads":0,"post_type":"post"
                                               #,"text":"Post text","can_edit":1,"created_by":564321,"can_delete":1,
                                               #"comments":{"count":0}},"group_id":123456}]}

    messages = vk.method("messages.getConversations",{"offset":0,"count":20,"filter":"unanswered"})
    
    if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            for q in range(3):
                if body.lower() == w[q]:
                    vk.method("messages.send", {"peer_id": id, "message": "\U0001f4cc Что я могу:\nСкидывать ссылки на преподователей, деканат, оффицальные группы КФУ\n\nИнформировать о последних новостях\n\nПомогать с поиском информации о КФУ\n\nFor example:\n <Скинь ссылки на преподователей>\n <Скинь фото КФУ>\n <Скинь расписание пар>\n и тп", "random_id": get_random_id()})


            for i in range(30):
                if body.lower() == a[i]:
                    if i < 10:
                        i=1
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Приветствую!\U0001f43c\nЯ бот kamata.\nHow can i help you?", "random_id": get_random_id()})
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Для получения информации напиши <\help>", "random_id": get_random_id()})
                    if (i > 10) and (i<20):
                        i=1
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Привет!\U0001f600\nЯ бот kamata.\nHow can i help you?", "random_id": get_random_id()})
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Для получения информации напиши <\help>", "random_id": get_random_id()})
                    if (i > 20) and (i<30):
                        i=1
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Привет!\U0001f608\nЯ бот kamata.\nHow can i help you?", "random_id": get_random_id()})
                        vk.method("messages.send", 
                                  {"peer_id": id, "message": "Для получения информации напиши <\help>", "random_id": get_random_id()})



            for j in range(28):
                if body.lower() == b[j]:
                    vk.method("messages.send", 
                              {"peer_id": id, "message": "https://vk.com/id444710087 - Чабанов В. программирование\n\n"
                              "https://vk.com/kisarsenal - Корниенко А. ИКТ/3D-моделирование\n\n" 
                              "https://vk.com/si_smirnova - Смирнова С. высшая математика\n\n"
                              "https://vk.com/id212121815 - Ильина В. иностранный язык\n\n"
                              "https://vk.com/id6304742 - Сосновский Ю. ИКТ/Проект/схемотехника/робототехника\n\n"
                              "https://vk.com/id90381955 - Засека М. Физ-ра\n\n"
                              "https://vk.com/id587875071 - Сердюков В. Физ-ра\n\n"
                              "https://vk.com/id587442982 - Горская И. Структуры и алгоритмы\n\n"
                              "https://vk.com/id14075349 - Задерейчюк А. История\n\n"
                              "https://vk.com/id461453168 - Космачев О. лаб.физика\n\n"
                              "https://vk.com/id587450722 - Ахрамович Л. физика\n\n"
                              "https://vk.com/id6141672 - Матюнина Я. лаб.физика\n\n"
                              "https://vk.com/chernyshdp - Черныш Я. технологии проектирования\n\n"
                              "https://vk.com/u.foundme - Дмитриенко П. системное программирование\n\n"
                              "https://vk.com/milyukovvv - Милюков В. физика/комп.моделирование/методы и алгоритмы" , "random_id": get_random_id()})
            

            for k in range(7):
                 if body.lower() == c[k]:
                    vk.method("messages.send", 
                              {"peer_id": id, "message": "https://vk.com/straf - Рыбась А. деканат ФТИ\n\n"
                               "https://vk.com/id19403806 - Карасанова С. деканат ФТИ", "random_id": get_random_id()})


            
            for l in range(16):
                 if body.lower() == d[l]:
                    vk.method("messages.send", 
                              {"peer_id": id, "message": "https://vk.com/vernadskycfu -  КФУ\n\n"
                               "https://vk.com/college_tnu -  КФУ ТНУ\n\n"
                               "https://vk.com/kimkfu -  КИМ КФУ ФТИ\n\n"
                               "https://vk.com/phystechcfu -КФУ ФТИ", "random_id": get_random_id()})

            for h in range(20):
                if body.lower() == f[h]:
                    uploader = vk_api.upload.VkUpload(vk)    
                    img = uploader.photo_messages("tild3463-6561-4930-b738-643039353562__2.jpg")
                    media_id = str(img[0]['id'])
                    owner_id = str(img[0]['owner_id']) 
                    uploader1 = vk_api.upload.VkUpload(vk)    
                    img1 = uploader1.photo_messages("2_d_850.jpg")
                    media_id1 = str(img1[0]['id'])
                    owner_id1 = str(img1[0]['owner_id']) 
                    uploader2 = vk_api.upload.VkUpload(vk)    
                    img2 = uploader2.photo_messages("1114001230.jpg")
                    media_id2 = str(img2[0]['id'])
                    owner_id2 = str(img2[0]['owner_id']) 
                    uploader3 = vk_api.upload.VkUpload(vk)    
                    img3 = uploader3.photo_messages("15032014105030_1364.jpg")
                    media_id3 = str(img3[0]['id'])
                    owner_id3 = str(img3[0]['owner_id']) 
                    
                    if h < 5:
                        vk.method("messages.send", 
                                {"peer_id": id, "attachment": "photo" + owner_id3 + "_" + media_id3, "random_id": get_random_id()})
               
                    elif (h>5) and (h<10):
                        vk.method("messages.send", 
                                  {"peer_id": id, "attachment": "photo" + owner_id2 + "_" + media_id2, "random_id": get_random_id()})
                        
                    elif (h>10) and (h<15):
                        vk.method("messages.send", 
                                  {"peer_id": id, "attachment": "photo" + owner_id1 + "_" + media_id1, "random_id": get_random_id()})
                
                    elif (h>15) and (h<20):
                        vk.method("messages.send", 
                                  {"peer_id": id, "attachment": "photo" + owner_id + "_" + media_id, "random_id": get_random_id()})


            for e in range(6):
                if body.lower() == r[e]:
                    uploader = vk_api.upload.VkUpload(vk)    
                    img = uploader.photo_messages("123456789.jpg")
                    media_id4 = str(img[0]['id'])
                    owner_id4 = str(img[0]['owner_id'])
                    vk.method("messages.send", 
                                  {"peer_id": id, "attachment": "photo" + owner_id4 + "_" + media_id4, "random_id": get_random_id()})


            for t in range(16):
                if body.lower() == y[t]:
                    vk.method("messages.send", 
                              {"peer_id": id, "message": "Последние новости уже на сайте: https://cfuv.ru/category/news", "random_id": get_random_id()})


           
          











