from pymongo import MongoClient

client = MongoClient("mongodb+srv://SidRoy:Siddhant%402003@bol-cluster.i6olax5.mongodb.net/?retryWrites=true&w=majority&appName=bol-cluster")
db = client["bol"]

stories = [
    {
        "title": "banana",
        "translations": {
            "en": "As kids, when mom scolded us, we silently ate bananas and said, 'I'm a monkey now!'",
            "hi": "बचपन में जब मम्मी डाँटती थी, हम चुपचाप केला खाकर \"बंदर बन गए\" बोलते थे।",
            "bn": "ছোটবেলায় মা বকলে আমরা চুপচাপ কলা খেয়ে বলতাম, 'আমি এখন বাঁদর!'",
            "pa": "ਬਚਪਨ 'ਚ ਜਦ ਮਾਂ ਡਾਂਟਦੀ ਸੀ, ਅਸੀਂ ਚੁੱਪ ਚਾਪ ਕੇਲਾ ਖਾ ਕੇ ਕਹਿੰਦੇ, 'ਹੁਣ ਮੈਂ ਬਾਂਦਰ ਹਾਂ!'",
            "bho": "बचपन में माई डाँटे त हम चुपचाप केला खा के कहे, 'अब हम बन गइल बानर!'",
            "es": "De niños, cuando mamá nos regañaba, comíamos un plátano y decíamos: '¡Ahora soy un mono!'",
            "ja": "子供の頃、母に怒られたらバナナを食べて「もう猿になった！」と言っていた。"
        }
    },
    {
        "title": "car",
        "translations": {
            "en": "If the groom comes in a car, relatives wish he came on a Bullet.",
            "hi": "शादी में दूल्हा कार से आया तो सब बोले, \"भाई, बुलेट से आता तो मजा आ जाता!\"",
            "bn": "বিয়ে তে বর গাড়ি করে এলে আত্মীয়রা বলে, 'বুলেটে আসলে ভালো হতো!'",
            "pa": "ਵਿਆਹ 'ਚ ਦੂਲਾ ਜੇ ਕਾਰ 'ਚ ਆਵੇ ਤਾਂ ਸਾਰੇ ਕਹਿੰਦੇ, 'ਬੁਲੇਟ 'ਤੇ ਆਉਂਦਾ ਤਾਂ ਵਧੀਆ ਸੀ!'",
            "bho": "शादी में दूल्हा अगर कार से आइल, त लोग कहले, 'बुलेट से आवता त मज़ा आ जाता!'",
            "es": "Si el novio llega en coche, todos desean que hubiera venido en una Bullet.",
            "ja": "花婿が車で来たら、みんな「バイクで来たらもっとよかった」と言う。"
        }
    },
    {
        "title": "book",
        "translations": {
            "en": "Books are bought with excitement, read rarely, and lost mysteriously.",
            "hi": "किताबें तो खरीदी जाती हैं, पढ़ी जाती हैं... कभी-कभी!",
            "bn": "বই কেনা হয় উৎসাহে, পড়া হয় কদাচিৎ, হারিয়ে যায় গায়েবভাবে।",
            "pa": "ਕਿਤਾਬਾਂ ਖਰੀਦ ਲੈਂਦੇ ਆਂ ਉਤਸ਼ਾਹ ਨਾਲ, ਪਰ ਪੜ੍ਹਦੇ ਨਹੀਂ!",
            "bho": "किताब त खरीदी जा ला जोश में, पढ़ल त कभी-कभारे, गायब हो जाला चुपचाप!",
            "es": "Los libros se compran con emoción, se leen rara vez y se pierden misteriosamente.",
            "ja": "本はワクワクして買うけど、読むのは稀で、いつの間にか行方不明。"
        }
    },
    {
        "title": "bottle",
        "translations": {
            "en": "Old bottle, chilled water, and grandma's scolding — straight to the heart.",
            "hi": "पुरानी बोतल में ठंडा पानी और दादी की डांट — दोनों सीधे दिल पे लगते थे।",
            "bn": "পুরনো বোতল, ঠান্ডা জল, আর দাদির বকা — একেবারে হৃদয়ে পৌঁছে যায়।",
            "pa": "ਪੁਰਾਣੀ ਬੋਤਲ, ਠੰਢਾ ਪਾਣੀ, ਤੇ ਦਾਦੀ ਦੀ ਡਾਂਟ — ਦਿਲ 'ਚ ਲੱਗ ਜਾਂਦੀ ਸੀ!",
            "bho": "पुरान बोतल में बर्फ जइसन पानी आउर दादी के डांट — सीधा दिल में लागेला!",
            "es": "Botella vieja, agua fría y los regaños de la abuela — directo al corazón.",
            "ja": "古いボトルに冷たい水、そして祖母の小言 — 心にしみる。"
        }
    },
    {
        "title": "bus",
        "translations": {
            "en": "Getting a seat on a crowded Indian bus? You're blessed!",
            "hi": "अगर सुबह-सुबह बस में सीट मिल जाए, तो किस्मतवाला ही हो सकता है!",
            "bn": "সকালবেলা ভিড় বাসে সিট পেলে, তুমি সত্যিই ভাগ্যবান!",
            "pa": "ਸਵੇਰੇ ਭਰੀ ਹੋਈ ਬੱਸ ਵਿੱਚ ਸੀਟ ਮਿਲਣਾ? ਵੱਡੀ ਕਿਸਮਤ ਚਾਹੀਦੀ ਹੈ!",
            "bho": "सुबह-सुबह भीड़ वाली बस में सीट मिल जाए त भगवान के आशीर्वाद समुझी!",
            "es": "¿Conseguir asiento en un autobús lleno? ¡Eres afortunado!",
            "ja": "混んだバスで座席が取れたら、それは本当に幸運。"
        }
    },
    {
        "title": "chair",
        "translations": {
            "en": "In India, a chair isn't just for sitting — it's political power.",
            "hi": "भारत में कुर्सी सिर्फ बैठने की चीज़ नहीं, यह राजनीति का केंद्र है।",
            "bn": "ভারতে চেয়ার মানে শুধু বসার নয়, এটা ক্ষমতার প্রতীক।",
            "pa": "ਭਾਰਤ 'ਚ ਕੁਰਸੀ ਸਿਰਫ਼ ਬੈਠਣ ਲਈ ਨਹੀਂ, ਇਹ ਰਾਜਨੀਤੀ ਦੀ ਨਿਸ਼ਾਨੀ ਹੈ!",
            "bho": "भारत में कुरसी मतलब बस बइठे के ना, पूरा राजनीति के गेम हौ!",
            "es": "En India, una silla no es solo para sentarse, ¡es símbolo de poder!",
            "ja": "インドでは椅子は座るためだけでなく、権力の象徴でもある。"
        }
    },
    {
        "title": "umbrella",
        "translations": {
            "en": "Umbrellas protect from rain — and from nosy neighbors' gaze!",
            "hi": "छाता सिर्फ बारिश में नहीं, पड़ोसन की नज़र से भी बचाता है!",
            "bn": "ছাতা বৃষ্টি থেকে রক্ষা করে, আর পাড়া-প্রতিবেশীর নজর থেকেও!",
            "pa": "ਛਤਰੀ ਸਿਰਫ਼ ਮੀਂਹ ਤੋਂ ਨਹੀਂ, ਪੜੋਸਣ ਦੀ ਨਜ਼ਰ ਤੋਂ ਵੀ ਬਚਾਉਂਦੀ ਹੈ!",
            "bho": "छाता ना त बस बरसात के बचाव ह, ई त पड़ोसिन के नजर से भी बचावेला!",
            "es": "El paraguas protege de la lluvia y de la mirada de los vecinos.",
            "ja": "傘は雨よけだけでなく、隣人の視線からも守ってくれる。"
        }
    },
    {
        "title": "backpack",
        "translations": {
            "en": "Our school bags were heavier than our future.",
            "hi": "स्कूल बैग इतना भारी होता था कि लग रहा होता था हम ट्रेकिंग पर निकले हैं।",
            "bn": "স্কুল ব্যাগ ছিল এত ভারী, মনে হতো হিমালয়ে যাচ্ছি।",
            "pa": "ਸਕੂਲ ਦਾ ਬੈਗ ਇੰਨਾ ਭਾਰੀ ਹੁੰਦਾ ਸੀ, ਜਿਵੇਂ ਟ੍ਰੈਕਿੰਗ 'ਤੇ ਜਾ ਰਹੇ ਹੋਏ!",
            "bho": "स्कूल के बस्ता अइसन लागे जइसन ट्रेकिंग पर जातानी हमनी!",
            "es": "La mochila escolar pesaba más que nuestro futuro.",
            "ja": "学生の頃のリュックは、将来よりも重かった。"
        }
    },
    {
        "title": "person",
        "translations": {
            "en": "To Indian parents, a 'real person' is either an engineer or a doctor.",
            "hi": "भारतीय माता-पिता के लिए 'व्यक्ति' वही है जो इंजीनियर या डॉक्टर हो।",
            "bn": "ভারতীয় অভিভাবকদের কাছে প্রকৃত মানুষ মানে ইঞ্জিনিয়ার বা ডাক্তার।",
            "pa": "ਹਿੰਦੂ ਮਾਪਿਆਂ ਲਈ 'ਅਸਲ ਬੰਦਾ' ਜਾਂ ਤਾਂ ਇੰਜੀਨੀਅਰ ਜਾਂ ਡਾਕਟਰ ਹੁੰਦਾ ਹੈ।",
            "bho": "भारतीय माई-बाप के नजर में 'बड़का आदमी' त इंजीनियर ना त डॉक्टर होई!",
            "es": "Para los padres indios, una 'persona real' es ingeniero o doctor.",
            "ja": "インドの親にとって「ちゃんとした人」とは、エンジニアか医者である。"
        }
    },
    {
        "title": "apple",
        "translations": {
            "en": "The kid who eats an apple daily still surrenders before golgappas.",
            "hi": "\"An apple a day\" वाले बच्चे आज भी गोलगप्पे के सामने हार जाते हैं।",
            "bn": "যে ছেলে প্রতিদিন আপেল খায়, সে-ও ফুচকার সামনে হেরে যায়।",
            "pa": "ਜਿਹੜਾ ਬੱਚਾ ਹਰ ਰੋਜ਼ ਸੇਬ ਖਾਂਦਾ, ਉਹ ਵੀ ਗੋਲਗੱਪਿਆਂ ਅੱਗੇ ਹਾਰ ਜਾਂਦਾ।",
            "bho": "रोज सइब खाये वाला बच्चा भी गोलगप्पा देख के पिघल जाला!",
            "es": "El niño que come una manzana al día aún se rinde ante los golgappas.",
            "ja": "毎日リンゴを食べる子供でも、ゴールガッパの前では負けてしまう。"
        }
    },
    {
        "title": "mirror",
        "translations": {
            "en": "Every Indian mirror knows all dance rehearsals and selfie fails.",
            "hi": "हर भारतीय आईना सारे डांस रिहर्सल और सेल्फी फेल जानता है।",
            "bn": "প্রতিটা ভারতীয় আয়না জানে সব নাচের মহড়া ও সেলফি ফেইল।",
            "pa": "ਹਰ ਭਾਰਤੀ ਆਇਨਾ ਨੱਚਣ ਦੀ ਰਿਹਰਸਲ ਅਤੇ ਫੇਲ ਸੈਲਫੀਆਂ ਦਾ ਗਵਾਹ ਹੁੰਦਾ।",
            "bho": "हर भारतीय आईना डांस के रिहर्सल आउर सेल्फी के फेल देख चुकल बा।",
            "es": "Cada espejo indio conoce todos los ensayos de baile y fracasos de selfies.",
            "ja": "インドの鏡はすべてのダンス練習とセルフィー失敗を見てきた。"
        }
    },
    {
        "title": "scooter",
        "translations": {
            "en": "Three people, one scooter, and a goat — Indian jugaad at its finest!",
            "hi": "तीन लोग, एक स्कूटर, और एक बकरी — असली भारतीय जुगाड़!",
            "bn": "তিনজন মানুষ, এক স্কুটার, আর একটা ছাগল — এক কথায় ভারতীয় জুগাড়।",
            "pa": "ਤਿੰਨ ਬੰਦੇ, ਇੱਕ ਸਕੂਟਰ ਤੇ ਇੱਕ ਬਕਰੀ — ਭਾਰਤੀ ਜੁਗਾੜ ਦੀ ਮਿਸਾਲ!",
            "bho": "तीन गो आदमी, एगो स्कूटर आउर एगो बकरी — सच्चा भारतीय जुगाड़!",
            "es": "Tres personas, un scooter y una cabra — el máximo nivel de jugaad indio.",
            "ja": "3人、1台のスクーター、そしてヤギ — これぞインドの知恵（ジュガード）！"
        }
    },
    {
        "title": "tv",
        "translations": {
            "en": "Indian TVs have seen more drama than Shakespeare ever wrote.",
            "hi": "भारतीय टीवी ने जितना ड्रामा देखा है, शेक्सपियर ने भी नहीं लिखा।",
            "bn": "ভারতীয় টিভিতে যে পরিমাণ নাটক দেখা যায়, শেকসপিয়ারও অবাক হতেন।",
            "pa": "ਭਾਰਤੀ ਟੀਵੀ ਨੇ ਜਿੰਨਾ ਡ੍ਰਾਮਾ ਵੇਖਿਆ, ਸ਼ੈਕਸਪੀਅਰ ਵੀ ਨਹੀਂ ਲਿਖ ਸਕਿਆ।",
            "bho": "भारतीय टीवी पर जेतना ड्रामा चलल बा, शेक्सपियर के किताब भी फेल हो जाई।",
            "es": "La televisión india ha visto más drama que todas las obras de Shakespeare.",
            "ja": "インドのテレビはシェイクスピアよりも多くのドラマを見てきた。"
        }
    },
    {
        "title": "fridge",
        "translations": {
            "en": "The fridge isn't for food. It's a shrine for leftovers and old pickles.",
            "hi": "फ्रिज खाना के लिए नहीं, बचे हुए खाने और अचार के लिए होता है।",
            "bn": "ফ্রিজ মানে বেঁচে থাকা খাবার আর পুরনো আচার রাখার জায়গা।",
            "pa": "ਫਰਿੱਜ ਖਾਣੇ ਲਈ ਨਹੀਂ, ਬਚੇ ਹੋਏ ਆਚਾਰਾਂ ਲਈ ਹੁੰਦਾ।",
            "bho": "फ्रिज में नया खाना कम, बाचल अचार ज़्यादा मिले।",
            "es": "La nevera no es para comida nueva, es para sobras y encurtidos antiguos.",
            "ja": "冷蔵庫は新しい食べ物のためではなく、残り物と古い漬物のための神殿だ。"
        }
    },
    {
        "title": "shoes",
        "translations": {
            "en": "Buying new shoes? Be ready for the ritual of applying oil and walking slowly.",
            "hi": "नए जूते लिए? अब तेल लगाओ और धीरे-धीरे चलो की रसम निभाओ।",
            "bn": "নতুন জুতো কিনলে তেল লাগিয়ে ধীরে হাঁটার রীতিনীতি পালন করো।",
            "pa": "ਨਵੇਂ ਜੁੱਤੇ ਖਰੀਦੇ? ਹੁਣ ਤੇਲ ਲਾ ਕੇ ਆਹਿਸਤਾ ਚਲਣ ਦੀ ਰਸਮ ਆ ਗਈ।",
            "bho": "नया जूता मिलते ही , तेल लगाके, धीरे-धीरे चलो!",
            "es": "¿Zapatos nuevos? Prepárate para el ritual de caminar lento y aplicar aceite.",
            "ja": "新しい靴を買った？オイルを塗ってゆっくり歩く儀式が始まる。"
        }
    },
    {
        "title": "fan",
        "translations": {
            "en": "Indian ceiling fans: faster than emotions, louder than arguments.",
            "hi": "पंखा इतना तेज चलता है, लगता है तूफान आ गया!",
            "bn": "ভারতীয় পাখা এত জোরে চলে, মনে হয় সাইক্লোন আসছে।",
            "pa": "ਭਾਰਤੀ ਫੈਨ ਐਨੀ ਤੇਜ਼ੀ ਨਾਲ ਘੁੰਮਦਾ ਕਿ ਲੱਗੇ ਤੂਫਾਨ ਆ ਗਿਆ!",
            "bho": "हमरे घरे के पंखा तेज चल के झगड़ा से तेज आवज करेला!",
            "es": "Los ventiladores indios giran más rápido que las emociones.",
            "ja": "インドの天井ファンは感情より早く、議論よりうるさい。"
        }
    },
    {
        "title": "clock",
        "translations": {
            "en": "Time is an illusion. Indian standard time is more of a suggestion.",
            "hi": "समय बस एक सुझाव है, IST मतलब 'In Some Time'!",
            "bn": "সময় কেবল একটা ধারনা, IST মানে — কিছু সময়ে আসবো।",
            "pa": "IST ਮਤਲਬ — ਥੋੜ੍ਹੀ ਦੇਰ 'ਚ ਆਉਂਦੇ ਹਾਂ।",
            "bho": "IST मतलब - आईब त आईब, बाकी टाईम के भरोस ना!",
            "es": "IST significa: Llego... cuando llego.",
            "ja": "ISTとは「そのうち来る時間」の略です。"
        }
    },
    {
        "title": "mobile",
        "translations": {
            "en": "Indians check phones even if there's no notification — just vibes.",
            "hi": "फोन बिना नोटिफिकेशन के भी हर 5 मिनट में देखना एक कला है।",
            "bn": "নোটিফিকেশন না থাকলেও ফোন দেখা — একটা অভ্যাস।",
            "pa": "ਕੋਈ ਨੋਟੀਫਿਕੇਸ਼ਨ ਨਾ ਹੋਵੇ ਤਾਂ ਵੀ ਫੋਨ ਵੇਖਣਾ ਆਦਤ ਬਣ ਗਈ।",
            "bho": "कोई मैसेज ना आवे तबो फोन देखे के आदत बा।",
            "es": "Aunque no haya notificaciones, revisamos el móvil... por si acaso.",
            "ja": "通知がなくても携帯を見るのは、インド人の本能です。"
        }
    },
    {
        "title": "soap",
        "translations": {
            "en": "One soap, ten people — Indian hostel luxury.",
            "hi": "एक साबुन से पूरी हॉस्टल नहा लेती है!",
            "bn": "একটা সাবান দিয়ে গোটা হোস্টেল স্নান করে।",
            "pa": "ਇੱਕ ਸਾਬਣ ਨਾਲ ਸਾਰੀ ਹੋਸਟਲ ਇਨਹਾ ਕਰ ਲੈਂਦੀ।",
            "bho": "एगो साबुन से पूरा हॉस्टल नहावेला!",
            "es": "Un jabón para diez personas — lujo hostalero indio.",
            "ja": "インドのホステルでは1個の石鹸で10人が使う。"
        }
    },
    {
        "title": "remote",
        "translations": {
            "en": "Controlling the TV remote is a generational war.",
            "hi": "टीवी का रिमोट — सबसे बड़ा घर का संग्राम।",
            "bn": "রিমোট নিয়ে ঘরে প্রতিদিনের যুদ্ধ।",
            "pa": "ਟੀਵੀ ਰਿਮੋਟ ਲੈ ਕੇ ਘਰ 'ਚ ਰੋਜ਼ ਦੀ ਲੜਾਈ ਹੁੰਦੀ।",
            "bho": "रिमोट के कब्ज़ा मतलब घर में महाभारत सुरु!",
            "es": "El control remoto de TV — campo de batalla familiar.",
            "ja": "テレビのリモコンは家庭内戦争の主な原因。"
        }
    }
]

# Insert into MongoDB
try:
    for story in stories:
        db.stories.insert_one(story)
    print("✅ Successfully inserted 20 cultural stories with multi-language translations.")
except Exception as e:
    print(f"❌ Error inserting stories: {e}")

# Optional: Close the connection
client.close()