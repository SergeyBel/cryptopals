Задание демонстрирует две вещи:  

1. Режим ECB уязвим к атаке заменой\удаления блока
2. Шифрование не обеспечивает целостность сообщения


В задании очень сложно придуман оракул, можно было сделать его гораздо проще, поэтому сначала опишу общую идею: 
Если в шифротексте заменить один блок на другой, зашифрованный на том же ключе, то сообщение будет успешно расшифровано со вставленной информацией  


Решение задания:  
Сначала нам нужно получить шифротекст блока `admin\0xb...\0xb` - это зашифрованный текст = строка 'admin' + pkcs7 паддинг до полного блока.
Для этого мы передаём оракулу email, состоящий из 10 символов 'A' и строки admin\0xb...\0xb'. Тогда в зашифрованный текст будем иметь вид

`email=A...A` - 1 блок  
`admin\0xb...\0xb` - 2 блок   
`&uid=10&role=user` - остальные блоки  

Вырезая из шифротекста второй блок, получаем необходимый зашифрованный блок


Теперь подаём на вход оракулу email, состоящий из 13 символов, зашифрованный текст:  
`email=...&uid=10&role=` - 1 и 2 блок   
`user...` - 3 блок    

Заменяем последний блок на ранее полученыый зашифрованный блок `admin\0xb...\0xb` и передаём на вход оракулу расшифрования