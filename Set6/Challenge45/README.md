Задание демонстрирует, что важно тщательно проверять параметры, которые используются в подписи DSA

Случай $g = 0 \pmod p$:    
В этом случае проверка любой подписи для любого сообщения будет верной, потому что
$r = g ^ k \pmod p = 0$  
$v = g^{u_1} y^{u_2} = 0$  
И v всегда совпадает с r  


Случай $g = 1 \pmod p$:  
В этом случае можно составить такую подпись, которая будет подходить к любому тексту  
z - любое число  
$r = y ^ z \pmod p \pmod q$  
$s = r z^{-1} \pmod q$ 

Тогда при проверке:
$v = g^{u_1} y^{u_2} = y^{u_2} = y^{rw} = y^{rr^{-1}z} = y^z = r$  
