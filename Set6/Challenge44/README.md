Задание демонстрирует, что нельзя использовать повторяющиеся значения k для различных сообщений при использовании подписи DSA - это приводит к раскрытию секретного ключа

## Решение
Указанная формула для нахождения k является решением системы уравненений расчёта s для двух различных сообщений

1. Если k одинаковые, то $r = g^k \pmod p \pmod q$ также будут одинаковые. Находим в файле два сообщения с одинаковым r, это сообщения
```
msg: Listen for me, you better listen for me now. 
s: 1267396447369736888040262262183731677867615804316
r: 1105520928110492191417703162650245113664610474875
m: a4db3de27e2db3e5ef085ced2bced91b82e0df19


msg: Pure black people mon is all I mon know. 
s: 1021643638653719618255840562522049391608552714967
r: 1105520928110492191417703162650245113664610474875
m: d22804c4899b522b23eda34d2137cd8cc22b9ce8
```
Можно это сделать и автоматически, но поскольку файл небольшой легче руками

1. Рассчитываем $k = (m1 - m2) * (s1 - s2)^{-1} \pmod q$
1. Рассчитываем x по известному к, как в Задании 43 
