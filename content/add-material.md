---
layout: main
title: Добавление нового материла на сайт ITIN.ua
---
# Как добавить новый материал?
Мы расматриваем интересные статьи которые относятся к тематике нашего сайта от всех пользователей.Такие статьи мы разместим после модерации.
В статье будет имя автора и ссылка на его профиль, с информацией о себе и о видах его деятельности.


## ![Send us an email](/images/info/email.png) Самое простое — выслать нам на Email
Вышлите нам на емейл [{{site.admin_email}}](mailto:{{site.admin_email}}) свою статью.
Воспользуйтесь шаблоном:

**Заголок статьи:** например, Вывод денег в Украину  
**Категория:** например, Работа с иностранными компаниями  
**Автор:** Иван Васильев  
**Картинка:** файл или ссылка на иллюстарцию к материалу  
__*Сама статья*__
       
Если вы пишите нам первый раз, тогда добавьте свое фото, и краткую информацию о себе. 
Например, как в разделе [Наши авторы](/content/list/users.html). 
Статья появится на сайте сразу после модерации.

## ![Send us an email](/images/info/octocat-yellow.png) Коллективная работа с сайтом через GitHub
Миллионы людей совместно работают над статьями и даже целыми ресурсами с помощью [GitHub](https://ru.wikipedia.org/wiki/GitHub).
Внося изменения на GitHub, они появятся у нас на сайте.

**GitHub** самый крупный веб-сервис для хостинга проектов, документов, сайтов и их совместной разработки.
Основан на системе контроля версий [Git](https://ru.wikipedia.org/wiki/Git)

Вот успешные примеры совмесной работы с текстами:  
* [Команда математиков за полгода написала 600-страничную книгу, используя GitHub](http://habrahabr.ru/post/184716/)  
* [Гражданский кодекс Франции теперь на Github](http://geektimes.ru/post/248196/)  
* [Исландия: каждая кухарка может написать Конституцию](http://ttolk.ru/?p=14243)  

## Работа с GitHub 

* Зарегистрируйтесь на сайте [https://github.com/](https://github.com/)  
* Сделайте Fork (Ваша  копия нашего проекта, в которой Вы можете вносить изменения, что бы они попали на сайт, а модератор может либо принять их либо отклонить) [https://github.com/itinua/itinua.github.io](https://github.com/itinua/itinua.github.io) 
 ![](/images/git/1.png)
* Внесите изменения под своим аккаунтом в проект (структура сайта и как добавить статью ниже) 
* Сделайте **Pull Request** (Предложить нам принять изменения) в наш репозиторий
![](/images/git/2.png)
![](/images/git/3.png)
![](/images/git/4.png)
* После модерации изменения появятся на сайте

В дальнейшем достаточно вносить изменения и отдавать их на модерацию.

На самом деле все вышесказанное очень простое действие, так работают миллионы программистов, тестеров, верстальщиков и других образованных людей.  
В современном мире совместная разработка возможна только благодаря таким вот системам :) 

## Структура сайта

**posts**  В этой папке все статьи   
**content/author** Информация о всех наших авторах  
**images** Картинки к материалам

## ![Send us an email](/images/info/article.png) Создание новой статьи
Статья появляется автоматически на сайте, когда в нужной папке появляется такой файл.
Например в директории
**_posts/[a1] Работа с иностранными компаниями**

Название файла должно быть в формате  
**2015-06-15**-kak-rabotat-s-google.md  
Где
**2015-06-15** Дата создания или последнего редактирования  
**kak-rabotat-s-google** Название транслитом, потом это будет ссылка URL  
**.md** - формат файла [Markdown](http://webquant.ru/posts/markdown/) или [Детальное описание на Английском](http://daringfireball.net/projects/markdown/syntax)  

**Что бы быстро создать правильное имя файла, воспользуйтель этой формой, например, впишите название статьи и нажмите Enter**

<script >
    var a = {"\u0438":"i","Ё":"YO","й":"i","Й":"I","Ц":"TS","У":"U","К":"K","Е":"E","Н":"N","Г":"G","Ш":"SH","Щ":"SCH","З":"Z","Х":"H","Ъ":"","ё":"yo","ц":"ts","у":"u","к":"k","е":"e","н":"n","г":"g","ш":"sh","щ":"sch","з":"z","х":"h","ъ":"","Ф":"F","Ы":"I","В":"V","А":"a","П":"P","Р":"R","О":"O","Л":"L","Д":"D","Ж":"ZH","Э":"E","ф":"f","ы":"i","в":"v","а":"a","п":"p","р":"r","о":"o","л":"l","д":"d","ж":"zh","э":"e","Я":"Ya","Ч":"CH","С":"S","М":"M","И":"I","Т":"T","Ь":"","Б":"B","Ю":"YU","я":"ya","ч":"ch","с":"s","м":"m","и":"i","т":"t","ь":"","б":"b","ю":"yu"};
раздела
    function transliterate(word){
    return word.split('').map(function (char) {
    return a[char] || char;
    }).join("");
    }
    function onKey(e){
         e = e || window.event;
            if (e.keyCode == 13)
            {
                var orig = document.getElementById('btnSearch').value;
                orig = orig.replace(/[.,:?()!"'№„“Ьь]/g, '');
                document.getElementById('btitle1').innerHTML = orig;
                
                var text = orig.toLowerCase().replace(/^\s+|\s+$/g,'').replace(/ /g, '-');
                var r = transliterate(text).replace(/[^\x00-\x7F]/g, "");
                
                var today = new Date().toISOString().slice(0, 10);
                r = today +"-"+ r + ".md";
                document.getElementById('btnSearch').value = r;
                document.getElementById('btitle3').innerHTML = r;
                document.getElementById('btnSearch').select();
            }
    }
    function onAuthor(v){
    document.getElementById('bauthor').innerHTML=v;
    }
     function onCategory(v){
        document.getElementById('bcategory').innerHTML=v;
    }
    
    function onImg(img){
     document.getElementById('bimg').innerHTML=img.name;
        }
    function loadImg(){
        $.ajax({
            type: "GET",
            url: "https://github.com/itinua/itinua.github.io/tree/master/images"
        }).done(function (data) {
           var container = $('<div/>').html(data);
           var result = [];
            container.find('a.js-directory-link').each(function() {
                if(this.href.match(/.jpg$/)){
                    var image = "https://raw.githubusercontent.com/itinua/itinua.github.io/master/images/"+this.title;
                    var item = "<img style='padding:5px;' src='"+image+"' height='70' name='"+this.title+"' onclick='onImg(this)'/>";
                    result+=item;
                }
    
            });
    
            $("#msgid").html(result);
        });
    }
    
</script>
###Форма создания имени файла (title) для статьи

Название <input type="text" id="btnSearch" size="60" onkeypress="onKey(event);"/><br/><br/>
Автор <select onchange="onAuthor(this.value);">
{% for item in site.authors %}
{% assign user=item[1] %}
  <option value="{{item[0]}}">{{user.name}}</option>
{% endfor %}  
</select>
Категория <select onchange="onCategory(this.value);"style="width: 240px">
{% for item in site.all_categories %}
  <option value="{{item.id}}">{{item.name}}</option>
{% endfor %}  
{% for item in site.all_countries %}
  <option value="{{item.id}}">{{item.name}}</option>
{% endfor %}  
</select> <input type="button" value="Картинки" onclick="loadImg()" />
[Для выбора картинок устновите Google Chrome Plugin](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi?hl=en)
<div id="msgid">
</div>

**Какая система налогообложения мне подходит**
станет  
**2015-06-17-kakaya-sistema-nalogooblozheniya-mne-podhodit.md**  

Это и есть хорошее имя для файла, которое нужно скопировать с формы создания имени файла и нужно будет потом вставить в поле при создании статьи . 

**Для того, что бы создать статью нужно**

*перейти на Github

*зайти в posts

*из папки posts перейти в нужный раздел (в котором Вы хотите разместить статью)

*возле названия раздела нажать на "+". 

Таким образом в нужном разделе вы создаете статью.

Далее вставляем имя файла в поле "name your file" (хорошее имя файла, которое мы скопировали ранее).

Теперь нам нужно сделать "шапку" статьи. Делается она очень просто - нужно скопировать шаблон, который ниже (**включая три тире сверху и снизу**) и вставить туда свои данные (подробности ниже в подтеме "Заголовок статьи").

**<font id="btitle3"></font>**
<pre style="white-space: normal;">
---<br/> 
layout: article<br/>  
categories: [<font id="bcategory">a1</font>]<br/>   
title: <font id="btitle1"></font><br/>
img: <font id="bimg"></font><br/>         
author: <font id="bauthor">ivan-ivanenko</font><br/>   
---<br/>  
</pre>

## Заголовок статьи (здесь вы указываете детали "шапки")

В файле статьи обязательно указать заголовок (т.е. "шапку), который можно скопировать с любой статьи нужного раздела и поменять под свою статью.

**Итак, то, что отбражается в заголовке статьи**

**---**  

**layout: article** Значит что у нас шаблон статья  

**categories: [a1, actual, featured]** Значит что статья появится в разделе _[a1] Работа с иностранными компаниями_ 

***actual*** - если статья должна появится внизу в актуальных  

***featured*** - если статья должна появится как главная, выделенная в разделе 

**title: Как работать с Google** Заголовок  

**img: money-minimal.jpg** Обязательное имя картинки, картинка должна находится в папке ***images***  

**author: ivan-ivanenko** Если есть автор 

**---**
Далее мы добавляем тело статьи, которое форматируем с помощью упрощенного языка разметки Markdown (кликабельная ссылка выше). **Внимание** Форматируйте материал по инструкции, так как статья может отображаться неправильно.

Отформатировав отправляйте нам :)
</pre>

ВСЕ

Создавайте материал и мы его ждем у нас на сайте

<a href="https://github.com/itinua/itinua.github.io/tree/master/_posts" target="_blank">Перейти в GitHub</a>

## Как добавить нового Автора на сайт
1) Добавить фото в папку **images/author**  
2) Создать учетную записить в файле **_config.yml**  
например  

         firstname-lastname:
           name: First Last
           job: Кем работает автор
           image: author picture.jpg фото автора
           fb: 
           ln: 
           tw:
           g_:
           web: 
           git: 
3) Создать страницу автора в **/content/author**  напрмер *firstname-lastname.md*  
с заголовком
<pre>
---
layout: userprofile
author: firstname-lastname
---
Описание автора в свободной форме
</pre>

Важно, что бы идентификатор автора совпадал в **_config.yml** и в  **/content/author**
