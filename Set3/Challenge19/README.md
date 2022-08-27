В задании нужно расшифровать набор текстов, зашифрованных на одном и том же ключе режима CTR  

На самом деле к режиму CTR задание не имеет никакого отношения, он используется только чтобы сгенерировать гамму (ключ для xor-шифрования). 
По сути задание состоит в расшифровке текстов, зашифрованных xor-шифром на одном и том же ключе

Хотя по описанию нужно заниматься классическим статичстсическим анализом, подбирая буквы\сочетания букв, для меня это было довольно скучно, поэтмому я решал задание на основании взлома шифра Виженера (Задание 6).
Только потом  увидел, что для того есть отдельное Задание 20, поэтому они решены одинаковым способом

1. Первые 16 байт гаммы можно получить, используя способ из Задания 6
2. После этого сообщения становятся осмысленными и дальнешие байты ключа можно подобрать опираясь на смысл сообщения.
Наверняка можно и автоматическим перебором, отсеивая явно неправильные (непечатные, не подходящие под сочетания английский букв и т.п.) - не проверял, в любом случае это несложно

```
I have met them at close of day
Coming with vivid faces
From counter or desk among grey
Eighteenth-century houses.
I have passed with a nod of the head
Or polite meaningless words,
Or have lingered awhile and said
Polite meaningless words,
And thought before I had done
Of a mocking tale or a gibe
To please a companion
Around the fire at the club,
Being certain that they and I
But lived where motley is worn:
All changed, changed utterly:
A terrible beauty is born.
That woman's days were spent
In ignorant good will,
Her nights in argument
Until her voice grew shrill.
What voice more sweet than hers
When young and beautiful,
She rode to harriers?
This man had kept a school
And rode our winged horse.
This other his helper and friend
Was coming into his force;
He might have won fame in the end,
So sensitive his nature seemed,
So daring and sweet his thought.
This other man I had dreamed
A drunken, vain-glorious lout.
He had done most bitter wrong
To some who are near my heart,
Yet I number him in the song;
He, too, has resigned his part
In the casual comedy;
He, too, has been changed in his turn.
Transformed utterly:
A terrible beauty is born.
```
