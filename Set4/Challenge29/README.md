Данная атака работает не только для хеш-функции SHA1, а для любой хэш-функции, построенной по схожему принципу

Алгоритм работы хеш-функции:
1. Дополнение сообщения до полного блока
2. Обрабатывается блок за блоком функцией сжатия $h_i = H(m_i, h_{i-1}), h_0 = const$
3. Последнее $h$ является хэшем сообщения

Так как последнее полученное $h$ является результатом работы без какой-либо пост обработки, знание этого $h$
эквивалетно знанию состояния функции сжатия после обработки определённого сообщения  

Поэтому если нам известен хеш какого-то сообщения, то мы можем постоить хеш для сообшения, которое содержит исходное в качестве префикса,
начав вычислять функцию сжатия не с начального состояния, а с состояния $h$
 
 
Нам нужно получить верный MAC для сообщения
`key || original-message || padding || new-message` имея MAC для сообщения  `key || original-message`  

Для этого мы:
1. Даём на вход оракулу `original-message`, получаем в ответ `h = SHA1(key || original-message || padding)`
3. Начинаем вычисление функции SHA1, для сообщения `key || original-message || padding || new-message || padding` но не со значения $h_0$, а со значения $h$. Мы не знаем ключ, но нам не нужно его значение, а только длина, чтобы вычислить правильный паддинг 
4. В результате получаем верное хеш-значения для сообщения `key || original-message || padding || new-message`