Задание демонтрирует слабость xor-шифра с повторяющимся ключом. Дан текст, зашифрованный xor-шифром с повторяющимся ключом и нам нужно дешифровать его (для xor-шифрования это равносильно нахождению ключа). Отмечу, что хотя это классическая задача расшифровки шифра Виженера, и любой, кто занимался криптографией, знает как решать её в теории, оешить на практике и довести подобную задачу до ответа не так просто как это звучит в теории

## Общая идея
Процесс дешифровки состоит из следующих шагов:
1. Определяем длину ключа
2. Разбиваем текст на блоки так, что в один блок входят байты, которые шифроутся на одном и том же байте ключа
3. Каждый такой блок зашифрован однобайтовым xor-шифром: дефшифруем каждый блок, собираем из полученных байтов ключ
4. Расшифровываем текст на полученном ключе

# Теория  
## Определение длины ключа
Для начала определим *расстояние хэмминга* для двух битовый строк - это количество бит, в которых эти строки различаются. Или, перефразируя, минимальное количество бит в одной строке, которые нужно инвертировать, чтобы получить вторую

Например, для строк `0011` и `1001` расстояние будет равно 2, так как они различаются в нулевом и втором бите  


Расстояние хэмминга будет использоваться как мера "случайности" для битовых строк. Идея состоит в том, что расстояние хэмминга для двух строк английского текста будет отличаться от расстояния хэмминга для двух случайных строк. Мы будем использовать относительное расстояние хэмминга, т.е. расстояние хэмминга, делёное на длину строки, это позволит нам сравнивать между собой "случайность" пар строк разной длины  

Так относительное расстояние хэмминга для строк из примера равно $2 / 4 = 0.5$  

Для определения длины ключа перебираем возможную длину ключа (в задании дана подсказка, что длина ключа лежит в пределах от 2 до 40), для каждой длины
1. Берём два блока текста данной длины
2. Считаем относительное расстояние хэмминга между этими блоками
3. Длина, при которой будет получено минимальное расстояние хэмминга, и будет искомой длиной ключа

## Разбивка текста
После того, как длина ключа найдена, текст разбивается на блоки так, что в каждом блоке содержатся все байты, которые шифруются на одном и том же байте ключа
Например, текст 'Burn' и длина ключа равна 3, тогда блоки будут:  
('B', 'n') - шифруются первым байтом ключа  
('u') - шифруются вторым  байтом ключа  
('n') - шифруются третьим байтом ключа  

## Получение отдельный байтов ключа
Каждый такой блок зашифрован однобайтовым xor-ом, который мы уже взламывали в задании 3. Применяя указанный метод, получаем все байты ключа

## Расшифровка
Собираем полный ключ из полученных байтов и расшифровывает текст

# Практика

## Определение длины ключа
Если брать два блока, то длина ключа может быть определена не совсем верно, в таком случае можно проверять несколько длин с наименьшими значениями. Чтобы улучшить точность определения можно брать несколько блоков (при решении было выбрано значение 4, это определяет длину правильно сразу) и считать среднее между парными расстояниями хэмминга

## Расшифровка
После применения указанного метода получаем:  
Ключ: `TerMinAtor X: Bring the noiSe`  
Текст:
```
'mbaCk and I'm ringin' thE belL
a rockin' on the mikewhilE tHe fly girls yell
InecstAsyin the back of me
WEll tHats my DJ Deshay cuttiN' alL tHem Z's
Hittin' hardand Thegirlies goin' crazy *VaniLlas on the mike, man Im noT lAzy.

I'm lettin' mydrugkiCk in
It controls mymoutH aNd I begin
To just lEt itflOw, let my concepts gO
MypoSse's to the side yelLin',GoVanilla Go!

Smooth'cauSe That's the way I willbe
andif you don't give a Damn,thEn
Why you starin' aT me *Soget off 'cause I conTrol Thestage
There's no diSsin'alLowed
I'm in my own Phase
THe girlies sa y they Love Me And that is ok
And Ican DanCe better than any kiD n' PlaY

Stage 2 -- Yea thE oneya wanna listen to
Its ofF mY head so let the beaT plaY tHrough
So I can funkit uP aNd make it sound good
3 yo -- Knock on some wOod
forgood luck, I like myrhymEs Atrocious
SupercalafRagilIstIcexpialidocious
I'man eFfeCt and that you can bEt
IcaN take a fly girl andmakeheR wet.

 SAmson to Delilah
TheRe's No Denyin', You can try To haNg *But you'll keep tryiN' togeT my style
Over and Over,prActice makes perfect *But Notif you're a loafer. *
Youllget nowhere, no placE, notiMe, no girls
Soon --Oh mY GOd, homebody, you proBablyeaT
Spaghetti with a sPoon!CoMe on and say it!

ViP. VAniLla Ice yep, yep, I'mcomiN' Hard like a rhino
InToxicAtiNg so you stagger likE a wIno
So punks stop tryinG andgiRl stop cryin'
VanilLa IcE iS sellin' and you peoPle aRe Buyin'
'Cause why thE freAksare jockin' like CraZy GlUe *Movin' and groovin' TryinG tO sing along
All thrOugh Theghetto groovin' thisheresoNg
Now you're amazedby tHe vIP posse.

Steppin'so hArdlike a German Nazi
startLedby the bases hittin'grouNd *There's no trippin' On miNe,I'm just gettin' dowN
SpArkAmatic, I'm hangin' tIght LikE a fanatic
You trapPed mE oNce and I thought thaT
YoU mIght have it
So stepdownanD lend me your ear
'↑9 inmytime! You, '90 is myyear♫
*You're weakenin' fasT, YO☺ aNd I can tell it
YouR bodY'sgettin' hot, so, so i cansmEll it
So don't be mAd anD dOn't be sad
'Cause tHe lyRicS belong to ICE, You Can cAllme Dad
You're pitchIn' afiT, so step back and eNdure
LEt the witch doctor, ice, Do The dance to cure
Socomeupclose and don't be sQuare
YOu wanna battle me --AnytIme♀ anywhere

You thouGht tHatI was weak, Boy, youre dEadwrong
So come on, eVerybOdyand sing this song
- play that funky musicSay,gowhite boy, go white Boy gO
Play that funky musicGo wHitE boy, go white boy, Go
LAy Down and boogie and pLay tHatfunky music till youdie.

play that funky musicComeon♀ Come on, let me heaR
PlAy That funky music whitE boyyoU say it, say it
PlaY thaT fUnky music A little lOudernoW
Play that funky muSic, WhiTe boy Come on, Come On, COmeon
Play that funky Music
```


