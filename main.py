# ornek = "Hayatın en önemli gerçeği samimiliktir. Bu itibarla hayat ile bağı olan edebiyat mutlaka samimi bir edebiyattır denilebilir. " \
#         "Hayatı en gizli en karışık yönleriyle anlatmayan duygularımızı tıpkı hayatta olduğu gibi saf ve derin bir şekilde duyurmayan elemlerimizi felaketlerimizi açık açık yansıtmayan bir edebiyat hayat ile ilgisiz ve sahte bir edebiyattır. " \
#         "Öyle bir edebiyat kelimeleri dizip onları işleyen pek hünerli kuyumcular çıkarabilir. Belki onlar çok süslüçok göz alıcı şeyler yapabilirler. Fakat ne yazık ki bütün bu sahte ürünler muntazam kış bahçelerinde yetişen iri yapraklı " \
#         "parlak renkli çiçeklere benzer. Uzaklığından dolayı bize çok çekici çok harikulade görünen o meçhul sıcak iklimlerin bu göz kamaştıran ürünleri nasıl açık bir havaya sert bir rüzgara dayanamazsa hayat ile ilgisi olmayan böyle bir edebiyat da " \
#         "zamanın sonsuz kasırgaları önünde süpürülüp gitmeye mahkumdur. Halbuki bedii his hislerimizin en ilahi ve en samimisidir. Akşam rüzgarı ile inleyen bir çam ormanının karanlık hışırtıları ne kadar tabii ise ruhun güzellik karşısında duyduğu hisler de " \
#         "hayatın en derin ve anlaşılmaz köşelerinden birdenbire fırlayıp çıktığı için her şeyden çok samimidir. İşte bunun gibi milletler için de güzel ve iyi telakkilerinden daha milli hiçbir şey yoktur. Bir toplumu başkalarından ayırmak isterseniz onun din " \
#         "ve ahlak hakkındaki güzellik hakkındaki samimi duygularını arayınız. Çünkü bunlar doğrudan doğruya ruhundan koptuğu için hayatının en samimi taraflarıdır."

ornek = "In digital communication system, we basically show the discrete time signals in form of symbols and" \
        "send the signals with help of digital signal procesors. Pulse Code Modulation (PCM) is a scheme for" \
        "representing analog data in the digital form and transmiting them. We can digitize all forms of analog" \
        "data, including full motion video, music and virtual reality (VR) using PCM. The PCM encoded signals are" \
        "in binary form; that is, there can be only two possible states, represented by logic 1 and logic 0. A sine" \
        "wave is sampled and quantised in PCM. The analog signal amplitude is sampled at regular intervals of" \
        "time. Firstly, we have to convert the continuos signals to their discrete form for example converting of" \
        "sound wave to some samples. This is done by a process called sampling. At the source of " \
        "communication system, the amplitude of the analog signal is sampled at regular intervals. Next is the " \
        "quantization. The amplitude of the analog signal at each sampling is taken to the closest pre-determined " \
        "levels. This process is called quantization. The number of levels is always a power of two. The output of" \
        "pulse code modulation is series of binary numbers, represented by some power of two bits. At the " \
        "receiverend, pulse code demodulator converts the binary numbers into pulses. These pulses are" \
        "processed to get back the original analog waveform. The way by which we can reconstruct the actual " \
        "signal completely from the sampling signal is given by the nyquist criterion, which says a perfect " \
        "reconstruction of the sample version is because if the sampling rate is more than 2 times the maximum " \
        "frequency."

metin = ""
for karakter in ornek:
    if karakter.isalpha():
         metin += karakter

metin = metin.lower()
metin = metin.replace(" ", "")

metin2 = metin[:101]
metin3 = metin[:1001]

sozluk = {}
sozluk2 = {}
sozluk3 = {}
sozluk4 = {}

for kelime in metin:
    if kelime in sozluk:
        sozluk[kelime] += 1
    else:
        sozluk[kelime] = 1

print("\nToplam harf sayıları\n")
print(sozluk)

for kelime in metin2:
    if kelime in sozluk2:
        sozluk2[kelime] += 1
    else:
        sozluk2[kelime] = 1

print("\nİlk 100 Kelimenin Frekansı (% olarak)\n")
print(sozluk2)

for kelime in metin3:
    if kelime in sozluk3:
        sozluk3[kelime] += 1
    else:
        sozluk3[kelime] = 1


for kelime, frekans in sozluk3.items():
     yuzde = int((frekans / 1000) * 100)
     sozluk4[kelime] = yuzde

print("\nİlk 1000 Kelimenin Frekansı (% olarak ve tam kısımları )\n")
print(sozluk4)