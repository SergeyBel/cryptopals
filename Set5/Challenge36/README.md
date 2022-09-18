По заданию нужно реализовать протокол Secure Remote Password 
Не буду копировать описание протокола, напишу только доказательство корректности:  
Client: $s = (B - kg^x)^{a + ux} = (kg^x + g^b - kg^x)^{a + ux} = g^{b(a + ux)}$  
Server: $s = (Av^u)^b = (g^ag^{ux})^b = g^{b(a + ux)}$