Видно, что текст уже читается и даже можно найти первоисточник, но тем не менее в нём некоторые буквы в верхнем регистре. Это произошло потому что программа не совсем правильно определила ключ и вместо маленьких букв определила правильными большие. Можно было попробовать ещё покрутить метрику, но легче поправить огрехи автоматической дешифровки вручную, в итоге:  
Ключ: `Terminator X: Bring the noise`  
Текст:
```
I'm back and I'm ringin' the bell
A rockin' on the mike while the fly girls yell
In ecstasy in the back of me
Well that's my DJ Deshay cuttin' all them Z's
Hittin' hard and the girlies goin' crazy
Vanilla's on the mike, man I'm not lazy.

I'm lettin' my drug kick in
It controls my mouth and I begin
To just let it flow, let my concepts go
My posse's to the side yellin', Go Vanilla Go!

Smooth 'cause that's the way I will be
And if you don't give a damn, then
Why you starin' at me
So get off 'cause I control the stage
There's no dissin' allowed
I'm in my own phase
The girlies sa y they love me and that is ok
And I can dance better than any kid n' play

Stage 2 -- Yea the one ya' wanna listen to
It's off my head so let the beat play through
So I can funk it up and make it sound good
1-2-3 Yo -- Knock on some wood
For good luck, I like my rhymes atrocious
Supercalafragilisticexpialidocious
I'm an effect and that you can bet
I can take a fly girl and make her wet.

I'm like Samson -- Samson to Delilah
There's no denyin', You can try to hang
But you'll keep tryin' to get my style
Over and over, practice makes perfect
But not if you're a loafer.

You'll get nowhere, no place, no time, no girls
Soon -- Oh my God, homebody, you probably eat
Spaghetti with a spoon! Come on and say it!

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino
Intoxicating so you stagger like a wino
So punks stop trying and girl stop cryin'
Vanilla Ice is sellin' and you people are buyin'
'Cause why the freaks are jockin' like Crazy Glue
Movin' and groovin' trying to sing along
All through the ghetto groovin' this here song
Now you're amazed by the VIP posse.

Steppin' so hard like a German Nazi
Startled by the bases hittin' ground
There's no trippin' on mine, I'm just gettin' down
Sparkamatic, I'm hangin' tight like a fanatic
You trapped me once and I thought that
You might have it
So step down and lend me your ear
'89 in my time! You, '90 is my year.

You're weakenin' fast, YO! and I can tell it
Your body's gettin' hot, so, so I can smell it
So don't be mad and don't be sad
'Cause the lyrics belong to ICE, You can call me Dad
You're pitchin' a fit, so step back and endure
Let the witch doctor, Ice, do the dance to cure
So come up close and don't be square
You wanna battle me -- Anytime, anywhere

You thought that I was weak, Boy, you're dead wrong
So come on, everybody and sing this song

Say -- Play that funky music Say, go white boy, go white boy go
play that funky music Go white boy, go white boy, go
Lay down and boogie and play that funky music till you die.

Play that funky music Come on, Come on, let me hear
Play that funky music white boy you say it, say it
Play that funky music A little louder now
Play that funky music, white boy Come on, Come on, Come on
Play that funky music
```

