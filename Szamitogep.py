class Szamitogep:

    def __init__(self,szabadMemoria: float, bekapcsolva: bool):
        if szabadMemoria == 0:
            self.szabadMemoria  = 1024
        else:
            self.szabadMemoria = szabadMemoria
        if bekapcsolva == 0:
            self.bekapcsolva == False
        else:
            self.bekapcsolva = bekapcsolva

    def kapcsol(self):
        if self.bekapcsolva:
            self.bekapcsolva = False
        else:
            self.bekapcsolva = True

    def programMasol(self,meret: float)->bool:
        sikeres = False
        if self.bekapcsolva and self.szabadMemoria-meret > 0:
            self.szabadMemoria -= meret
            sikeres = True
        return sikeres

    def __str__(self):
        if self.bekapcsolva:
            szoveg = "bekapcsolva"
        else:
            szoveg = "kikapcsolva"
        return f"Szabad memória méret {self.szabadMemoria}, állapot: {szoveg}."