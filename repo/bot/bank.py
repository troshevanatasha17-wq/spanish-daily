# Банк вопросов по темам конспекта испанского (номер темы = номер в конспекте).
# mcq:   (вопрос, [варианты], индекс правильного, пояснение ≤200 символов)
# gap:   (bank, [(до, [правильные ответы], после), ...])
# multi: (вопрос, [варианты], [индексы правильных], пояснение)

BANK = {
1: dict(
    mcq=[
        ("Как читается буква h в испанском?", ["никогда не читается", "[х]", "[г]", "[ш]"], 0, "h всегда немая: hospital, ahora, hombre, huevo."),
        ("Как читается буква j?", ["[д]", "[х]", "[й]", "[ж]"], 1, "j = [х]: juego, jueves, jefe. ¡Jajaja! = хахаха."),
        ("Как читается g в слове «gente»?", ["[г]", "[х]", "[дж]", "[гь]"], 1, "g перед e, i = [х]; перед a, o, u — [г]: gato, gorda."),
        ("Какое слово читается с [нь]?", ["año", "ano", "pollo", "perro"], 0, "ñ = [нь]: año — год, niño — ребёнок."),
    ],
    gap=(["jefe", "año", "hombre"], [
        ("«Начальник» по-испански — ", ["jefe"], " (j = [х])"),
        ("«Год» по-испански — ", ["año"], " (ñ = [нь])"),
        ("В слове «", ["hombre"], "» (мужчина) буква h не читается."),
    ]),
    multi=("В каких словах h НЕ читается?",
           ["hospital", "ahora", "hombre", "jefe", "huevo"],
           [0, 1, 2, 4], "h всегда немая. В jefe немой буквы нет — j = [х]."),
),
2: dict(
    mcq=[
        ("— ¿Hola, qué tal? — …", ["Bien, ¿y tú?", "Me llamo Julio", "Soy de Madrid", "Encantado"], 0, "На ¿qué tal? отвечают: bien, ¿y tú? / ¡muy bien!"),
        ("Как спросить «как тебя зовут»?", ["¿Qué tal?", "¿Cómo te llamas?", "¿De dónde eres?", "¿Cuántos años tienes?"], 1, "Ответ: Me llamo… или (Yo) soy…"),
        ("Женщина знакомится и хочет сказать «очень приятно»:", ["Encantado", "Encantada", "Encantados", "Encantar"], 1, "По роду говорящего: женщина — encantada, мужчина — encantado."),
        ("«Доброе утро» по-испански:", ["Buenas tardes", "Buenas noches", "Buenos días", "Hasta luego"], 2, "día — м.р. → buenos días; tarde и noche — ж.р. → buenas."),
    ],
    gap=(["tal", "llamo", "noches"], [
        ("¿Hola, qué ", ["tal"], "? — привет, как дела?"),
        ("Me ", ["llamo"], " Natasha. ¿Y tú?"),
        ("¡Buenas ", ["noches"], "! — добрый вечер!"),
    ]),
    multi=("Что говорят при прощании?",
           ["Hasta luego", "Nos vemos", "Adiós", "Encantado", "Buenas noches"],
           [0, 1, 2], "Encantado — при знакомстве, buenas noches — приветствие вечером."),
),
3: dict(
    mcq=[
        ("Yo ___ de Madrid.", ["eres", "soy", "es", "son"], 1, "ser: yo soy, tú eres, él es."),
        ("Tom Holland es de Inglaterra. Él es ___.", ["inglés", "inglesa", "inglésa", "Inglaterra"], 0, "Мужчина — inglés, женщина — inglesa."),
        ("Kardashians son ___.", ["estadounidense", "estadounidenses", "americanos", "Estados Unidos"], 1, "Множественное число: estadounidenses."),
        ("— ¿De dónde eres? — …", ["Soy de Bogotá.", "Me llamo Ana.", "Muy bien.", "Encantada."], 0, "Вопрос «откуда ты?» → soy de + место."),
    ],
    gap=(["soy", "eres", "es"], [
        ("Yo ", ["soy"], " de Rusia."),
        ("¿De dónde ", ["eres"], " tú?"),
        ("Ella ", ["es"], " de España."),
    ]),
    multi=("Какие формы глагола ser правильные?",
           ["yo soy", "tú eres", "él son", "nosotros somos", "ellos es"],
           [0, 1, 3], "ser: soy, eres, es, somos, sois, son."),
),
4: dict(
    mcq=[
        ("___ cerveza", ["el", "la", "los", "las"], 1, "cerveza — женский род: la cerveza."),
        ("___ vino", ["la", "el", "una", "las"], 1, "vino — мужской род: el vino."),
        ("Множественное число слова «mujer»:", ["mujers", "mujeres", "mujera", "mujeras"], 1, "Слово на согласную + es: mujer → mujeres."),
        ("«кроссовки» с неопределённым артиклем:", ["unas zapatillas", "unos zapatillas", "un zapatillas", "una zapatillas"], 0, "zapatillas — ж.р. мн.ч.: unas."),
    ],
    gap=(["el", "la", "unos"], [
        ("", ["el"], " vino tinto — красное вино (м.р.)"),
        ("", ["la"], " carne — мясо (ж.р.)"),
        ("", ["unos"], " pantalones negros — чёрные брюки"),
    ]),
    multi=("Выбери слова женского рода:",
           ["la casa", "el día", "la falda", "el vino", "la ciudad"],
           [0, 2, 4], "el día — исключение, мужской род. el vino — тоже мужской."),
),
5: dict(
    mcq=[
        ("«Мне 27 лет» по-испански:", ["Tengo 27 años.", "Soy 27 años.", "Estoy 27 años.", "Tengo 27 veces."], 0, "Возраст — через tener: tengo X años."),
        ("44 по-испански:", ["cuarenta y cuatro", "cuatro cuarenta", "cuarenta cuatro", "catorce"], 0, "Десяток + y + единица: cuarenta y cuatro."),
        ("¿Cuántos años ___ tu abuela?", ["tienes", "tengo", "tiene", "tienen"], 2, "ella → tiene."),
        ("29 по-испански:", ["veintinueve", "veinte nueve", "treinta y nueve", "veintinuevos"], 0, "21–29 пишутся слитно: veintiuno … veintinueve."),
    ],
    gap=(["tengo", "treinta", "años"], [
        ("Yo ", ["tengo"], " 27 años."),
        ("31 = ", ["treinta"], " y uno."),
        ("¿Cuántos ", ["años"], " tienes?"),
    ]),
    multi=("Правильные числительные:",
           ["veintiuno", "veinte y uno", "treinta", "noventa", "sesenta y ocho"],
           [0, 2, 3, 4], "21–29 слитно (veintiuno), с 31 — через y: treinta y uno."),
),
6: dict(
    mcq=[
        ("___ haces? — Что ты делаешь?", ["Cómo", "Qué", "Dónde", "Cuándo"], 1, "qué — что; cómo — как."),
        ("«почему» и «потому что» по-испански:", ["por qué / porque", "porque / por qué", "por / para", "que / qué"], 0, "Вопрос — por qué (раздельно), ответ — porque (слитно)."),
        ("¿___ años tienes? — сколько тебе лет?", ["Qué", "Cómo", "Cuántos", "Cuál"], 2, "cuántos / cuántas — сколько."),
        ("¿De ___ eres? — откуда ты?", ["qué", "dónde", "adónde", "quién"], 1, "(de) dónde — (от)куда; adónde — куда."),
    ],
    gap=(["Qué", "dónde", "Cuántos"], [
        ("¿", ["Qué"], " haces en tu tiempo libre?"),
        ("¿De ", ["dónde"], " eres?"),
        ("¿", ["Cuántos"], " años tienes?"),
    ]),
    multi=("Выбери вопросительные слова:",
           ["qué", "cómo", "pero", "cuántos", "porque"],
           [0, 1, 3], "pero — но, porque — потому что: это не вопросительные слова."),
),
7: dict(
    mcq=[
        ("Yo ___ (cantar).", ["cantas", "canto", "canta", "cantar"], 1, "-ar: yo + o → canto."),
        ("Tú ___ (bailar).", ["bailo", "bailas", "baila", "bailan"], 1, "-ar: tú + as → bailas."),
        ("¿___ tú por el parque los domingos? (pasear)", ["paseo", "paseas", "pasea", "paseamos"], 1, "tú + as → paseas."),
        ("Ella ___ (cocinar) sopa.", ["cocino", "cocinas", "cocina", "cocinan"], 2, "él/ella + a → cocina."),
    ],
    gap=(["hablo", "estudias", "trabaja"], [
        ("Yo ", ["hablo"], " español."),
        ("¿Tú ", ["estudias"], " inglés?"),
        ("Ella ", ["trabaja"], " en una oficina."),
    ]),
    multi=("Правильные формы глаголов на -ar:",
           ["yo canto", "tú bailas", "yo hablas", "ella trabaja", "tú cocino"],
           [0, 1, 3], "yo + o, tú + as, él/ella + a."),
),
8: dict(
    mcq=[
        ("Tú ___ (leer) libros.", ["leo", "lees", "lee", "leéis"], 1, "-er: tú + es → lees."),
        ("Yo ___ (vivir) en Madrid.", ["vivo", "vives", "vive", "vivimos"], 0, "-ir: yo + o → vivo."),
        ("¿___ (beber) cerveza a veces?", ["Bebo", "Bebes", "Bebe", "Bebéis"], 1, "-er: tú + es → bebes."),
        ("Nosotros ___ (comer) juntos.", ["comemos", "coméis", "comen", "como"], 0, "-er: nosotros + emos → comemos."),
    ],
    gap=(["como", "escribes", "lee"], [
        ("Yo ", ["como"], " ensalada."),
        ("Tú ", ["escribes"], " mucho en tu trabajo."),
        ("Ella ", ["lee"], " un libro."),
    ]),
    multi=("Правильные формы глаголов на -er / -ir:",
           ["yo veo", "tú comes", "yo vivo", "tú leo", "ella escribe"],
           [0, 1, 2, 4], "tú + es: comes, lees, escribes. ella + e: escribe."),
),
9: dict(
    mcq=[
        ("Yo ___ (tener) 27 años.", ["tienes", "tengo", "teno", "tiene"], 1, "tener: yo tengo (нестандартная форма)."),
        ("Ella ___ (hacer) yoga.", ["haco", "haces", "hace", "hago"], 2, "hacer: yo hago, но él/ella — hace."),
        ("Yo ___ (salir) con amigos.", ["salo", "sales", "salgo", "sale"], 2, "salir: yo salgo."),
        ("¿___ (ir) a la cafetería? — спроси у собеседника", ["Voy", "Vas", "Va", "Vamos"], 1, "ir: tú vas. voy — это yo."),
    ],
    gap=(["tengo", "hago", "voy"], [
        ("Yo ", ["tengo"], " muchos amigos."),
        ("Yo ", ["hago"], " yoga por la mañana."),
        ("Yo ", ["voy"], " al trabajo en metro."),
    ]),
    multi=("Правильные формы особых глаголов:",
           ["yo tengo", "tú haces", "yo salo", "él va", "tú veo"],
           [0, 1, 3], "yo salgo (не salo), tú ves (не veo), él va."),
),
10: dict(
    mcq=[
        ("Nosotros ___ (trabajar) hasta las 6.", ["trabajamos", "trabajáis", "trabajan", "trabajo"], 0, "-ar: nosotros + amos → trabajamos."),
        ("Vosotros ___ (ser) altos.", ["somos", "sois", "son", "ser"], 1, "ser: vosotros sois. somos — nosotros."),
        ("Ellos ___ (vivir) juntos.", ["vivimos", "vivís", "viven", "vive"], 2, "-ir: ellos + en → viven."),
        ("Nosotros ___ (comer) juntos por la noche.", ["comemos", "coméis", "comen", "como"], 0, "-er: nosotros + emos → comemos."),
    ],
    gap=(["vamos", "sois", "escriben"], [
        ("Nosotros ", ["vamos"], " al parque."),
        ("Vosotros ", ["sois"], " guapas."),
        ("Ellos ", ["escriben"], " mucho en su trabajo."),
    ]),
    multi=("Правильные формы:",
           ["nosotros hablamos", "vosotros coméis", "ellos vive", "vosotros cantáis", "nosotros van"],
           [0, 1, 3], "ellos viven; nosotros + amos/emos/imos, но ir → vamos."),
),
11: dict(
    mcq=[
        ("___ gusta salir con amigos. (мне нравится)", ["Te", "Me", "Le", "Les"], 1, "me gusta — мне нравится."),
        ("Me ___ los gatos.", ["gusta", "gustan", "gusto", "gustas"], 1, "Множественное число → gustan."),
        ("Согласиться с фразой «no me gusta»:", ["A mí también", "A mí tampoco", "A mí sí", "A mí no"], 1, "«Мне тоже нет» = a mí tampoco."),
        ("A mis padres ___ gusta viajar.", ["le", "les", "me", "te"], 1, "A + люди во мн.ч. → les gusta."),
    ],
    gap=(["gusta", "gustan", "también"], [
        ("Me ", ["gusta"], " el vino. — мне нравится вино"),
        ("Me ", ["gustan"], " los gatos. — мне нравятся коты"),
        ("— Me gusta leer. — A mí ", ["también"], ". — мне тоже"),
    ]),
    multi=("Правильные фразы с gustar:",
           ["Me gusta cantar", "Te gustan los gatos", "A ella le gusta bailar", "Me gustas el vino", "Les gusta viajar"],
           [0, 1, 2, 4], "gusta/gustan зависит от того, что нравится: me gusta el vino (не gustas)."),
),
12: dict(
    mcq=[
        ("Yo ___ (levantarse) a las 8.", ["me levanto", "te levantas", "se levanta", "me levantas"], 0, "se → me + форма yo: me levanto."),
        ("¿Cómo ___ llamas?", ["me", "te", "se", "os"], 1, "tú → te llamas."),
        ("Ellos ___ (acostarse) tarde.", ["se acuestan", "nos acostamos", "se acuesta", "se acuestan"], 0, "ellos se acuestan (o→ue)."),
        ("«Я просыпаюсь» (despertarse):", ["me despierto", "me despertó", "se despierta", "me despiertas"], 0, "e→ie: me despierto."),
    ],
    gap=(["me ducho", "te acuestas", "se llama"], [
        ("Yo ", ["me ducho"], " por la mañana."),
        ("¿A qué hora ", ["te acuestas"], " tú?"),
        ("Ella ", ["se llama"], " Marta."),
    ]),
    multi=("Правильные формы возвратных глаголов:",
           ["me llamo", "te levantas", "se ducha", "nos llamamos", "se acuesto"],
           [0, 1, 2, 3], "Частица по лицу: me/te/se/nos/os; acostarse: o→ue (me acuesto)."),
),
13: dict(
    mcq=[
        ("Tengo que ___ deporte. (мне надо заниматься спортом)", ["hacer", "hago", "haces", "haciendo"], 0, "tener que + инфинитив."),
        ("«Я могу» по-испански:", ["puedo", "puede", "puedes", "podo"], 0, "poder: o→ue, yo puedo."),
        ("Ella tiene que ___ al trabajo.", ["va", "ir", "vas", "voy"], 1, "tener que + инфинитив: ir."),
        ("«Можно мне заплатить картой?»", ["¿Puedo pagar con tarjeta?", "¿Puedes pagar con tarjeta?", "¿Puede pagar con tarjeta?", "¿Podemos pagar con tarjeta?"], 0, "Просьба от себя: ¿puedo pagar…?"),
    ],
    gap=(["tengo que", "puedo", "puedes"], [
        ("Yo ", ["tengo que"], " ir al trabajo. — мне надо идти на работу"),
        ("Cuando llueve, yo ", ["puedo"], " estar en casa. — могу быть дома"),
        ("¿Tú ", ["puedes"], " hablar otros idiomas? — ты можешь говорить на других языках?"),
    ]),
    multi=("Правильные фразы:",
           ["Tengo que estudiar", "Puedo estar en la playa", "Tienes que comes", "¿Puedo pagar en efectivo?", "Puedes hablar"],
           [0, 1, 3, 4], "tener que + инфинитив (comes — форма глагола, не инфинитив)."),
),
14: dict(
    mcq=[
        ("Yo ___ a viajar a México este verano.", ["voy", "vas", "va", "vamos"], 0, "ir a + инфинитив: yo voy."),
        ("¿Qué ___ a hacer este fin de semana?", ["voy", "vas", "va", "van"], 1, "tú vas a + инфинитив."),
        ("Voy a ___ un jersey gris. (надену)", ["ponerme", "llevarme", "ponerse", "me pongo"], 0, "voy a ponerme — надену (возвратный глагол)."),
        ("Ellos ___ a jugar al tenis.", ["van", "vamos", "vais", "va"], 0, "ellos van a + инфинитив."),
    ],
    gap=(["voy a", "vas a", "vamos a"], [
        ("Yo ", ["voy a"], " viajar este verano."),
        ("¿Qué ", ["vas a"], " hacer hoy?"),
        ("Nosotros ", ["vamos a"], " ir al parque."),
    ]),
    multi=("Правильные фразы о будущем:",
           ["Voy a llevar un vestido", "Tú vas a ponerte una camiseta", "Ellos van a comer", "Yo va a bailar", "Vamos a descansar"],
           [0, 1, 2, 4], "ir спрягается: yo voy, tú vas, ellos van, nosotros vamos."),
),
15: dict(
    mcq=[
        ("Yo ___ cansada. (я устала)", ["soy", "estoy", "es", "está"], 1, "Временное состояние → estar: estoy cansada."),
        ("Ella ___ profesora.", ["es", "está", "soy", "estás"], 0, "Профессия — постоянное → ser: es."),
        ("¿___ casada? — ты замужем?", ["Eres", "Estás", "Es", "Está"], 1, "estar casado/a — состояние: ¿estás casada?"),
        ("Nosotros ___ en casa. (мы дома)", ["somos", "estamos", "están", "son"], 1, "Местонахождение → estar: estamos en casa."),
    ],
    gap=(["es", "estoy", "está"], [
        ("Ella ", ["es"], " de Rusia. (постоянное → ser)"),
        ("Yo ", ["estoy"], " cansada. (состояние → estar)"),
        ("Él no ", ["está"], " casado."),
    ]),
    multi=("Фразы с правильным глаголом:",
           ["Soy profesora", "Estoy en casa", "Es rusa", "Está cansado", "Soy casada"],
           [0, 1, 2, 3], "casado — estar (¿estás casada?), не ser."),
),
16: dict(
    mcq=[
        ("___ padres se llaman Ana y Luis. (мои родители)", ["Mi", "Mis", "Tu", "Su"], 1, "множественное число → mis."),
        ("Фраза «su hermana» может значить:", ["его, её или их сестра", "только его сестра", "только её сестра", "моя сестра"], 0, "su/sus = его, её, их — понятно только из контекста."),
        ("¿Cómo se llama ___ hermano? (твой брат)", ["mi", "tu", "mis", "tus"], 1, "tu + ед.ч.: tu hermano."),
        ("«быть замужем» по-испански:", ["estar casada", "ser casada", "estar casado", "ser casado"], 0, "estar + casado/a; женщина — casada."),
    ],
    gap=(["mis", "su", "se llaman"], [
        ("", ["Mis"], " abuelas se llaman Carmen y Rosa."),
        ("", ["Su"], " padre tiene 58 años. (его/её/их)"),
        ("¿Cómo ", ["se llaman"], " tus padres?"),
    ]),
    multi=("Правильные фразы:",
           ["mi hermano", "mis padres", "tus hijos", "su hermanas", "se llaman Ana y Luis"],
           [0, 1, 2, 4], "su + ед.ч.: su hermana; sus + мн.ч.: sus hermanos."),
),
17: dict(
    mcq=[
        ("Ella es una mujer ___. (высокая)", ["alto", "alta", "altos", "altas"], 1, "ж.р. ед.ч. → alta."),
        ("Ellos son ___. (толстые)", ["gordo", "gorda", "gordos", "gordas"], 2, "м.р. мн.ч. → gordos."),
        ("«Она брюнетка» по-испански:", ["Es morena", "Es rubia", "Es moreno", "Tiene morena"], 0, "moreno/a; женский род → morena."),
        ("«Он мне не нравится как человек»:", ["No me cae bien", "No me gusta", "No me cae malo", "No me cae"], 0, "me cae bien / no me cae bien."),
    ],
    gap=(["delgada", "altos", "largo"], [
        ("Ella es una mujer ", ["delgada"], ". — она худенькая"),
        ("Vosotros sois ", ["altos"], ". — вы высокие"),
        ("Tiene el pelo ", ["largo"], ". — у неё длинные волосы"),
    ]),
    multi=("Правильные согласования:",
           ["una mujer delgada", "un hombre alto", "vosotras sois guapas", "ellos son gorda", "ellas son altas"],
           [0, 1, 2, 4], "ellos son gordos (м.р. мн.ч.)."),
),
18: dict(
    mcq=[
        ("___ vestido (это платье)", ["este", "esta", "estos", "estas"], 0, "vestido — м.р. ед.ч. → este."),
        ("___ zapatillas rosas (эти розовые кроссовки)", ["este", "esta", "estos", "estas"], 3, "ж.р. мн.ч. → estas."),
        ("— ¿Te gusta esta blusa o esta? — …", ["Me gusta la blanca.", "Me gusta esta blanca.", "Me gusta el blanco.", "Me gusta blanco."], 0, "blusa — ж.р. → la blanca."),
        ("___ falda verde (эта зелёная юбка)", ["este", "esta", "estos", "estas"], 1, "falda — ж.р. ед.ч. → esta."),
    ],
    gap=(["este", "estos", "estas"], [
        ("", ["este"], " jersey blanco — этот белый джемпер"),
        ("", ["estos"], " pantalones — эти брюки"),
        ("", ["estas"], " zapatillas — эти кроссовки"),
    ]),
    multi=("Правильные сочетания:",
           ["este vestido", "esta falda", "estos zapatos", "estas blusa", "estas faldas"],
           [0, 1, 2, 4], "blusa — женский род: esta blusa."),
),
19: dict(
    mcq=[
        ("¿A qué hora te levantas? — …", ["A las 8.", "A la 8.", "En las 8.", "Son las 8."], 0, "a las + число; только a la una (в час)."),
        ("«в час» (дня, ночи):", ["a las una", "a la una", "en la una", "a la uno"], 1, "Исключение: a la una."),
        ("8:30 по-испански:", ["ocho y media", "ocho media", "ocho y cuarto", "media ocho"], 0, "y media — половина следующего часа."),
        ("Ceno a las 7.30 ___ .", ["de la mañana", "de la tarde", "de la noche", "de noche"], 2, "Вечером/ночью → de la noche (или de la tarde)."),
    ],
    gap=(["a las", "y media", "a la una"], [
        ("Me levanto ", ["a las"], " 7. — встаю в семь"),
        ("Ceno a las 7 ", ["y media"], " — ужинаю в 7:30"),
        ("Tiene un descanso ", ["a la una"], " — перерыв в час"),
    ]),
    multi=("Правильные фразы о времени:",
           ["a las ocho", "a la una", "me acuesto a las 11", "a las medianoche", "de la mañana"],
           [0, 1, 2, 4], "medianoche — существительное: a medianoche (без las)."),
),
20: dict(
    mcq=[
        ("«Сначала я моюсь» по-испански:", ["Primero me ducho.", "Primero ducho.", "Me primero ducho.", "Ducho primero."], 0, "primero + возвратный глагол."),
        ("«После завтрака иду на работу»:", ["Después de desayunar voy al trabajo.", "Después desayuno voy al trabajo.", "Después de desayuno voy trabajo.", "Después voy a trabajo."], 0, "después de + инфинитив; ir al trabajo."),
        ("«У меня перерыв в час»:", ["Tengo un descanso a la una.", "Tengo descanso a la una.", "Descanso a la una.", "Tengo un descanso la una."], 0, "tener un descanso."),
        ("Ella se acuesta a las 9 porque ___ levantarse temprano.", ["tiene que", "tener que", "tiene", "que"], 0, "tener que + инфинитив: tiene que levantarse."),
    ],
    gap=(["me levanto", "después de", "me acuesto"], [
        ("Yo ", ["me levanto"], " a las ocho de la mañana."),
        ("", ["Después de"], " ducharse bebo un vaso de agua."),
        ("Yo ", ["me acuesto"], " a las 11 de la noche."),
    ]),
    multi=("Правильные фразы о распорядке:",
           ["me levanto a las 7", "después de cenar veo la tele", "antes de dormir leo", "me ducho rápidamente", "se acuesta a la mañana"],
           [0, 1, 2, 3], "Время уточняем: a las 9 de la noche, por la mañana."),
),
21: dict(
    mcq=[
        ("«в понедельник» по-испански:", ["el lunes", "los lunes", "en lunes", "a lunes"], 0, "el + день недели — в этот день; los lunes — по понедельникам."),
        ("«По средам я хожу в спортзал»:", ["Los miércoles voy al gimnasio.", "El miércoles voy gimnasio.", "Los miércoles voy gimnasio.", "Miércoles voy al gimnasio."], 0, "los + день недели — регулярное действие."),
        ("«Мой день рождения в июне»:", ["Mi cumpleaños es en junio.", "Mi cumpleaños es junio.", "Mi cumpleaños está en junio.", "Cumpleaños es en junio."], 0, "es en + месяц."),
        ("Времена года: el invierno, la primavera, el verano, ___.", ["el otoño", "la otoño", "el agosto", "la temporala"], 0, "el otoño — осень (мужской род)."),
    ],
    gap=(["el viernes", "en verano", "los fines de semana"], [
        ("", ["El viernes"], " va a la playa. — в пятницу она идёт на пляж"),
        ("Mi cumpleaños es en junio, ", ["en verano"], "."),
        ("", ["Los fines de semana"], " llevo un vestido. — по выходным"),
    ]),
    multi=("Правильные фразы:",
           ["el lunes trabajo", "los miércoles voy al gimnasio", "en junio", "el invierno hace frío", "en la primavera nieva"],
           [0, 1, 2, 3], "Месяц — en; времена года с артиклем el/la."),
),
22: dict(
    mcq=[
        ("«Идёт дождь» по-испански:", ["llueve", "nieva", "hace lluvia", "lluever"], 0, "llover → llueve; nevar → nieva (снег)."),
        ("«Холодно» о погоде:", ["hace frío", "es frío", "está frío", "hace frio mucho"], 0, "hace + существительное: hace frío/calor/sol/viento."),
        ("«Сегодня минус два градуса»:", ["Hace menos dos grados.", "Hace dos grados menos.", "Es menos dos grados.", "Hace frío dos grados."], 0, "hace menos + число grados."),
        ("«Мне не нравится, когда идёт дождь»:", ["No me gusta cuando llueve.", "No me gusta cuando hace llueve.", "No gusta cuando llueve.", "No me gusta cuando llueva."], 0, "cuando + llueve."),
    ],
    gap=(["hace", "llueve", "nieva"], [
        ("", ["Hace"], " mucho calor. — очень жарко"),
        ("Hace frío y ", ["llueve"], ". — холодно и идёт дождь"),
        ("En la montaña en marzo ", ["nieva"], ". — в горах в марте идёт снег"),
    ]),
    multi=("Правильные фразы о погоде:",
           ["hace mucho calor", "hace buen tiempo", "hace 20 grados", "es mucho frío", "llueve y nieva"],
           [0, 1, 2, 4], "О погоде — hace, не es."),
),
23: dict(
    mcq=[
        ("«чёрные брюки» по-испански:", ["unos pantalones negros", "unos pantalones negras", "un pantalones negro", "unos pantalón negros"], 0, "pantalones — м.р. мн.ч. → negros."),
        ("«джинсы» по-испански:", ["los vaqueros", "las vaqueras", "el vaquero", "los jeans"], 0, "los vaqueros — джинсы."),
        ("Множественное число цвета «azul»:", ["azules", "azulos", "azul", "azuls"], 0, "На согласную + es: azules, verdes, grises."),
        ("«Сегодня я ношу белое платье»:", ["Hoy llevo un vestido blanco.", "Hoy llevo una vestida blanca.", "Hoy me llevo un vestido blanco.", "Hoy llevo un vestido blanca."], 0, "llevar — носить; vestido — м.р. → blanco."),
    ],
    gap=(["camiseta", "vaqueros", "roja"], [
        ("una ", ["camiseta"], " azul — синяя футболка"),
        ("unos ", ["vaqueros"], " azules — синие джинсы"),
        ("una falda ", ["roja"], " — красная юбка"),
    ]),
    multi=("Правильные сочетания:",
           ["unos zapatos negros", "unas zapatillas rosas", "una camiseta azul", "un vestido blanca", "unos pantalones cortos"],
           [0, 1, 2, 4], "vestido — мужской род: un vestido blanco."),
),
24: dict(
    mcq=[
        ("«Можно заплатить картой?»", ["¿Puedo pagar con tarjeta?", "¿Puedo pagar en efectivo?", "¿Cuánto cuesta?", "¿Qué número usas?"], 0, "pagar con tarjeta — картой; en efectivo — наличными."),
        ("«Сколько стоит рубашка?»", ["¿Cuánto cuesta la camisa?", "¿Cuánto cuestan la camisa?", "¿Cuánto es la camisa?", "¿Qué cuesta la camisa?"], 0, "cuesta — ед.ч.; cuestan — мн.ч."),
        ("«Какой у тебя размер?» (обувь)", ["¿Qué número usas?", "¿Cuál es tu talla?", "¿Qué te parece?", "¿Cuánto usas?"], 0, "número — размер обуви; talla — размер одежды."),
        ("«Тебе идёт» по-испански:", ["Te queda bien.", "Te lleva bien.", "Te es bien.", "Te parece bien."], 0, "quedar bien — идти (об одежде)."),
    ],
    gap=(["en efectivo", "cuesta", "barata"], [
        ("¿Puedo pagar ", ["en efectivo"], "? — можно наличными?"),
        ("¿Cuánto ", ["cuesta"], " la camisa? — сколько стоит рубашка?"),
        ("¿Tenéis alguna ropa muy ", ["barata"], "? — есть что-нибудь подешевле?"),
    ]),
    multi=("Фразы для магазина:",
           ["¿Cuál es tu talla?", "Te queda bien", "Es caro", "¿Qué haces?", "¿Puedo pagar con tarjeta?"],
           [0, 1, 2, 4], "¿Qué haces? — «что ты делаешь» — не про покупки."),
),
25: dict(
    mcq=[
        ("«Еду на работу на автобусе»:", ["Voy en autobús al trabajo.", "Voy a autobús al trabajo.", "Voy en autobús a trabajo.", "Voy autobús al trabajo."], 0, "ir en + транспорт; al = a + el."),
        ("«Она летит в Испанию»:", ["Ella va en avión a España.", "Ella va avión a España.", "Ella va en avión al España.", "Ella va a avión a España."], 0, "ir en avión a + страна."),
        ("«загорать» по-испански:", ["tomar el sol", "hacer el sol", "tomar sol", "estar el sol"], 0, "tomar el sol."),
        ("A Ana le gusta viajar en tren ___ es rápido y cómodo.", ["porque", "por qué", "por", "que"], 0, "«потому что» = porque (слитно)."),
    ],
    gap=(["en tren", "la playa", "fotos"], [
        ("Tú vas ", ["en tren"], " a Madrid. — едешь поездом в Мадрид"),
        ("Cuando hace calor voy a ", ["la playa"], ". — иду на пляж"),
        ("Me gusta hacer ", ["fotos"], ". — люблю фотографировать"),
    ]),
    multi=("Чем занимаются в отпуске:",
           ["nadar en el mar", "visitar museos", "hacer turismo", "ver la tele", "tomar el sol"],
           [0, 1, 2, 4], "ver la tele — домашнее занятие, не отпускное."),
),
26: dict(
    mcq=[
        ("Как в Испании называют Санту?", ["Papa Noel", "Santa Claus", "El Gordo", "Reyes"], 0, "En España Santa Claus = Papa Noel."),
        ("Что едят в новогоднюю ночь в Испании?", ["doce uvas", "tapas", "turrones", "veinte uvas"], 0, "12 виноградин в полночь — каждая загадывает желание."),
        ("«Каждая виноградина — это желание»:", ["Cada uva es un deseo.", "Cada uva es un desayuno.", "Cada uva es un regalo.", "Cada uva es un día."], 0, "el deseo — желание."),
        ("Рождественская лотерея в Испании называется:", ["El Gordo", "La Navidad", "El Año Nuevo", "La Suerte"], 0, "La lotería de Navidad = El Gordo."),
    ],
    gap=(["se reúne", "uvas", "diciembre"], [
        ("La familia ", ["se reúne"], " en casa. — семья собирается дома"),
        ("A las doce comemos doce ", ["uvas"], ". — в полночь едим 12 виноградин"),
        ("El 24 de ", ["diciembre"], " cenamos juntos. — 24 декабря ужинаем вместе"),
    ]),
    multi=("Испанские традиции с доски:",
           ["Papa Noel", "doce uvas en Año Nuevo", "El Gordo", "Día de Muertos es fiesta española", "cenar en familia el 24"],
           [0, 1, 2, 4], "Día de Muertos — мексиканский праздник, не испанский."),
),
}
